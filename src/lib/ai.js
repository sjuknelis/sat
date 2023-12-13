import OpenAI from "openai";
import {readFileSync} from "fs";
import {mkdir, writeFile} from "fs/promises";
import {exec} from "child_process";

const chatgpt = new OpenAI({
    apiKey: readFileSync("apikey.txt").toString()
});

async function runGptPrompt(jsonMode, gptFour, prompt) {
    let properties = {
        model: gptFour ? "gpt-4-1106-preview" : "ft:gpt-3.5-turbo-1106:personal::8UbLB1cc",
        messages: [{role: "user", content: prompt.trim()}]
    };
    if (jsonMode) properties.response_format = {
        type: "json_object"
    }
    const gptData = await chatgpt.chat.completions.create(properties);
    console.log(gptData.choices[0].message.content)
    return gptData.choices[0].message.content;
}

export async function makePassage(type) {
    const data = await runGptPrompt(true, false, `
Generate an SAT reading passage of at least 45 lines with the following type: ${type}.
Provide this passage as a JSON array of strings, where each string is one line, as follows: {passage: string[]}.
The response should contain nothing but the passage in its JSON format, broken up into reasonably sized lines (at least 8 words per line).
Each line should start with a line number.
It is critical that the passage be at least 45 lines long and that each line is at least 10 words long.
    `);
    return JSON.parse(data).passage.map(item => item.split(" ").slice(1).join(" "));
}

export async function makeQuestions(passage, count, category) {
    const data = await runGptPrompt(true, false, `
Here is an SAT reading passage:
${passage.map((line, index) => `${index + 1} ${line}`).join("\n")}

Create ${count} difficult SAT reading questions for this passage${category ? ` that fall under the following category: ${category}` : ""}. Provide the correct answer. When listing the answer choices, do not include any letter prefixes like "A."
Some of the questions should refer to specific quotes in the passage. When quoting from the passage, include the line number.
Represent the question in JSON array format as follows, and don't include anything other than the JSON representation in your response: {question_set :{question: string, answers: string[], correct_answer_index: number}[]}
    `);
    return JSON.parse(data).question_set;
}

export async function makeDataGraph(passage) {
    const description = await runGptPrompt(false, true, `
Here is an SAT reading passage:
${passage.map((line, index) => `${index + 1} ${line}`).join("\n")}

Describe a potential graph that could go with this passage. Include in your description all data and labels that would be placed on this graph. Someone should be able to create the graph in its entirety from this description.
    `);

    let code = await runGptPrompt(false, true, `
Here is an SAT reading passage:
${passage.map((line, index) => `${index + 1} ${line}`).join("\n")}

Here is a description of a graph that could go with this passage:
${description}

Write Python code to create this graph using matplotlib and save it in the local directory as "img.png".
Do not output anything other than the Python code. Do not include any explanation of the code or of the graph.
    `);
    code = code
        .split("\n")
        .filter(line => line.trim() != "```python" && line.trim() != "```")
        .join("\n");

    const dirName = Math.floor(Math.random() * 10000 + 10000).toString(36);
    const dirPath = `static/imagedata/${dirName}`
    await mkdir(dirPath);
    await writeFile(`${dirPath}/code.py`, code);

    const execPromise = new Promise((resolve, reject) => {
        exec(`cd ${dirPath} && python3 code.py`, (err, stdout, stderr) => {
            if (err) reject(err);
            resolve();
        });
    });
    await execPromise;

    return {
        image: dirName,
        description
    }
}

export async function makeDataQuestions(description) {
    const data = await runGptPrompt(true, true, `
Here is a description of a graph included with an SAT reading passage:
${description}

Create 2 difficult SAT reading questions that fall under the category of data reasoning with the provided graph. Provide the correct answer. When listing the answer choices, do not include any letter prefixes like "A."
Some of the questions should refer to specific quotes in the passage. When quoting from the passage, include the line number.
Represent the question in JSON array format as follows, and don't include anything other than the JSON representation in your response: {question_set: {question: string, answers: string[], correct_answer_index: number}[]}
    `);
    return JSON.parse(data).question_set;
}
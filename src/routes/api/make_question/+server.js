import OpenAI from "openai";
import {readFileSync} from "fs";
import {json} from "@sveltejs/kit";

const chatgpt = new OpenAI({
    apiKey: readFileSync("apikey.txt").toString()
});

export async function GET({ url }) {
    const question = JSON.parse(url.searchParams.get("q"));

    const prompt = `
Here is an SAT reading passage:
${question.passage.map((line, index) => `${index + 1} ${line}`).join("\n")}

Here is a sample question for this passage:
${question.question_item.question}
${question.question_item.answers.map((answer, index) => `${["A", "B", "C", "D"][index]}. ${answer}`).join("\n")}
Correct answer: ${["A", "B", "C", "D"][question.question_item.correct_answer_index]}

Please create a difficult question in the style of this question for this passage${question.question_item.category ? ` in this category: ${question.question_item.category}` : ""}. Provide the correct answer. When listing the answer choices, do not include any letter prefixes like "A."
Represent the question in JSON format as follows, and don't include anything other than the JSON representation in your response: {question: string, answers: string[], correct_answer_index: number}
    `.trim();

    const gptData = await chatgpt.chat.completions.create({
        model: "gpt-4",
        messages: [{role: "user", content: prompt}]
    });
    const gptQuestion = JSON.parse(gptData.choices[0].message.content || "");
    return json(gptQuestion);
}
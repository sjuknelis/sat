import {json} from "@sveltejs/kit";
import {readFile} from "fs/promises";
import {makePassage, makeQuestions, makeDataGraph, makeDataQuestions} from "$lib/ai";

export async function GET({ url }) {
    const passageId = url.searchParams.get("passage_id");
    const category = url.searchParams.get("category");
    const aiType = url.searchParams.get("ai_type");

    let passage;
    if (passageId != "ai") passage = JSON.parse((await readFile(`data/${passageId}.json`)).toString()).passage;
    else passage = await makePassage(aiType);

    let questionSet, graph;
    if (passageId != "ai") {
        if (category == "all") {
            questionSet = JSON.parse((await readFile(`data/${passageId}.json`)).toString()).questionSet;
        } else {
            questionSet = await makeQuestions(passage, 8, category);
        }
    } else {
        if (category == "all") {
            if (aiType.toLowerCase() == "science") {
                questionSet = await makeQuestions(passage, 8);
                console.log(questionSet)
                graph = await makeDataGraph(passage);
                console.log(graph)
                questionSet.push(...await makeDataQuestions(graph.description));
                console.log(questionSet)
            }
        } else if (category == "Data Reasoning") {
            passage.graph = await makeDataGraph(passage);
            questionSet = await makeDataQuestions(passage.graph.description);
        } else {
            questionSet = await makeQuestions(passage, 8, category);
        }
    }

    return json({
        passage,
        question_set: questionSet,
        graph
    });
}
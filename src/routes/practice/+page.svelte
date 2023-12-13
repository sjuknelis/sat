<script>
    import {page} from "$app/stores";
    import {onMount} from "svelte";

    let practiceSet;
    
    const url = $page.url.searchParams;
    onMount(async () => {
        practiceSet = await (await fetch(`/api/get_practice_set?${url.toString()}`)).json();
        console.log(practiceSet);
    });

    function getButtonColor(question, answerIndex) {
        if (question.provided_answer_index === undefined) return "white";

        if (question.correct_answer_index == answerIndex) return "lightgreen";
        else if (question.provided_answer_index == answerIndex) return "lightyellow";
        else return "pink";
    }

    function submitResponse(questionIndex, answerIndex) {
        const questionSet = practiceSet.question_set[questionIndex];
        if (questionSet.provided_answer_index !== undefined) return;

        questionSet.provided_answer_index = answerIndex;
        if (answerIndex != questionSet.correct_answer_index) {
            practiceSet.question_set.splice(questionIndex + 1, 0, null);
            (async () => {
                const request = {
                    passage: practiceSet.passage,
                    question_item: practiceSet.question_set[questionIndex]
                }
                practiceSet.question_set[questionIndex + 1] = await (await fetch(`/api/make_question?q=${JSON.stringify(request)}`)).json();
                practiceSet = practiceSet;
            })();
        }
        practiceSet = practiceSet;
    }
</script>

{#if practiceSet}
    <div class="container">
        <div class="row main">
            <div class="col-6">
                {#each practiceSet.passage as line, lineIndex}
                    <div class="row">
                        <div class="col-1">{(lineIndex + 1) % 5 == 0 ? lineIndex + 1 : ""}</div>
                        <div class="col-11">{line}</div>
                    </div>
                {/each}
                {#if practiceSet.graph}
                    <!-- svelte-ignore a11y-missing-attribute -->
                    <img src={`/imagedata/${practiceSet.graph.image}/img.png`} />
                {/if}
            </div>
            <div class="col-6">
                {#each practiceSet.question_set as question, questionIndex}
                    {#if question}
                        <p>{question.question}</p>
                        {#each question.answers as answer, answerIndex}
                            <button
                                on:click={() => submitResponse(questionIndex, answerIndex)}
                                style={`background-color: ${getButtonColor(question, answerIndex)}`}
                            >
                                {answer}
                            </button>
                        {/each}
                    {:else}
                        <p>...</p>
                    {/if}
                    <hr />
                {/each}
            </div>
        </div>
    </div>
{:else}
    <p>AI is working...</p>
{/if}

<style>
    button {
        display: block;
    }
    .row.main > .col-6 {
        overflow-y: scroll;
        height: 100vh;
    }
</style>
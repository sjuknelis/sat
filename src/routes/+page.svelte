<script>
    import {PASSAGE_IDS, PASSAGE_TYPES, SKILLS} from "../lib/const";

    const randomFrom = arr => arr[Math.floor(Math.random() * arr.length)];
</script>

<div class="container">
    <div class="row">
        <div class="col-6">
            <h4>Real passage practice</h4>
            {#each PASSAGE_IDS as id}
                <button class="btn btn-secondary" on:click={() => location.href = `/practice/?passage_id=${id}&category=all`}>{id}</button>
            {/each}
        </div>
        <div class="col-6">
            <h4>AI passage practice</h4>
            {#each PASSAGE_TYPES as type}
                <button class="btn btn-secondary" on:click={() => location.href = `/practice/?passage_id=ai&category=all&ai_type=${type}`}>{type}</button>
            {/each}
        </div>
    </div>
    <div class="row">
        <div class="col-6">
            <h4>Real skill practice</h4>
            {#each SKILLS as skill}
                <button class="btn btn-secondary" on:click={() => location.href = `/practice/?passage_id=${randomFrom(PASSAGE_IDS)}&category=${skill}`}>{skill}</button>
            {/each}
        </div>
        <div class="col-6">
            <h4>AI skill practice</h4>
            {#each SKILLS as skill}
                <button class="btn btn-secondary" on:click={() => location.href = `/practice/?passage_id=ai&category=${skill}&ai_type=${randomFrom(PASSAGE_TYPES)}`}>{skill}</button>
            {/each}
        </div>
    </div>
</div>

<style>
    button {
        margin: 0.2em;
    }
</style>
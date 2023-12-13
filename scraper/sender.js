function sendContent(title) {
    const passageTexts = Array.from(document.querySelectorAll(".passage-text")).map(el => el.innerText);
    if ( passageTexts.length > 1 ) {
        for ( let i = 0; i < passageTexts.length; i++ ) passageTexts[i] = `Passage ${i + 1}\n${passageTexts[i]}`;
    }
    const passage = passageTexts.join("\n");

    const questions = Array.from(document.querySelectorAll(".perseus-group-invalid-answer > .perseus-renderer > .paragraph:first-child")).map(el => el.innerText);
    const answers = Array.from(document.querySelectorAll(".checkbox-and-option")).map(el => el.innerText);
    const content = {
        passage,
        questions,
        answers,
        title
    };

    const req = new XMLHttpRequest();
    req.open("GET", `http://localhost:8000/upload?data=${encodeURIComponent(JSON.stringify(content))}`);
    req.send();
}
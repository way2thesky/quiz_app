function fixString(string){
    string = string.replace(/&quot;/g, '"')
    string = string.replace(/&ldquo;/g, '"')
    string = string.replace(/&rdquo;/g, '"')
    string = string.replace(/&#039;/g, "'")
    return string
}

function RandomQuestion(){
    fetch('https://opentdb.com/api.php?amount=1&type=boolean')
        .then((page) => page.json())
        .then(data => {
            const question = document.getElementById("question");
            question.value = fixString(String(data['results'][0]['question']))
            const answer = document.getElementsByName('is_true')
            if (data['results'][0]['correct_answer'] === 'True'){
                answer[0].checked = true
            }else if (data['results'][0]['correct_answer'] === 'False') {
                answer[1].checked = true
            }
        });}
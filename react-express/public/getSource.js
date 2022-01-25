function get_source(document_body) {
    console.log("immediate function test22");
    return document_body.innerText;
}

function get_url(){
    var newURL = window.location.protocol + "//" + window.location.host + "/" + window.location.pathname;
    console.log("current url");
    return newURL
}

chrome.extension.sendMessage({
    action: "getSource",
    source: get_url(document.body)
});


// chrome.extension.sendMessage({
//     action: "getSource",
//     source: get_url(document.body)
// });

// function dragText() {
//     console.log("mouse move");

//     let text;

//     if(window.getSelection) {
//         text = window.getSelection().toString();
//     }
//     else if (document.selection) {
//         text = document.selection.createRange().text;
//     }
//     return text;
// }

// document.onmouseup = function() {
//     if(chrome.browserAction.onClicked.addListener) {
//         console.log("working");
//     }
// }

function displayText(translated) {
    let newDIV = document.createElement("div");
    let newP = document.createElement("p");
    let closeButton = document.createElement("span");

    closeButton.innerHTML = "X";
    closeButton.addEventListener('click', function() {
        this.parentElement.style.display = "none";
    });
    newP.innerHTML = translated;

    newDIV.appendChild(closeButton);
    newDIV.appendChild(newP);

    newDIV.setAttribute("class","translatedTextView");
    newDIV.style.padding = "1rem";
    newDIV.style.position = "fixed";
    newDIV.style.zIndex = "1";
    newDIV.style.right = "0";
    newDIV.style.top = "0";
    newDIV.style.textAlign = "right";
    newDIV.style.background = "#FFFFFF";
    newDIV.style.border = "2px solid #CEECF5";
    newDIV.style.borderRadius = "1em 0 1em 1em";

    document.body.appendChild(newDIV);
}

function express_url() {
    var url = get_url()
    fetch(url, {mode: 'cors'})
        .then((response) => response.json())
        .then((data) => (function() {

        })())
        .catch((error) => console.log(error))
}
const colors = ['blue', 'yellow', 'purple', 'pink', 'green', 'darkblue', 'lightblue', 'lightgreen', 'grey', 'black']

function changeColor(id) {
    let box = document.getElementById(id);
    box.style.background = colors[Math.round(Math.random() * 10)];
}


function init() {
    const quantity = 13;
    for (let i = 1; i <= 13; i++) { 
        let container = document.getElementById("container");
        let box = document.createElement("div");
        box.className = "box";
        box.id = 'box-' + i;
        box.innerText = i;
        container.appendChild(box);

}
}

init()
    
// Gather all objects

var names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
var objects = []

for (var i = 0; i < names.length; i++) {
    objects.push(document.getElementById(names[i]))
}

// Give all objects the ability to change

function addCoolStuff(element) {
    element.addEventListener("click", function () {
        var curTxt = element.textContent
        if (curTxt === " ")
            element.textContent = "X"
        else if (curTxt === "X")
            element.textContent = "O"
        else
            element.textContent = " "
    })
}

for (var i = 0; i < objects.length; i++)
    addCoolStuff(objects[i])

// Add reset to button
var button = document.querySelector("#resetBtn")
button.addEventListener("click", function () {
    for (var i = 0; i < objects.length; i++)
        objects[i].textContent = " "
})
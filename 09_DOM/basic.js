var oneClick = document.querySelector("#oneClick")
var dblClick = document.querySelector("#dblClick")
var hover = document.querySelector("#hover")

oneClick.addEventListener("click", function () {
    oneClick.textContent = "I have been clicked!"
    oneClick.style.color = "blue"
})
dblClick.addEventListener("dblclick", function () {
    dblClick.textContent = "I have been clicked twice!"
    dblClick.style.color = "red"
})
hover.addEventListener("mouseover", function () {
    hover.textContent = "I am being hovered over!"
    hover.style.color = "purple"
})
hover.addEventListener("mouseout", function () {
    hover.textContent = "Hover over this one!"
    hover.style.color = "black"
})
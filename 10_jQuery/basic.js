$('#oneClk').click(function () {
    $(this).text("You clicked me!")
    $(this).css("color", "red")
})
$('#dblClk').dblclick(function () {
    $(this).text("You clicked me twice!")
    $(this).css("color", "blue")
})
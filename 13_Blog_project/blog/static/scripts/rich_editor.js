$("#fake_text").click(function (e) {
    if (window.getSelection) {
        var sel = window.getSelection()
        if (sel.toString().length > 0) {
            $('.toast').toast('show');
            $('.toast').css({
                position: "absolute",
                left: e.pageX,
                top: e.pageY
            })
        } else {
            $('.toast').toast('hide');
        }
    }
});

$("#make_text_bold").click(function (e) {
    var span = document.createElement("span")
    span.className = "bold_text"

    var selected = window.getSelection()
    var range = selected.getRangeAt(0)

    span.appendChild(range.extractContents())
    range.insertNode(span)

    selected.removeAllRanges();
    selected.addRange(range);
});

$("#make_text_italic").click(function (e) {
    var span = document.createElement("span")
    span.className = "italic_text"

    var selected = window.getSelection()
    var range = selected.getRangeAt(0)

    span.appendChild(range.extractContents())
    range.insertNode(span)

    selected.removeAllRanges();
    selected.addRange(range);
});

$("#make_text_strike").click(function (e) {
    var span = document.createElement("span")
    span.className = "strike_text"

    var selected = window.getSelection()
    var range = selected.getRangeAt(0)

    span.appendChild(range.extractContents())
    range.insertNode(span)

    selected.removeAllRanges();
    selected.addRange(range);
});

$("#make_text_clear").click(function (e) {
    var span = document.createElement("span")
    span.className = "clean_text"

    var selected = window.getSelection()
    var range = selected.getRangeAt(0)

    span.appendChild(document.createTextNode(range.toString()))

    range.deleteContents()
    range.insertNode(span)
    range.selectNode(span)

    selected.removeAllRanges();
    selected.addRange(range);
});

$("#save_draft_btn").click(function (e) {
    $("#actual_text").val($("#fake_text").html())
    $("#actual_title").val($("#fake_title").text())
});

$("#fake_text").html($("#fake_text").text())
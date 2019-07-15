var player1Name = prompt("Player 1 (blue) name:")
var player2Name = prompt("Player 2 (red) name:")

$("#players")[0].textContent = player1Name + " vs " + player2Name

var bluesTurn = true
var gameover = false

function changeColor() {
    $(this).prop("disabled", true)
    if (bluesTurn)
        $(this).addClass("isBlue")
    else
        $(this).addClass("isRed")

}

//$('.empty-cell').click(changeColor)

const NUM_COLUMNS = 7
var columns = {}

for (var i = 0; i < NUM_COLUMNS; i++) {
    columns["col" + i] = 0
}

function processMove() {
    if (gameover) {
        return
    }
    var colNum = $(this).attr('id')
    var colIdx = Number(colNum[3])
    var lowestRow = columns[colNum]
    var row = $("#row" + lowestRow)

    var corrPlace = row.children()[colIdx]
    // this is the correct <tr> so the button
    // is its child[0]
    var corrButton = corrPlace.children[0]

    gameover = checkIfWon(colIdx, lowestRow)

    changeColor.apply(corrButton)
    columns[colNum] += 1

    if (gameover) {
        var winner = player2Name
        if (bluesTurn)
            winner = player1Name
        $("#title")[0].textContent = "Game over!"
        $("#players")[0].textContent = winner + " won!"
    }
    bluesTurn = !bluesTurn

    // check if it's a tie
    for (var i = 0; i < NUM_COLUMNS; i++) {
        if (columns["col" + i] < 6)
            return
    }

    $("#title")[0].textContent = "Game over!"
    $("#players")[0].textContent = "It's a tie!"

}

$('.empty-cell').click(processMove)

function checkIfWon(currCol, currRow) {
    //Check if the game should be over

    var coords = [
        // horizontal
        [
            [0, 1],
            [0, 2],
            [0, 3]
        ],
        [
            [0, -1],
            [0, 1],
            [0, 2]
        ],
        [
            [0, -2],
            [0, -1],
            [0, 1]
        ],
        [
            [0, -3],
            [0, -2],
            [0, -1]
        ],
        // diagonal 
        [
            [1, 1],
            [2, 2],
            [3, 3]
        ],
        [
            [-1, -1],
            [1, 1],
            [2, 2]
        ],
        [
            [-2, -2],
            [-1, -1],
            [1, 1]
        ],
        [
            [-3, -3],
            [-2, -2],
            [-1, -1]
        ],
        [
            [1, -1],
            [2, -2],
            [3, -3]
        ],
        [
            [1, -1],
            [2, -2],
            [3, -3]
        ],
        [
            [-1, 1],
            [1, -1],
            [2, -2]
        ],
        [
            [-2, 2],
            [-1, 1],
            [1, -1]
        ],
        [
            [-3, 3],
            [-2, 2],
            [-1, 1]
        ],
        // vertical
        [
            [-1, 0],
            [-2, 0],
            [-3, 0]
        ]
    ]

    var color = "isBlue"
    if (!bluesTurn) {
        color = "isRed"
    }

    for (var i = 0; i < coords.length; i++) {
        var set = coords[i]
        matching = 0
        for (var j = 0; j < set.length; j++) {
            var rowCorr = set[j][0]
            var colCorr = set[j][1]
            var newCol = currCol + colCorr
            var newRow = currRow + rowCorr

            if (newRow < 0 || newCol < 0 || newCol > 6 || newRow > 5) {
                continue
            }

            // console.log("Row: " + newRow + " Col: " + newCol)
            var wholeRow = $("#row" + newRow)
            var selectedItem = wholeRow.children()[newCol]
            var selectedButton = selectedItem.children[0]

            if (selectedButton.classList.contains(color))
                // console.log("Row: " + newRow + " Col: " + newCol)
                matching += 1
        }
        if (matching >= 3) {
            return true
        }
    }
    return false
}
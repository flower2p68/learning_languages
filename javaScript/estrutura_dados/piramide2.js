const character = "#";
const count = 8;
let inverted = true;

function padRow(rowNumber, rowCount) {
    return " ".repeat(rowCount - rowNumber) + character.repeat(2 * rowNumber - 1) + " ".repeat(rowCount - rowNumber);
}

for (let i = 1; i <= count; i++) {
    if (inverted) {
        console.log(padRow(count - i + 1, count));
    } else {
        console.log(padRow(i, count));
    }
}

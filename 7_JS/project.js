alert("You will now be asked four questions!");

var firstName = prompt("What is your first name:");
var lastName = prompt("What is your last name:");
var age = prompt("How old are you:");
var height = prompt("How tall are you:");
var pet = prompt("What is the name of your pet:");

if ((firstName[0] !== lastName[0]) ||
    (age <= 20 || age >= 30) ||
    (height < 170) ||
    (pet[pet.length - 1] !== "y")) {
    console.log("You are not the spy, go away!");
}
else {
    console.log("Hello there spy, the secret message is: BananaBread");
}
const changeCalculator = document.querySelector('.change');
var loadPage;

var total_ammount = 0;


//Function to calculate the amount of change need to be given to the customer and what coins are needed for it.
//Output is a Dictionary in a style {"Change Type", Number to Give}
var calculateChange = function(price, cash){
    var returnValue = cash - price;
    var change = {};

    //array of coin types
    const coinTypes = ["£20" , "£10" ,"£5" , "£2" ,"£1" , "50p" , "20p" , "10p","5p" , "2p" , "1p"];
    const coinValues = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1];

    var amount;

    for (var i = 0; i < coinValues.length; i++){
        amount = Math.floor(returnValue/coinValues[i]);
        if (amount > 0){
            change[coinTypes[i]] = amount;
            returnValue = returnValue % coinValues[i];
        }
    }

    return change;
}

//function to update the total amount the customer gave to the staff
changeCalculator.addEventListener('click', e => {
    if (
        e.target.classList.contains('btn')
    ) {
        console.log("button pressed");

        //Extra number from the message box
        var totalPrice = document.getElementById("main-box").value.replace( /^\D+/g, '') * 100;


        let stringChangeOutput = "Change to Give: ";
        console.log(totalPrice);

        if (e.target.classList.contains('nine')){
            total_ammount *=10;
            total_ammount += 9;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('eight')){
            total_ammount *=10;
            total_ammount += 8;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('seven')){
            total_ammount *=10;
            total_ammount += 7;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('six')){
            total_ammount *=10;
            total_ammount += 6;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('five')){
            total_ammount *=10;
            total_ammount += 5;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('four')){
            total_ammount *=10;
            total_ammount += 4;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('three')){
            total_ammount *=10;
            total_ammount += 3;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('two')){
            total_ammount *=10;
            total_ammount += 2;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('one')){
            total_ammount *=10;
            total_ammount += 1;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('zero')){
            total_ammount *=10;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('clear')){
            total_ammount = 0;
            document.getElementById("enteredCash").value = total_ammount/100;
        }
        if (e.target.classList.contains('delete')){
            total_ammount = Math.floor(total_ammount / 10)
            document.getElementById("enteredCash").value = total_ammount/100;
        }

        if (total_ammount > totalPrice){
            var tempDict = calculateChange(totalPrice , total_ammount);
            for(var key in tempDict) {
                var value = tempDict[key];

                console.log(key);
                console.log(value);

                stringChangeOutput += key.toString() + " x " + value.toString() + " , ";
            }

            document.getElementById("enteredCash").value = stringChangeOutput;
            document.getElementById("main-box").value = "Payment Complete";
        }

    }
});

//Functions which deal with controlling the number of tickets select using buttons.

function minusAdult(){
    if (document.getElementById("tAdult").value > 0){
        document.getElementById("tAdult").value -= 1;
    }
}
function addAdult(){
    document.getElementById("tAdult").value++;
}

function minusSenior(){
    if (document.getElementById("tSenior").value > 0){
        document.getElementById("tSenior").value -= 1;
    }
}

function addSenior(){
    document.getElementById("tSenior").value++;
}

function minusChild(){
    if (document.getElementById("tChild").value > 0){
        document.getElementById("tChild").value -= 1;
    }
}

function addChild(){
    document.getElementById("tChild").value++;}




//Changes the message in card Payment page that the payment was successful
function paymentSuccess(){
    document.getElementById("messageBox").value = "Payment Accepted, Print Tickets";
    document.getElementById("messageBox").style.backgroundColor = "green";
    document.getElementById("messageBox").style.color = "white";
}

//Changes the message in card Payment page that the payment was not successful
function paymentFailed(){
    document.getElementById("messageBox").value = "Payment Failed, Please Try Again";
    document.getElementById("messageBox").style.backgroundColor = "red";
    document.getElementById("messageBox").style.color = "black";
}





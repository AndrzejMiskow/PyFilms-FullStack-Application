
//Function to calculate the amount of change need to be given to the customer and what coins are needed for it.
var calculateChange = function(price, cash){
    var returnValue = cash - price;
    var change = {};

    //array of coin types
    const coinTypes = ["£20" , "£10" ,"£5" , "£2" ,"£1" , "50p" , "20p" , "10p","5p" , "2p" , "1p"];
    const coinValues = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1];

    var amount;

    for (var i = 0; i < coinValues.length; i++){
        amount = Math.floor(returnValue/coinValues[i]);
        console.log(amount);
        if (amount > 0){
            change[coinTypes[i]] = amount;
            returnValue = returnValue % coinValues[i];
            console.log(returnValue);
        }
    }

    return change;
}

console.log(calculateChange(176,200));
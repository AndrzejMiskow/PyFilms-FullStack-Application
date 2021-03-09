function onLoaderFunc()
{
    $(".seatStructure *").prop("disabled", true);
    $(".displayerBoxes *").prop("disabled", true);
}

var totalTickets = 0;

function takeData()
{
    //Adding up tickets from the form
    totalTickets = Number($("#qChild").val()) + Number($("#qAdult").val()) + Number($("#qSenior").val());

    if (totalTickets <= 0)
    {
        alert("Please select a valid number of tickets");
    }
    else
    {
        alert("Select Your Seats");
    }
}




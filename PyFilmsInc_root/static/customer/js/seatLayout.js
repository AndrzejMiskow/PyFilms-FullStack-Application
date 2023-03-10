//contains all the elements in the seat layout
const seatLayout = document.querySelector('.seatLayout');

//All seats which are not reserved
const seats = document.querySelectorAll('.row-seat .seat');

//number of tickets
var totalTickets = 0;
var selectedSeatsCount = 0;

function takeData()
{
    var child = document.getElementsByName("qChild");
    
    //Adding up tickets from the form
    //If movie rated 18+, child seats won't be selectable
    if (child.length<=0)
    {
        totalTickets = Number($("#qAdult").val()) + Number($("#qSenior").val());
    }
    else 
    {
        totalTickets = Number($("#qChild").val()) + Number($("#qAdult").val()) + Number($("#qSenior").val());
    }
    
    if (totalTickets <= 0)
    {
        alert("Please select a valid number of tickets");
    }
    else
    {
        alert("Select your seats");
    }
}

//Updates the number of selected Seats Can be used to update the database
function updateSelected (){
    const selectedSeats = document.querySelectorAll('.row-seat .selected');

    selectedSeatsCount = selectedSeats.length;
}

function confirmSeats(){
    const selectedSeats = document.querySelectorAll('.row-seat .selected');

    //We can use seatsIndex to store a seat in the DB as selected (after confirmation)
    const seatsIndex = [...selectedSeats].map(seat => [...seats].indexOf(seat));

    document.getElementById("SelectedSeatsID").value = seatsIndex.toString();

}


// Function to select seats, if the number of tickets is bigger than 0
//The click contains a seat and is not occupied then it will be selected
seatLayout.addEventListener('click', e => {
    if (
        totalTickets > 0 &&
        e.target.classList.contains('seat') &&
        !e.target.classList.contains('occupied')
    ) {
        if ( selectedSeatsCount < totalTickets){
            e.target.classList.toggle('selected');
            updateSelected();
        }
        else //if the number of selected seats is greater than the total number of tickets
            {
                //We need to deselect a selected seat to be able to allocate another
                if(e.target.classList.contains('selected')){
                    e.target.classList.toggle('selected');
                    updateSelected();
                }
                else{
                    alert("Deselect a seat to pick a new one");
                }
        }
    }

});

function minusAdult(){
    if (document.getElementById("qAdult").value > 0){
        document.getElementById("qAdult").value -= 1;
    }
}
function addAdult(){
    document.getElementById("qAdult").value++;
}

function minusSenior(){
    if (document.getElementById("qSenior").value > 0){
        document.getElementById("qSenior").value -= 1;
    }
}

function addSenior(){
    document.getElementById("qSenior").value++;
}

function minusChild(){
    if (document.getElementById("qChild").value > 0){
        document.getElementById("qChild").value -= 1;
    }
}

function addChild(){
    document.getElementById("qChild").value++;
}

//Will remove required fields from card details
function payLatter(){
    document.getElementById("cExpiration").required = false;
    document.getElementById("cCVV").required = false;
    document.getElementById("cNumber").required = false;
    document.getElementById("cName").required = false;
}



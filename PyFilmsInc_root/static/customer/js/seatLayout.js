//contains all the elements in the seat layout
const seatLayout = document.querySelector('.seatLayout');

//All seats which are not reserved
const seats = document.querySelectorAll('.row .seat:not(.reserved)');

//number of tickets
var totalTickets = 0;
var selectedSeatsCount = 0;

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

function updateSelected (){
    const selectedSeats = document.querySelectorAll('.row .selected');

    //We can use seatsIndex to store a seat in the DB as selected (after confirmation)
    const seatsIndex = [...selectedSeats].map(seat => [...seats].indexOf(seat));

    selectedSeatsCount = selectedSeats.length;

};

// Function to select seats, if the number of tickets is bigger than 0
//The click contains a seat and is not occupied then it will be selected
seatLayout.addEventListener('click', e => {
    if (
        totalTickets > 0 &&
        selectedSeatsCount < totalTickets &&
        e.target.classList.contains('seat') &&
        !e.target.classList.contains('occupied')
    ) {
        e.target.classList.toggle('selected');

        updateSelected();
    }
});




// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    let forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

// validation function for the card number that prints alert to the user
function cardNumber(input) {
    let regexCardNumber = /\b\d{16}\b/
    if(input.value.match(regexCardNumber)) {
       // console.table(input.value.match(regexCardNumber));
        return true;
    } else {
        alert("Card number provided does not have 16 digits.");
        return false;
    }
}

// disables input of card number if character typed is not a digit
const CARDNUMBER_ALLOWED_CHARS = /\d/
document.querySelector("input[id='cNumber']").addEventListener("keypress", evt => {
    if (!CARDNUMBER_ALLOWED_CHARS.test(evt.key)) {
        evt.preventDefault();
    }
})

// validation function for the expiry date that prints alert to the user
function expDate(input) {
    let regexExpDate = /\b\d{2}\/\d{2}\b/
    if(input.value.match(regexExpDate)) {
        return true;
    } else {
        alert ("Expiry date provided is not of correct format MM/YY.")
        return false;
    }
}

// disables input of expiration date if character typed is not a digit or a forward slash
const EXPDATE_ALLOWED_CHARS = /[\d\/]/
document.querySelector("input[id='cExpiration']").addEventListener("keypress", evt => {
    if (!EXPDATE_ALLOWED_CHARS.test(evt.key)) {
        evt.preventDefault();
    }
})

// validation function for the CVV that prints alert to the user
function CVV(input) {
    let regexCVV = /\d/
    if(input.value.match(regexCVV)) {
        return true;
    } else {
        alert("CVV provided is not of correct format (3 or 4 digits).")
        return false;
    }
}

// disables input of CVV if character typed is not a digit
const CVV_ALLOWED_CHARS = /\d/
document.querySelector("input[id='cCVV']").addEventListener("keypress", evt => {
    if (!CVV_ALLOWED_CHARS.test(evt.key)) {
        evt.preventDefault();
    }
})

document.getElementById("checkout-submit").addEventListener("click", function() {
    cardNumber(document.form1.cNumber)
});

document.getElementById("checkout-submit").addEventListener("click", function() {
    expDate(document.form1.cExpiration)
})

document.getElementById("checkout-submit").addEventListener("click", function() {
    CVV(document.form1.cCVV)
})

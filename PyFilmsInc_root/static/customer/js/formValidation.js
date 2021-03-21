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

// validation function for the card number
function cardNumber(input) {
    if(input.value.length === 16) {
      return true;
    } else {
        alert("Card number provided does not have 16 digits.");
        return false;
    }
}

// validation function for the expiry date
function expDate(input) {
    if(input.value.length === 5) {
        return true;
    } else {
        alert ("Expiry date provided is not of correct format MM/YY.")
        return false;
    }
}

// validation function for the CVV
function CVV(input) {
    if(input.value.length === 3 || input.value.length === 4) {
        return true;
    } else {
        alert("CVV provided is not of correct format (3 or 4 digits).")
        return false;
    }
}

document.getElementById("checkout-submit").addEventListener("click", function() {
    cardNumber(document.form1.cNumber)
});

document.getElementById("checkout-submit").addEventListener("click", function() {
    expDate(document.form1.cExpiration)
})

document.getElementById("checkout-submit").addEventListener("click", function() {
    CVV(document.form1.cCVV)
})

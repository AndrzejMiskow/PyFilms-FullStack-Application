$(document).ready(function(){

    $('input[type=password]').keyup(function() {
        var password = $(this).val();

        //validate the length
        if ( password.length < 8 ) {
            $('#length').removeClass('valid').addClass('invalid');
        } else {
            $('#length').removeClass('invalid').addClass('valid');
        }

        //validate letter
        if ( password.match(/[A-z]/) ) {
            $('#letter').removeClass('invalid').addClass('valid');
        } else {
            $('#letter').removeClass('valid').addClass('invalid');
        }

        //validate capital letter
        if ( password.match(/[A-Z]/) ) {
            $('#capital').removeClass('invalid').addClass('valid');
        } else {
            $('#capital').removeClass('valid').addClass('invalid');
        }

        //validate number
        if ( password.match(/\d/) ) {
            $('#number').removeClass('invalid').addClass('valid');
        } else {
            $('#number').removeClass('valid').addClass('invalid');
        }

        //validate space
        if ( password.match(/[^a-zA-Z0-9\-\/]/) ) {
            $('#space').removeClass('invalid').addClass('valid');
        } else {
            $('#space').removeClass('valid').addClass('invalid');
        }

    }).focus(function() {
        $('#password_info').show();
    }).blur(function() {
        $('#password_info').hide();
    });

});


//Only allows text input and some symbols
function textValidation(txt) {
    txt.value = txt.value.replace(/[^a-zA-Z-'\n\r.]+/g, '');
}

//checking is passwords match
function checkPass()
{
    var pass1 = document.getElementById('password1');
    var pass2 = document.getElementById('password2');
    var message = document.getElementById('confirmMessage');

    var correct = "#66cc66";
    var invalid = "#ff6666";

    if(pass1.value == pass2.value){
        pass2.style.backgroundColor = correct;
        message.style.color = correct;
        message.innerHTML = "Passwords Match"
    }else{
        pass2.style.backgroundColor = invalid;
        message.style.color = invalid;
        message.innerHTML = "Passwords Do Not Match!"
    }
}
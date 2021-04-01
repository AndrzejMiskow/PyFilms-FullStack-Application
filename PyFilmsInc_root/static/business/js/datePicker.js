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

let dateClass='.date-pick';
$(document).ready(function() {
    if (document.querySelector(dateClass).type !== 'date') {
        let dateCSS = document.createElement('link');
        dateCSS.type='text/css';
        dateCSS.rel='stylesheet';
        dateCSS.href='//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/base/jquery-ui.css';

        dateCSS.onload=function() {
            let dateJS = document.createElement('script');
            dateJS.type='text/javascript';
            dateJS.src='//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js';

            dateJS.onload=function() {
                $(dateClass).datepicker({
                    dateFormat: "yy-mm-dd"
                });
            }
            document.body.appendChild(dateJS);
        }
        document.body.appendChild(dateCSS);
    }
});

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
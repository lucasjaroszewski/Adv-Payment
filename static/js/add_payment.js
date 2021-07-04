// Get Cookies for CSRFToken
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// Gets user ID and e-mail
const user_id = JSON.parse(document.getElementById('user_id').textContent);
const user_email = JSON.parse(document.getElementById('user_email').textContent);


// Objetcts to input into Payment
var Payment_1 = {
    "user": user_id,
    "email": user_email,
    "cnpj": "12.345.6789/0001-10",
    "company_name": "Cool Company",
    "price": "1000.00",
    "expiration_date": "2021-07-21",
    "payment_status": "Available",
}

var Payment_2 = {
    "user": user_id,
    "email": user_email,
    "cnpj": "12.345.6789/0001-12",
    "company_name": "Excelent Company",
    "price": "690.90",
    "expiration_date": "2020-07-21",
    "payment_status": "Expired",
}

var Payment_3 = {
    "user": user_id,
    "email": user_email,
    "cnpj": "12.345.6789/0001-14",
    "company_name": "Great Company",
    "price": "2578.81",
    "expiration_date": "2022-07-21",
    "payment_status": "Available",
}

// Button: Add Payment 1
var button_payment_1 = document.getElementById('payment1_add')
button_payment_1.addEventListener('click', function(e) {

    // Fetches API and creates a new payment
    fetch('/api/payment-create/', {
        method: 'POST',
        headers: {
            'Content-type':'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:
            JSON.stringify(Payment_1)
    })
})

// Button: Add Payment 2
var button_payment_2 = document.getElementById('payment2_add')
button_payment_2.addEventListener('click', function(e) {

    // Fetches API and creates a new payment
    fetch('/api/payment-create/', {
        method: 'POST',
        headers: {
            'Content-type':'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:
            JSON.stringify(Payment_2)
    })
})

// Button: Add Payment 3
var button_payment_3 = document.getElementById('payment3_add')
button_payment_3.addEventListener('click', function(e) {

    // Fetches API and creates a new payment
    fetch('/api/payment-create/', {
        method: 'POST',
        headers: {
            'Content-type':'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:
            JSON.stringify(Payment_3)
    })
})

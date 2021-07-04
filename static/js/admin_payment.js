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


/// Gets user ID and e-mail
const user_id = JSON.parse(document.getElementById('user_id').textContent);
const user_email = JSON.parse(document.getElementById('user_email').textContent);


// Button: Accept
jQuery('#adminTable').on('click', ".accept", function() {
    var $this = $(this);
    var payment_id = $this.attr('id');
    status_update = 'Accepted'

    // Fetch API and updates information of the selected payment
    fetch(`/api/payment-update/${payment_id}/`, {
        method: 'POST',
        headers: {
            'Content-type':'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:
            JSON.stringify({ 'payment_status':status_update, 'email':user_email })
    })
    .then(location.reload())
})

// Button: Deny
jQuery('#adminTable').on('click', ".deny", function() {
    var $this = $(this);
    var payment_id = $this.attr('id');
    status_update = 'Denied'


    // Fetch API and updates information of the selected payment
    fetch(`/api/payment-update/${payment_id}/`, {
        method: 'POST',
        headers: {
            'Content-type':'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:
            JSON.stringify({ 'payment_status':status_update, 'email':user_email })
    })
    .then(location.reload())
})

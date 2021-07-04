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


// Gets username (email)
const user_id = JSON.parse(document.getElementById('user_id').textContent);


// Buttons logic
jQuery('#adminTable').on('click', ".accept", function() {
  var $this = $(this);
  var payment_id = $this.attr('id');
  $.ajax({
    type: 'GET',
    url: `/api/payment-update/${payment_id}`,
    success: function(payment) {
      acceptPayment(payment)
    },
    error: function() {
      console.log('Error: Payment ID not found.')
    }
  });
})

function acceptPayment(payment) {
    payment_id = payment.id
    status_update = 'Accepted'

    fetch(`/api/payment-update/${payment_id}/`, {
        method: 'POST',
        headers:{
            'Content-type':'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify({ 'payment_status':status_update })
    })
    .catch(error => console.log('Error: ' + error.message))
    .then(location.reload())
}

jQuery('#adminTable').on('click', ".deny", function() {
  var $this = $(this);
  var payment_id = $this.attr('id');
  $.ajax({
    type: 'GET',
    url: `/api/payment-update/${payment_id}`,
    success: function(payment) {
      denyPayment(payment)
    },
    error: function() {
      console.log('Error: Payment ID not found.')
    }
  });
})

function denyPayment(payment) {
    payment_id = payment.id
    status_update = 'Denied'

    fetch(`/api/payment-update/${payment_id}/`, {
        method: 'POST',
        headers:{
            'Content-type':'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify({ 'payment_status':status_update })
    })
    .catch(error => console.log('Error: ' + error.message))
    .then(location.reload())
}

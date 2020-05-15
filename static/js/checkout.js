    var total = '{{order.get_cart_total|floatformat:2}}'

    if (user != 'AnonymousUser'){
        document.getElementById('user-info').innerHTML = ''
     }
/*else {
    document.getElementById('form-wrapper').classList.add("hidden");
    document.getElementById('payment-info').classList.remove("hidden");
}

var form = document.getElementById('form')*/

//$(document).ready(function() {
        /*if(sessionStorage.getItem('userInfo')){
            var autoFillInfo = localStorage.getItem('userInfo')
            $('#firstName').text(autoFillInfo['firstName'])
            $('#lastName').html(autoFillInfo['lastName'])
            $('#email').html(autoFillInfo['email'])
            $('#address').html(autoFillInfo['address'])
            $('#address2').html(autoFillInfo['address2'])
            $('#city').html(autoFillInfo['city'])
            $('#country').html(autoFillInfo['country'])
            $('#zip').html(autoFillInfo['zipCode'])
            console.log('breki saved')
    }*/
    $('#submitInfo').on('click', function(e) {
        e.preventDefault()
    console.log('It has been formally submitted...')
        var fName = $('#firstName').val()
        var lName = $('#lastName').val()
        var email = $('#email').val()
        var address = $('#address').val()
        var address2 = $('#address2').val()
        var country = $('#country option:selected').text()
        var city = $('#city').val()
        var zipCode = $('#zip').val()

        var userInfo = {
            'firstName': fName,
            'lastName': lName,
            'email': email,
            'address': address,
            'address2': address2,
            'country': country,
            'city': city,
            'zip': zipCode
        }
    console.log(userInfo)
        sessionStorage.setItem('userInfo',JSON.stringify(userInfo))
        sessionStorage.getItem('userInfo')
        $('#form').submit()
    //form.addEventListener('submit',  function(e) {
    //e.preventDefault()
    //console.log('It has been formally submitted...')
    //})
    })
 //   })




    //document.getElementById('form-button').classList.add("hidden");
    /*document.getElementById('payment-info').classList.remove("hidden");
})
    document.getElementById('make-payment').addEventListener('click', function(e){
        submitFormData()
}) */
/*
function submitFormData(){
    console.log('You are continuing on your checkout journey!')
    var userFormData = {
				'name':null,
				'email':null,
				'total':total,
			}

	    	if (user == 'AnonymousUser'){
	    		userFormData.name = form.name.value
	    		userFormData.email = form.email.value
	    	}
}

    console.log('User Info:', userFormData)

    var url = "/process_order/"
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'form':userFormData }),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log('Success:', data);
            alert('Transaction completed');
            cart = {}
            document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
            window.location.href = "{% url 'cart' %}"
        })

 */

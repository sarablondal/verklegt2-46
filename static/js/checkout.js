var total = '{{order.get_cart_total|floatformat:2}}'


if (user != 'AnonymousUser'){
    document.getElementById('user-info').innerHTML = ''
 }

var form = document.getElementById('form')
form.addEventListener('click', function(e){
    e.preventDefault()
    console.log('Form Submitted...')
    document.getElementById('form-button').classList.add("hidden");
    document.getElementById('payment-info').classList.remove("hidden");
})
    document.getElementById('make-payment').addEventListener('click', function(e){
        submitFormData()
    })

function submitFormData(){
    console.log('Payment button clicked')

    var userFormData = {
        'firstName':null,
        'lastName':null,
        'email':null,
        'address': null,
        'address2': null,
        'country': null,
        'city': null,
        'zip': null,

        'total':total,
    }

    if (user == 'AnonymousUser'){
        userFormData.name = form.name.value
        userFormData.email = form.email.value
    }
    else{
        userFormData.firstName = form.firstName.value
        userFormData.lastName = form.lastName.value
        userFormData.email = form.email.value
        userFormData.address = form.address.value
        userFormData.address2 = form.address2.value
        userFormData.country = form.country.value
        userFormData.city = form.city.value
        userFormData.zip = form.zip.value
    }

    console.log('User Info:', userFormData)

    var url = "/process_order/"
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'form':userFormData, 'shipping':shippingInfo}),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log('Success:', data);
            alert('Transaction completed');
            cart = {}
            document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
            window.location.href = "{% url 'cart' %}"
        })
}
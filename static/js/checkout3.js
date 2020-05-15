$(document).ready(function() {
    var userInfo = sessionStorage.getItem('userInfo')
    var userInfo = JSON.parse(userInfo)
    var fName = userInfo['firstName']
    var lName = userInfo['lastName']
    var email = userInfo['email']
    var address = userInfo['address']
    var address2 = userInfo['address2']
    var country = userInfo['country']
    var city = userInfo['city']
    var zipCode = userInfo['zip']
    $('#userName').html("Name: " + fName + " " + lName)
    $('#userEmail').html("Email: " + email)
    $('#address').html("Address: " + address)
    $('#address2').html("Address 2: " + address2)
    $('#userCity').html("City: " + city)
    $('#userCountry').html("County: " + country)
    $('#userZip').html("Zip Code: " + zipCode)

    var paymentInfo = sessionStorage.getItem(('paymentInfo'))
    var paymentInfo = JSON.parse(paymentInfo)
    var payName = paymentInfo['ccName']
    var payNumber = paymentInfo['ccNumber']
    var payNumberLast4 = payNumber.substr(payNumber.length - 4)
    console.log(payNumberLast4)
    var payExpDate = paymentInfo['ccExp']
    var payCcCvv = paymentInfo['ccCvv']
    $('#cardName').html("Name of cardholder: " + payName)
    $('#cardNumber').html("Card Number: ****-****-****-" + payNumberLast4)
    $('#cardExpDate').html("Expiration date: " + payExpDate)
})

//listen for click on confirm order
$('#confirmOrder').on('click', function(e) {
    //cookies expired/deleted
    document.cookie = "cart=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    cart = {}
    console.log('New Cart Created!', cart)
    //new empty instance of cart created in cookies
    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
})


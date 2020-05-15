$(document).ready(function() {
    console.log("checkout3 working")
    var userInfo = sessionStorage.getItem('userInfo')
    var userInfo = JSON.parse(userInfo)
    console.log(userInfo)
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
    var payExpDate = paymentInfo['ccExp']
    var payCcCvv = paymentInfo['ccCvv']
    $('#cardName').html("Name of cardholder: " + payName)
    $('#cardNumber').html("Card Number: " + payNumber)
    $('#cardExpDate').html("Expiration date: " + payExpDate)
})


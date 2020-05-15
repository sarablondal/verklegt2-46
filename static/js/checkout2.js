console.log('checkout2 working')
$(document).ready(function(){
    $('#make-payment').on('click', function (e) {
        e.preventDefault()
        console.log("payment submitted")
        var ccName = $('#cc-name').val()
        var ccNumber = $('#cc-number').val()
        var ccExp = $('#cc-expiration').val()
        var ccCvv = $('#cc-cvv').val()

        var paymentInfo = {
            'ccName': ccName,
            'ccNumber': ccNumber,
            'ccExp': ccExp,
            'ccCvv': ccCvv
        }
        console.log("Paymentinfo: ", paymentInfo)
        sessionStorage.setItem('paymentInfo', JSON.stringify(paymentInfo))
        $('#paymentForm').submit()

    })
})
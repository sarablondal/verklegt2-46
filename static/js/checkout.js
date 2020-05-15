    var total = '{{order.get_cart_total|floatformat:2}}'

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

    })

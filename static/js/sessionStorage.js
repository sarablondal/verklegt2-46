/*sessionStorage.setItem('debug', "20");
var total = sessionStorage.getItem('debug');
console.log(total);

var total = parseInt( sessionStorage.getItem('debug'));
var quantity = 2;
var updatedTotal = total * quantity;
sessionStorage.setItem('total', updatedTotal);
console.log("this is updated total" + sessionStorage.getItem('total'));

var store = {
    item: "Zelda",
    price: 9.99,
    qty: 2
};
var jsonStr = JSON.stringify(store);
sessionStorage.setItem('store', jsonStr);
console.log(sessionStorage.getItem('store'));
var cartValue = sessionStorage.getItem('store');
var cartobject = JSON.parse(cartValue);
console.log(cartobject);*/
/*
(function( $ ) {
    $.Shop = function( element ) {
        this.$element = $( element ); // top-level element
        this.init();
    };

    $.Shop.prototype = {
        init: function() {
            // initializes properties and methods
        }
    };

    $(function() {
        var shop = new $.Shop( "#site" ); // object's instance
    });

})( jQuery );


$(function() {
    var shop = new $.Shop( "#site" );
    console.log( shop.$element );
});
*/

/* NOTA LOCALSTORAGE frekar því þá save'as það í tölvunni ef browser er lokaður og opnað aftur

sessionStorage.setItem('debug', "20");
var total = sessionStorage.getItem('debug');
console.log(total);


var total = parseInt( sessionStorage.getItem('debug'));
var quantity = 2;
var updatedTotal = total * quantity;
@ -19,6 +22,8 @@ console.log(sessionStorage.getItem('cart'));
var cartValue = sessionStorage.getItem('cart');
var cartobject = JSON.parse(cartValue);
console.log(cartobject);*/
console.log("cart")

/*
(function( $ ) {
    $.Shop = function( element ) {
@ -45,3 +50,96 @@ $(function() {
});
*/


/*console.log('working')

if(localStorage.getItem('cart' == null)){
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}

$('.cart').click(function () {
    console.log('clickedbtn');
    console.log(this.id + "þetta er id")
    var idstr = this.id.toString();
    console.log(idstr + "þetta er string id");
    if (cart[idstr] != undefined) {
        cart[idstr] = cart[idstr] + 1;
    }
    else {
        cart[idstr] = 1
    }
    console.log(cart);
    localStorage.setItem('cart', JSON.stringify(cart));
});
*/
/*
$('#save').on('click', function(){

    $('input[type="text"]').each(function(){
        var id = $(this).attr('id');
        var value = $(this).val();
       localStorage.setItem(id, value);

    });
});

$('#load').on('click', function(){
    $('input[type="text"]').each(function(){
        var id = $(this).attr('id');
        var value = localStorage.getItem(id);

        $(this).val(value);

    });
});

window.load=doShowAll();

function CheckBrowser() {
    if ('localStorage' in window && window['localStorage'] !== null) {
        // We can use localStorage object to store data.
        return true;
    } else {
            return false;
    }
}

function doShowAll() {
    if (CheckBrowser()) {
        var key = "";
        var list = "<tr><th>Item</th><th>Value</th></tr>\n";
        var i = 0;
        //For a more advanced feature, you can set a cap on max items in the cart.
        for (i = 0; i <= localStorage.length-1; i++) {
            key = localStorage.key(i);
            list += "<tr><td>" + key + "</td>\n<td>"
                    + localStorage.getItem(key) + "</td></tr>\n";
        }
        //If no item exists in the cart.
        if (list == "<tr><th>Item</th><th>Value</th></tr>\n") {
            list += "<tr><td><i>empty</i></td>\n<td><i>empty</i></td></tr>\n";
        }
        //Bind the data to HTML table.
        //You can use jQuery, too.
        document.getElementById('list').innerHTML = list;
    } else {
        alert('Cannot save shopping list as your browser does not support HTML 5');
    }
}

function SaveItem() {

    var name = document.forms.ShoppingList.name.value;
    var data = document.forms.ShoppingList.data.value;
    localStorage.setItem(name, data);
    doShowAll();

}
function RemoveItem()
{
var name=document.forms.ShoppingList.name.value;
document.forms.ShoppingList.data.value=localStorage.removeItem(name);
doShowAll();
} */

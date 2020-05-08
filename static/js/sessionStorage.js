/*sessionStorage.setItem('debug', "20");
var total = sessionStorage.getItem('debug');
console.log(total);

var total = parseInt( sessionStorage.getItem('debug'));
var quantity = 2;
var updatedTotal = total * quantity;
sessionStorage.setItem('total', updatedTotal);
console.log("this is updated total" + sessionStorage.getItem('total'));

var cart = {
    item: "Zelda",
    price: 9.99,
    qty: 2
};
var jsonStr = JSON.stringify(cart);
sessionStorage.setItem('cart', jsonStr);
console.log(sessionStorage.getItem('cart'));
var cartValue = sessionStorage.getItem('cart');
var cartobject = JSON.parse(cartValue);
console.log(cartobject);*/

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



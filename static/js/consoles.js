/* NOT ready, en komið langa leið runnar ekki, */
console.log("ég er hér")
$(document).ready(function() {
        $('#searchBtn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#searchBox').val();
        $.ajax( url: {
            url:'/consoles?searchFilter=' + searchText,
            type: 'GET',
            success: function(resp){
            var newHtml = resp.data.map(d => {
                return '<div class="container">\n' +
                    '        <section class = "catalog-views">\n' +
                    '            <div class="row">\n' +
                    '                <a href="/consoles/{{ console.id }}">\n' +
                    '                <div class= "catalog-view">\n' +
                    '                    <div class = "catalog-item-img">\n' +
                    '                        <img src="{{ console.consoleimage_set.first.image }}" />\n' +
                    '                    </div>\n' +
                    '                </div>\n' +
                    '                </a>\n' +
                    '            </div>\n' +
                    '\n' +
                    '                <div class="catalog-item-title">\n' +
                    '                        {{ console.name }}\n' +
                    '                    </div>\n' +
                    '\n' +
                    '                <!-- buttons hjá hverju item view síðu-->\n' +
                    '                <div class= "catalog-cta">\n' +
                    '                    <div class = "catalog-item-price">\n' +
                    '                        {{ console.price }} $\n' +
                    '\n' +
                    '                <!--    <button class = "catalog-cta-select">select</button>-->\n' +
                    '                <!--    <button class = "catalog-cta-add">add to cart</button>\n' +
                    '                Commenta þetta út því ég aðeins að breyta til\n' +
                    '                að testa cart og sjá hvort ég geti addað to cart-->\n' +
                    '                        <form class="" action="cart" method="post">{% csrf_token %}\n' +
                    '                            <p><input type="submit" value="Add To cart" class="catalog-cta-add"></p>\n' +
                    '                        </form>\n' +
                    '                        </div>\n' +
                    '                </div>\n' +
                    '\n' +
                    '        </section>\n' +
                    ' </div>'

            });
            $('consoles').html(newHtml.join(''));
            $('searchBox').val('');
            },
            error: function(xhr, status, error) {
            console.log(error)
            }
        })
        })
})
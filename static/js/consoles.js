/* NOT ready, en komið langa leið runnar ekki, smá villa */
console.log("ég er hér123")
$(document).ready(function () {
    $('#searchBtn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#searchBox').val();
        $.ajax( {
            url:'/consoles?searchFilter=' + searchText,
            type: 'GET',
            success: function (resp) {
                console.log(resp.data)
                var newHtml = resp.data.map(d => {
                    return `<div class ="catalog-views">
                                <a href="/consoles/${ d.id }">
                                    <img class="catalog-item-img" src="${ d.firstImage }" />
                                    <h3> ${ d.name } </h3>
                                    <h4> ${ d.price } $ </h4>
                                </a>
                                <form class="" action="cart" method="post">
                                    <p><input type="submit" value="add to cart" class="catalog-cta-add"></p>
                                </form>
                            </div>`
                });
                $('.catalog-views').html(newHtml.join(""));
                $('#searchBox').val('')
            },
            error: function(xhr, status, error) {
                console.log(error)
            }
        })
    })
})
/*
function saveText() {
    console.log("saved to localStorage")
    var e = document.getElementById("searchBox");
    if(typeof(Storage) !== 'undefined') {
        var currentValue = localStorage.getItem('searchField');
        if (currentValue.length == 0) {
            currentValue = e.value;
        } else {
            currentValue = currentValue + '\n' + e.value;
        }
        localStorage.setItem('searchField', currentValue);
        alert('current value:\n\n' + localStorage.getItem('searchField'));
    } else {
        alert('Cannot access local storage.');
    }
} */

                            /*<div  class="console">
                                <a href="http://127.0.0.1:8000/consoles/${d.id}">
                                <img class="consoleImage" src="${d.firstImage}">
                                <h4>${d.name}</h4>
                                <p>${d.price}</p>
                                </a>
                            </div>*/


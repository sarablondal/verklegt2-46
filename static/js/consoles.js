/* NOT ready, en komið langa leið runnar ekki, smá villa að það birtist fleiri en eitt instance af hverri vöru*/
$(document).ready(function () {
    //listens for click on search button
    $('#searchBtn').on('click', function (e) {
        e.preventDefault();
        //retrieve user input
        var searchText = $('#searchBox').val();
        $.ajax( {
            url:'/consoles?searchFilter=' + searchText,
            type: 'GET',
            success: function (resp) {
                console.log(resp.data)
                //loop throught response data from server
                var newHtml = resp.data.map(d => {
                    console.log(d)
                    return `<div class ="catalog-views">
                                <a href="/consoles/${ d.id }">
                                    <img class="catalog-item-img" src="${ d.firstImage }" />
                                    <h3> ${ d.name } </h3>
                                    <h4> ${ d.price } $ </h4>
                                </a>
                                <form class="" action="cart" method="post">
                                    <button data-product="{{console.id}}" data-action="add" class="btn btn-outline-secondary add-btn update-cart">Add to Cart</button>
                                    <a class="btn btn-outline-success" href="${ d.id }">View</a>
                                </form>
                            </div>`
                });
                //display new data according to userinput
                $('.product').html(newHtml.join(""));
                $('#searchBox').val('')
            },
            error: function(xhr, status, error) {
                console.log(error)
            }
        })
    })
})



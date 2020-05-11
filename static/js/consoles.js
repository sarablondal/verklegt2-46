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
                    return `<div  class="console">
                                <a href="consoles/${d.id}">
                                <img class="consoleImage" src="${d.firstImage}">
                                <h4>${d.name}</h4>
                                <p>${d.price}</p>
                                </a>
                            </div>`

                });
                $('.container').html(newHtml.join(''));
                $('#searchBox').val('')
            },
            error: function(xhr, status, error) {
                console.log(error)
            }
        })
    })
})


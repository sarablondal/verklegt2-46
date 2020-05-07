/* NOT ready, en komið langa leið runnar ekki, */
$(document).ready(function(){
    $('#searchBtn').on(types: 'click', selector: fucntion(e){
        e.preventDefault();
        var searchText = $('searchBox').val();
        $.ajax( url: {
            url: '/consoles?searchFilter=' + searchText,
                type: 'GET',
                success: function(resp) {
                var newHtml = resp.data.map( d => {
                    return '<div class="">
                        <ahref="/consoles/${d.id}">
                            <img class="console" src="${d.firstImage}"/>
                                    <h4>${d.name}</h4>
                                    <p>${d.description}<p>
                                    <p>${d.company}<p>
                                    <p>${d.pice}<p>
                                </a>
                            </div>'
                });
                $('consoles').html(newHtml.join(''));
                $('#serachBox').val(value: '');
            },
            error: function(xhr, status, error) {
                /* fix this and handle error */
                console.log(error)
            }
        })
    });
});
console.log('filter working');
$(document).ready(function() {
    $('.cBox').on('click', function () {
      $('.cBox').not(this).prop('checked', false);
    });
});

$(document).ready(function () {
    $('.cBox').on('click', function(e) {
      var categorySelected = $('input:checked').val();
      console.log(categorySelected)
      $.ajax({
        url:'/consoles?categoryFilter=' + categorySelected,
        type: 'GET',
        success: function(resp) {
          console.log(resp.data)
          var newHtml = resp.data.map(d => {
            return `<div class ="catalog-views">
                        <a href="/consoles/${d.id}">
                            <img class="catalog-item-img" src="${d.firstImage}" />
                            <h3> ${d.name} </h3>
                            <h4> ${d.price} $ </h4>
                        </a>
                        <!-- <form class="" action="cart" method="post"> -->
                            <p><input type="submit" value="add to cart" class="catalog-cta-add"></p>
                            <a class="btn btn-outline-success" href="${ d.id }}">View</a>
                        <!-- </form> -->
                    </div>`
          });
          $('.product').html(newHtml.join(''));
        },
        error: function(xhr, status, error) {
            console.log(error)
        }
      })
    })
})
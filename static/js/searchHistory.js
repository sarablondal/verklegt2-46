
$(document).ready(function(){
    $('#searchBtn').on('click', function (e) {
        e.preventDefault()
        var searchValue = $('#searchBox').val()
        if (localStorage.getItem('searchHistory') == null){
            /* ef localStorage fyrir searchHistory er ekki til þá búa það til og pusha searchvalue frá user í localstorage */
            var searchList = []
            searchList.push(searchValue.toLowerCase())
            /*var jsonString = searchVal.JSON.stringify(searchList)*/
            localStorage.setItem('searchHistory', JSON.stringify(searchList))
        } else {
            var jsonString = localStorage.getItem('searchHistory')
            var searchList = JSON.parse(jsonString)
            /* check for duplicates */
            if(!(searchList.includes(searchValue.toLowerCase()))){
                searchList.push(searchValue.toLowerCase())
            }
            localStorage.setItem('searchHistory', JSON.stringify(searchList))
        }
    });
});


$('#searchBox').on('click', function (e) {
    e.preventDefault()
    if(localStorage.getItem('searchHistory') != null) {
        var history = ''
        var localStorageStrList = localStorage.getItem('searchHistory')

        var localStorageList = JSON.parse(localStorageStrList)
        for(let i=0; i<localStorageList.length; i++){
            history += '<option>' + localStorageList[i] + '</option>'
        };
        document.getElementById('history').innerHTML = history
    }
})





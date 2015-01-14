// selects all rows, dont work with the first + last two rows. so
var elems = document.querySelectorAll('#tabled #tabledbody tr')
  , sortb = document.querySelectorAll('#tabled thead th')

sortb.forEach(function(item) {
  item.onclick = function() {
    console.log(item.innerHTML)
  }
})

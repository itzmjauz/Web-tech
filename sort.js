 
// selects all rows, dont work with the first + last two rows. so
var elems = document.querySelectorAll('#tabled #tabledbody tr')
var sortb = document.querySelectorAll('#tabled thead th')


  // className assignment for readability 
sortb[0].className = "sort0"
sortb[1].className = "sort1"
sortb[2].className = "sort2"
sortb[3].className = "sort3"
sortb[4].className = "sort4"

// assign onclick events
for (var ind = 0; ind < 5 ; ind++) {
  sortb[ind].onclick = function() {
    var oldName = this.className
    reset()
    if(oldName == "sortUp") {
      this.className = "sortDown"
      sortDown(ind)
    }
    else{
      this.className = "sortUp"
      sortUp(ind)
    }
    // sort etc, flip table indexes. 
  }
}

function reset(index) {
  I = [0, 1, 2, 3, 4]

  I.forEach(function(ind) {
    sortb[ind].className = "sort" + ind
  })
}

function sort(){
  var a = document.querySelector('#tabled .sortUp')
    , b = document.querySelector('#tabled .sortDown')

  if(a) sortUp(a)
  if(b) sortDown(b)
}

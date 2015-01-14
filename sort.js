// selects all rows, dont work with the first + last two rows. so
var elems = document.querySelectorAll('#tabled #tabledbody tr')
  , sortb = document.querySelectorAll('#tabled thead th')


// className assignment for readability 
sortb[0].className = "sort1"
sortb[1].className = "sort2"
sortb[2].className = "sort3"
sortb[3].className = "sort4"
sortb[4].className = "sort5"

// assign onclick events

sortb[0].onclick = function(){
  if(this.className == "sort1"){
    this.className = "sortUp"
    reset(0)
    // sort etc, flip table indexes. 
  }
}

function reset(index){
  
}

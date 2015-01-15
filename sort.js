 // selects all rows, dont work with the first + last two rows. so
 var sortb = document.querySelectorAll('#tabled thead th')


 // className assignment for readability 
 sortb[0].className = "sort0"
 sortb[1].className = "sort1"
 sortb[2].className = "sort2"
 sortb[3].className = "sort3"
 sortb[4].className = "sort4"

 // assign onclick events
 for (var ind = 0; ind < 5; ind++) {
   sortb[ind].onclick = function() {
     var oldName = this.className
     reset()
     if (oldName == "sortUp") {
       this.className = "sortDown"
     }
     else {
       this.className = "sortUp"
     }
     sort()
     // sort etc, flip table indexes. 
   }
 }

 function reset(index) {
   I = [0, 1, 2, 3, 4]

   I.forEach(function(ind) {
     sortb[ind].className = "sort" + ind
   })
 }

 function sort() {
   var a = document.querySelector('#tabled .sortUp')
   var b = document.querySelector('#tabled .sortDown')
   var table = getTable()
   var index = getIndex()
   if (a) {
     table.sort(function(x, y) {
       return x[index] > y[index]
     })
   }
   if (b) {
     table.sort(function(x, y) {
       return x[index] < y[index]
     })
   }
   write(table)
 }

 function getTable() {
   var elems = document.querySelectorAll('#tabled #tabledbody tr')
   var table = []
   for (var x = 0; x < elems.length; x++) {
     table[x] = []
     for (var y = 0; y < elems[x].querySelectorAll('td').length; y++) {
       table[x][y] = elems[x].querySelectorAll('td')[y].innerHTML
     }
   }
   return table
 }

 function getIndex() {
   var headers = document.querySelectorAll('#tabled thead th')
   var index = 0
   while (index < 5) {
     if (headers[index].className == "sortUp" || headers[index].className == "sortDown") {
       break
     }
     index++
   }
   return index
 }

function write(table){
  console.log(table)
}
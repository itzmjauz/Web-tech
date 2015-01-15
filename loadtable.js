link = "http://wt.ops.few.vu.nl/api/89000f2e/"

$.getJSON(link, function(data) {
  insert(data)
})

function insert(data) {
  var table = document.getElementById("tabledbody")
  for (var x = 0; x < data.length; x++) {
    var row = table.insertRow(table.rows.length)
    row.insertCell(0).innerHTML = data[x].name
    row.insertCell(1).innerHTML = data[x].category
    row.insertCell(2).innerHTML = data[x].amount
    row.insertCell(3).innerHTML = data[x].date
    row.insertCell(4).innerHTML = data[x].location
  }
}

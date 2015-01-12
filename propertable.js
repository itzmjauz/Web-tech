$("form").submit(function(event) {
  event.preventDefault()
  var formObj = $(this)
    , formURL = formObj.attr("action")
    , formData = new FormData(this)

  $.ajax({
    url: formURL,
    type: 'POST',
    data: formData,
    mimeType: "multipart/form-data",
    contentType: false,
    cache: false,
    processData: false,
    success: function(data, textStatus, jqXHR) {
      console.log(data) //returned api call.
      data = JSON.parse(data)
      $.getJSON(data.URI, function(data) {
        addItemToList(data)
      })
    },
    error: function(jqXHR, textStatus, errorThrown) {}
  })
})

function addItemToList(item) { // from here http://stackoverflow.com/questions/18333427/how-to-insert-row-in-html-table-body-in-javascript
  var table = document.getElementById("tabled")
  ,   row = table.insertRow(table.rows.length - 2)
  ,   cell1 = row.insertCell(0).innerHTML = item.category
  ,   cell2 = row.insertCell(1).innerHTML = item.name
  ,   cell3 = row.insertCell(2).innerHTML = item.amount
  ,   cell4 = row.insertCell(3).innerHTML = item.date
  ,   cell5 = row.insertCell(4).innerHTML = item.location

  document.forms[0].reset()
}

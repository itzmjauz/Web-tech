//semicolons are for pussies

$("form").submit(function(event) {
  event.preventDefault()
  var formObj = $(this)
  var formURL = formObj.attr("action")
  var formData = new FormData(this)

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

function addItemToList(item) { // for flipped tables
  var table = document.getElementById("tabled")
    , elems = document.querySelectorAll('#tabled tr')
    , length = document.querySelectorAll('#tabled tr')[1].querySelectorAll('td').length
    // set the properties in the list
  elems[0].insertCell(length - 1).innerHTML = item.category
  elems[1].insertCell(length - 1).innerHTML = item.name
  elems[2].insertCell(length - 1).innerHTML = item.amount
  elems[3].insertCell(length - 1).innerHTML = item.location
  elems[4].insertCell(length - 1).innerHTML = item.date

  document.querySelectorAll('#tabled tr th')[5].colSpan += 1
  document.forms[0].reset()
}

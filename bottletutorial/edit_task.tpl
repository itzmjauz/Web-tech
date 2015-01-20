%#template for editing a task %#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<p>Edit the task with ID = {{no}}</p>

<form action="/edit/{{no}}" method="GET">
  <table id="tabled" class="sortable">
    <caption>Inventory table</caption>
    <thead>
      <tr>
        <th>Name</th>
        <th>Category</th>
        <th>Amount</th>
        <th>Puchase Date</th>
        <th>Location</th>
      </tr>
    </thead>
    <tbody id="tabledbody">
    </tbody>
    <tr>
      <td>
        <input type="text" name="name" required>
      </td>
      <td>
        <input type="text" name="category" required>
      </td>
      <td>
        <input type="number" name="amount" required>
      </td>
      <td>
        <input type="date" name="date" id="datepicker" required>
      </td>
      <td>
        <input type="text" name="location" required>
      </td>
    </tr>
    <tr>
      <th colspan="5">
        <input type="submit" value="Submit" name="save">
      </th>
    </tr>
  </table>
</form>
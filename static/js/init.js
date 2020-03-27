(function($) {
  $(function() {
    $(".sidenav").sidenav();
  }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function() {
  $(".modal").modal();

  $(".modal-trigger.update").click(function() {
    const $row = $(this).closest("tr"); // Finds the closest row <tr>

    const form = document.getElementById("update_form");
    form.action += $row.data("id");
    const name = document.getElementById("update_name");
    name.value = $row.find("td:nth-child(1)").text();
    const description = document.getElementById("update_description");
    description.innerText = $row.find("td:nth-child(2)").text();
  });
});

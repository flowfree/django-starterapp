$(document).ready(function() {

  // Signout link
  $('#signout').click(function(e) {
    e.preventDefault();
    $('#form-signout').submit();
  });

  // Auto close alert messages
  $(".alert:not(.admin-warning)").delay(5000).slideUp(200, function() {
    $(this).alert('close');
  });
  
});
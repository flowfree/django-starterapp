$(document).ready(function() {

  // Signout link
  $('#signout').click(function(e) {
    e.preventDefault();
    $('#form-signout').submit();
  });

});
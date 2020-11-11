$(document).ready(function() {
	$('form').on('submit', function(event) {
	  $.ajax({
		 data : {
			textnum : $('#textid').val(),
				},
			type : 'POST',
			url : '/num'
		   })
	   .done(function(data) {
		alert(data);
	 });
	 event.preventDefault();
	 });
});
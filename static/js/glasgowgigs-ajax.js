$(document).ready(function() {

	$('#likes').click(function(){
		var venue;
		venue = $(this).attr("data-venue"); 
		$.get('/glasgowgigs/like_venue/', {venue_id: venueid}, function(data){ 
			$('#like_count').html(data); 
			$('#likes').hide(); 
		}); 
	});

});

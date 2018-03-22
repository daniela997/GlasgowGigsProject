$('#likes').click(function(){
	var venueid;
	venueid = $(this).attr("data-venueid"); 
	$.get('/glasgowgigs/like_venue/', {venue_id: venueid}, function(data){ 
		$('#like_count').html(data); 
		$('#likes').hide(); 
	}); 
});

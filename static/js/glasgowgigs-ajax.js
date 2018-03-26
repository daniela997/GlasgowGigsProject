$('#likes-venue').click(function(){
	var venueid;
	venueid = $(this).attr("data-venueid"); 
	$.get('/glasgowgigs/like_venue/', {venue_id: venueid}, function(data){ 
		$('#like_count_venue').html(data); 
		$('#likes-venue').hide(); 
	}); 
});

$('#likes-artist').click(function(){
	var artistid;
	artistid = $(this).attr("data-artistid"); 
	$.get('/glasgowgigs/like_artist/', {artist_id: artistid}, function(data){ 
		$('#like_count_artist').html(data); 
		$('#likes-artist').hide(); 
	}); 
});

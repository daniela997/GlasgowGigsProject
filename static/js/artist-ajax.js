$('#likes').click(function(){
	var artistid;
	artistid = $(this).attr("data-artistid"); 
	$.get('/glasgowgigs/like_artist/', {artist_id: artistid}, function(data){ 
		$('#like_count').html(data);
		$('#likes').hide(); 

	}); 
});

$('#book-event').click(function(){
	var eventid;
	eventid = $(this).attr("data-eventid"); 
	$.get('/glasgowgigs/book_event/', {event_id: eventid}, function(data){ 
		$('#book-event').html("Booked!"); 
    }); 
});


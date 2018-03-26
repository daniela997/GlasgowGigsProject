$(document).ready(function(){
    // Activate carousel
    $("#ArtistCarousel").carousel();
    
    // Enable carousel control
	$(".left").click(function(){
    	$("#ArtistCarousel").carousel('prev');
    });
    $(".right").click(function(){
    	$("#ArtistCarousel").carousel('next');
    });
});

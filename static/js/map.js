function initMap() {
	var location = {lat: {{venue.latitude}}, lng: {{venue.longitude}} };
	var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 15,
		center: location
    });
    var marker = new google.maps.Marker({
       position: location,
       map: map
    });
}

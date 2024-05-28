import json

def location(v_markers_html, c_markers_html, API_KEY):
    html= \
"""
<!DOCTYPE html>
<html>
  <head> 
    <meta charset="UTF-8">
	<meta name="viewport" content="initial-scale=1.0">
    <title>Maps JavaScript API</title>
	<style> 
  	  #map {
        height: 100%;
      }
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
	</style> 
</head>  
	<body>
		<div id ="map"> </div> 
	<script src="https://maps.googleapis.com/maps/api/js?key="""+API_KEY+"""&callback=initMap" async defer></script>
	<script>
      var map;
  	 function initMap() {
  	 var map = new google.maps.Map(document.getElementById('map'), {
		  center:{lat:42.8052452, lng:-1.6493937},
          zoom: 13,
        });
        """+v_markers_html+"""
        """+c_markers_html+"""
      }
	</script>
	</body>
</html>
"""
    return html

def write_v_markers_html(coordinatesList, names):
    v_html = ''
    for i, coordinates in enumerate(coordinatesList):
        v_html = v_html + """var marker"""+str(i)+""" = new google.maps.Marker({
        position: {lat: """+str(coordinates[0])+""", lng: """+str(coordinates[1])+"""},
        map: map,
        icon: {
      url: 'http://maps.google.com/mapfiles/ms/micons/blue.png'
    },
        draggable: false,
        title: 'Voluntario, """+names[i]+"""'});"""
    return v_html

def write_c_markers_html(coordinatesList, names, states):
    c_html = ''
    for i, coordinates in enumerate(coordinatesList):
        if 'Espera' in states[i]:
            icon = 'http://maps.google.com/mapfiles/kml/pal3/icon37.png'
        else:
            icon = 'http://maps.google.com/mapfiles/kml/pal3/icon38.png'
        c_html = c_html + r"""var marker"""+str(i)+""" = new google.maps.Marker({
        position: {lat: """+str(coordinates[0])+""", lng: """+str(coordinates[1])+"""},
        map: map,
        icon: {
      url: '"""+icon+"""'
    },
        draggable: false,
        title: 'Ayuda, """+names[i]+""", """+states[i]+"""'});"""
    return c_html

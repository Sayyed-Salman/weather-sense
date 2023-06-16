document.addEventListener('DOMContentLoaded', function() {
            var getLocationBtn = document.getElementById('getLocationBtn');
            getLocationBtn.addEventListener('click', function() {
                // Ask for user's location
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(function(position) {
                        // Retrieve latitude and longitude
                        var latitude = position.coords.latitude;
                        var longitude = position.coords.longitude;

                        // Send location to Flask server
                        var xhr = new XMLHttpRequest();

                        xhr.open('POST', '/location');
                        xhr.setRequestHeader('Content-Type', 'application/json');
                        xhr.onload = function() {
                            if (xhr.status === 200) {
                                console.log('Location sent successfully');
                            } else {
                                console.error('Error sending location:', xhr.statusText);
                            }
                        };
                        xhr.onerror = function() {
                            console.error('Request failed');
                        };
                        xhr.send(JSON.stringify({ 'latitude': latitude, 'longitude': longitude }));

                        window.location.href = `/weather/${latitude},${longitude}`;
                        
                    }, function(error) {
                        console.error('Error getting location:', error);
                    });
                } else {
                    console.error('Geolocation is not supported by this browser.');
                }
            });
        });
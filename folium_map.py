import folium
from folium.features import LatLngPopup

m = folium.Map(
    location=[48.7, 2.3],
    zoom_start=9,
)
LatLngPopup().add_to(m)
m.save("templates/index.html")
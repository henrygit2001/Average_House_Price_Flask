from pickle import TRUE
from flask import *
from flask_ngrok import run_with_ngrok
import folium
import requests
import googlemaps
import streamlit as st
from streamlit_folium import st_folium
from folium.plugins import MousePosition
from bs4 import BeautifulSoup
from geopy.geocoders import ArcGIS
import requests
import jyserver.Flask as jsf
###from selenium import webdriver
####from selenium.webdriver.common.by import By
###Code from  https://stackoverflow.com/questions/63413571/returning-latitude-longitude-values-from-folium-map-on-mouse-click-to-python-sc
##from streamlit_folium import st_folium
##import streamlit as st

##map = st_folium(m, height=350, width=700)
##map['last_clicked']['lat']
##map['last_clicked']['lng']
#######

###https://gis.stackexchange.com/questions/371628/get-coordinates-from-foliums-feature-latlngpopup-in-python
##import folium
##from folium.plugins import MousePosition


##m = folium.Map()

##MousePosition().add_to(m)

##m
####

app = Flask(__name__)
##run_with_ngrok(app)
@jsf.use(app)
class App:
    @jsf.task
    def main(self):
        starting_location = (35.8432, -100.0752)
        world_map = folium.Map(
        location=starting_location, 
        zoom_start = 5.0,
        min_zoom = 5.0
    )
        world_map.add_child(folium.LatLngPopup()) 
        world_map.add_child(folium.ClickForMarker())
        map = st_folium(world_map, height=350, width=700)
        formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        MousePosition().add_to(world_map)
        #nom = ArcGIS()
        #s = nom.geocode('seattle')
        #print(s.latitude)
        folium.Circle(
            radius=100,
            location=[45.5244, -122.6699],
            popup="The Waterfront",
            color="#3186cc",
            fill=True,
            fill_color="#3186cc",
        ).add_to(world_map)
        ## Open Up the Map in Index.html
        self.js.document.getElementById("map").innerHTML = world_map._repr_html_()
        ## Stuck...Trying to get the Longitude and Latitude after clicking randomly on the Map
        ##When inspecting the element of the popup box, the class that the Longitude and Latitude lies inside is called "leaflet-popup-content"
        popup = self.js.document.getElementsByClassName("leaflet-control-mouseposition leaflet-control").innerHTML
        print(popup)

@app.route("/")
def index():
    App.main()
    return App.render(render_template("index.html"))

    

    

if __name__ == "__main__":
    app.run(debug=TRUE)


                

#URL: https://5e51-2601-601-480-e510-2d58-f0f9-7c95-51cb.ngrok.io/



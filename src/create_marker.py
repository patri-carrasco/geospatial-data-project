
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd

def create_marker(gdf,name_map):
    for i,row in gdf.iterrows():
    #popup distrito
        distrito = {
            "location" : [row["latitud"], row["longitud"]],
            "tooltip" : row["name"]
        }
        icon = Icon( color = "blue",
                        prefix = "fa",
                        icon = "coffee",
                        icon_color = "black"
            )
        Marker (**distrito,icon = icon).add_to(name_map)


def create_marker_school(gdf,name_map):
    for i,row in gdf.iterrows():
    #popup distrito
        distrito = {
            "location" : [row["latitud"], row["longitud"]],
            "tooltip" : row["name"]
        }
        icon = Icon( color = "blue",
                        prefix = "fa",
                        icon = "graduation-cap",
                        icon_color = "black"
            )
        Marker (**distrito,icon = icon).add_to(name_map)


def create_marker_metro(gdf,name_map):
    for i,row in gdf.iterrows():
    #popup distrito
        distrito = {
            "location" : [row["latitud"], row["longitud"]],
            "tooltip" : row["name"]
        }
        icon = Icon( color = "blue",
                        prefix = "fa",
                        icon = "subway",
                        icon_color = "black"
            )
        Marker (**distrito,icon = icon).add_to(name_map)

         
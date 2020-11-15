
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
                        icon = "cutlery",
                        icon_color = "black"
            )
        Marker (**distrito,icon = icon).add_to(name_map)
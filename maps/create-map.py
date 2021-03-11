# Libraries
import folium
import pandas
from urllib.parse import quote

# Functions
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# Main Body
print("start program")
# Create map object w/ start zone and zoom level... 
map = folium.Map(location=[44.4280, -110.5885], zoom_start=9, tiles="Stamen Terrain")
#map = folium.Map(location=[44.4280, -110.5885], zoom_start=9)

# Open volcano information csv file
voldata = pandas.read_csv("resources/Volcanoes.txt")
lat = list(voldata["LAT"])
lon = list(voldata["LON"])
elev = list(voldata["ELEV"])
name = list(voldata["NAME"])
voltype = list(voldata["TYPE"])
loc = list(voldata["LOCATION"])

# Add "Volcano" FeatureGroup
print("Creating Volcano feature group")
volfg = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el, nm, typ, lc in zip(lat, lon, elev, name, voltype, loc):
    # Determine Color based on height
    fgcolor = color_producer(el)
    # Create Popup
    html = f"""<h4>{str(nm)} Info:</h4>
    <p>Elevation: {str(el)} m</p>
    <p>Volcano Type: <a href=\"https://www.google.com/search?q={str(quote(typ))}\" target=\"_blank\">{str(typ)}</a></p>
    <p>Location: {str(lc)}</p>
    <br/>
    <p><a href=\"https://www.google.com/search?q={str(quote(nm))}\" target=\"_blank\">More info on {str(nm)} here.</a></p>
    """
    iframe = folium.IFrame(html = html, width = 250 , height = 300)
    volfg.add_child(folium.CircleMarker(location = [lt, ln], popup = folium.Popup(iframe), radius = 10, 
                                    fill_color = color_producer(el), color = 'grey', fill = True, fill_opacity = 0.7)) # color = outer rim ; fill (force)

# Open national park csv file
print("Creating National Parks feature group")
parkdata = pandas.read_csv("resources/nationPark.csv")
""" print("=============================")
print(parkdata)
print("=============================") """
lat = list(parkdata["LAT"])
lon = list(parkdata["LON"])
name = list(parkdata["NAME"])
loc = list(parkdata["LOCATION"])

parkfg = folium.FeatureGroup(name="National Parks")
for lt, ln, nm, lc in zip(lat, lon, name, loc):
    # Create Popup
    html = f"""<h4>{str(nm)} Info:</h4>
    <br/>
    <p><a href=\"https://www.google.com/search?q={str(quote(nm + " national park"))}\" target=\"_blank\">More info on {str(nm)} national park here.</a></p>
    """
    iframe = folium.IFrame(html = html, width = 250 , height = 300)
    parkfg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='blue')))

popfg = folium.FeatureGroup(name="Population")
print("Creating Populations feature group")
popfg.add_child(folium.GeoJson(data=open('resources/world.json', 'r', encoding = 'utf-8-sig').read(),
                                        style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Add Feature group to map layer
map.add_child(popfg)
map.add_child(volfg)
map.add_child(parkfg)
map.add_child(folium.LayerControl())

# Create HTML document
print("saving map...")
map.save("Map1.html")
print("end program.")
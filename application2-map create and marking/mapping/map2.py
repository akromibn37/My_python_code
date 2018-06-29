import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(el):
	if el<1000:
		return 'green'
	elif el<3000:
		return 'orange'
	else:
		return 'red'
	
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="Volcanoes")

for lt,ln,el,na in zip(lat,lon,elev,name):	
	fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=8,color=color_producer(el), fill_color=color_producer(el), popup=na+" "+str(el)+' m'))
	#fg.add_child(folium.Marker(location=[37.2,-97.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

fgp=folium.FeatureGroup(name="Population")	
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")

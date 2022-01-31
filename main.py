import folium

fmap = folium.Map(location=["emplacement en int"], tiles="OpenStreetMap", zoom_start=14)

folium.Marker(["emplacement en int"],
              popup="Emplacement",
              icon=folium.Icon(color='green')).add_to(fmap)

fmap.save('cartes_MLJ.html')

# Maps and geospatial data


## [Folium](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@884a7a2954a84eda9d6f39bca49bf02a/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@92bebb5f52db431cb52c2c1df8cedcb7)
-----
Library to create several types of Leaflet maps. It enables both the binding of data to a map for choropleth visualizations as well as passing visualizations as markers on the map.  
Create a world map:
```
import folium

world_map = folium.Map()
```

Create a map of Canada:
```
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
```
Different styles can be settled by different 'tiles' parameter ('Stamen Toner', 'Stamen Terrain')


## [Maps with Markers](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@632e42a851a04330b3bd6fcb451af2f3/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@1e0d72b637424365b50fc82948922e86)
-------
Create feature group:
```
ontario = folium.map.FeatureGroup()
```

Style the feature group and add it to the feature group:
```
ontario.add_child(
    folium.features.CircleMarker([51.25, -85.32], radius=5, color='red', fill_color="red")
)
```
Add it to the map:
```
canada_map.add_child(ontario)
```
Label the marker:
```
folium.Marker([51.25, 85.32], popup='Ontario'.add_to(canada_map))
```


## [Choropleth Maps](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@e2f0c4666ac7439185f2ef5e35877f4d/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@de805075a5ba400d8233463a7e85cccf)
----
A thematical map in which areas are shaded in proportion to the measurement of the statistical variable being displayed in the map.  
To create a choropleth map Folium needs a Geo Json file that includes geospatial data.  
Create a choropleth map:
```
world_map = folium.Map(zoom_start=2, tiles='Mapbox Bright')

world_geo = r'world_countries_file.json'
world_map.choropleth(geo_path=world_geo, data=df_canada, columns=['Country', 'Total'], key_on='feature.properties.name', fill_color='y1OrRd', legend_name='Inmigration to Canada')
```

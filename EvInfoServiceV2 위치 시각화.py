import pandas as pd

EvInfoServiceV2_geoData = pd.read_csv('C:/Users/wkdtj/Desktop/기말 프로젝트/EvInfoServiceV2_geo.shp.csv', encoding='cp949',  engine='python')

import  folium
map_store = folium.Map(location=[37.61541164, 127.0135638], zoom_start = 12)

for i, store in EvInfoServiceV2_geoData.iterrows():   
    folium.Marker(location=[store['위도'], store['경도']], popup=store['store'], icon=folium.Icon(color='blue', icon='info-sign')).add_to(map_store)

map_store.save('C:/Users/wkdtj/Desktop/기말 프로젝트/map_store_1.html')

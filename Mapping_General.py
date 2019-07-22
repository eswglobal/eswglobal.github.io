# -*- coding: utf-8 -*-
"""
Created on Tue Oct  16 11:03:52 2018

@author: amjuli
"""

# =============================================================================
# = IMPORTS =
# ===========
import geopy, sys
import pandas as pd
from geopy.geocoders import Nominatim, GoogleV3
import folium

#inputfile=str(sys.argv[1])
inputfile = 'ESW_data.xlsx'
# namecolumn=str(sys.argv[2])

io = pd.read_excel(inputfile, sheet_name='Sheet1')
def get_latitude(x):
    return x.latitude

def get_longitude(x):
    return x.longitude
    
geolocator = Nominatim(user_agent="my-application",timeout=5)

  #geolocator = GoogleV3(timeout=5)
  # uncomment the geolocator you want to use
  # change the timeout value if you get a timeout error, for instance, geolocator = Nominatim(timeout=60)
io['helper'] = io['Chapter'].map(str)
geolocate_column = io['helper'].apply(geolocator.geocode)
io['latitude'] = geolocate_column.apply(get_latitude)
io['longitude'] = geolocate_column.apply(get_longitude)
#io.to_csv('geocoding-output-helper.csv')

#initalizing folium map object as m and using the geographic mean of the data points to center the viewpoint; basemap defaults to OSM
m = folium.Map(location=[io['latitude'].mean(), io['longitude'].mean()],tiles="OpenStreetMap", zoom_start=4)
for i in range(0,len(io)):
    folium.Marker([io.iloc[i]['latitude'], io.iloc[i]['longitude']],
                  popup=io.iloc[i]['Area_Name']).add_to(m)
# Save it as html
m.save('index.html')



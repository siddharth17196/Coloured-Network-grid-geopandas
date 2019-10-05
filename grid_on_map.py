import gmplot
import pickle
import googlemaps
import numpy as np
from geopy.distance import geodesic
import sqlite3
import datetime
import os
import matplotlib.pyplot as plt
import time
import folium
import math
from datetime import datetime, timedelta


 # bounding coordinates of Delhi
min_lat, min_lng = (28.404181, 76.83831)
max_lat, max_lng= (28.88382, 77.343689)

top_left = (max_lat, min_lng)
top_right = (max_lat, max_lng)
bot_left = (min_lat, min_lng)
bot_right = (min_lat, max_lng)

m = folium.Map(location=[28.628833, 77.206805], zoom_start=8)

n = 200             #200x200 grid
cols = np.linspace(min_lng, max_lng, num=n)
rows = np.linspace(min_lat, max_lat, num=n)

points = []
for i in range(n):
    points = []
    for j in range(n):
        points.append((rows[i],cols[j]))
    folium.PolyLine(points).add_to(m)    
for i in range(n):
    points = []
    for j in range(n):
        points.append((rows[j],cols[i]))
    folium.PolyLine(points).add_to(m)    
m.save('grid_on_map.html')

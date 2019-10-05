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

n = 200
cols = np.linspace(min_lng, max_lng, num=n)
rows = np.linspace(min_lat, max_lat, num=n)

grid = np.zeros((n,n))
bgrid = np.zeros((n,n))

#storing values for dates between July 1 to July 13
for single_date in (datetime.strptime('2019-07-01', '%Y-%M-%d') + timedelta(n) for n in range(14)):
    date = str(single_date.strftime('%Y-%M-%d'))
    print(date)    
    DB_PATH = 'C:/Users/Siddharth/Documents/july_19_corrected/july_19_corrected/'+date+'.db'        #database path
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM vehicle_feed"
    cur = conn.execute(query)
    c = np.zeros((n,n))
    bus = np.zeros((n,n), dtype=np.ndarray)
    for i in range(n):
        for j in range(n):
            bus[i][j] = []
    for q in cur:
        y = np.searchsorted(cols, float(q[2]))
        x = np.searchsorted(rows, float(q[1]))
        grid[x][y] += 1
        if q[0] not in bus[x][y]:
            bus[x][y].append(q[0])    
    c = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            bgrid[i][j] += len(bus[i][j])
            
cgrid = grid/bgrid                                       # total number points divide by number of buses in that area
cgrid = np.nan_to_num(cgrid)                    # converting nan to 0 (due to 0/0) 
f = open('weights200.pkl', 'wb')                 # saving grid values to a pickle file
pickle.dump(cgrid, f)
f.close()
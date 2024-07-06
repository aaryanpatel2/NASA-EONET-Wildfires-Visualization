import requests
import pandas
import sqlalchemy
import json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy

url="https://eonet.gsfc.nasa.gov/api/v2.1/categories/8?status=open"

JSO = requests.get(url)
data = json.loads(JSO.content)

x = numpy.array([])
y = numpy.array([])

for event in data["events"]:
    for geometry in event["geometries"]:
        coordinates = geometry["coordinates"]
        x = numpy.append(x, coordinates[0])
        y = numpy.append(y, coordinates[1])


font1 = {'family':'sans-serif','color': '#2b6c7b','size':20, 'weight':'bold'}
font2 = {'family':'sans-serif','color':'#2b6c7b','size':20, 'weight':'bold'}
font_title = {'family': 'sans-serif', 'color': '#3e97ab', 'size': 30, 'weight': 'bold'}


plt.style.use('dark_background')
plt.scatter(x, y, color='#88c999')
plt.xlabel("Longitude", fontdict=font1)
plt.ylabel("Latitude", fontdict=font2)
plt.title("Wildfire Locations", fontdict=font_title)
plt.show()
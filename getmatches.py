import http.client
import pandas as pd
import xml.etree.ElementTree as ET
import pickle
# can only get 1 match now
# match id - 6707f278-41fc-40d7-a5d0-051a3f51ee67
#saracens id - a4d33669-9e99-4626-a811-126bf8e7d52b

conn = http.client.HTTPSConnection("api.sportradar.us")
api_key = 'sdjugyse2z9krqcqzgcn48d2'
conn.request("GET", "/rugby-t1/matches/2fadc372-1bc2-4b13-af76-85997e0c389f/summary.xml?api_key={}".format(api_key))

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
print (type(data))

file = open('saracensmatch1.txt', 'wb')
pickle.dump(data, file)
file.close()
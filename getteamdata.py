import http.client
import pandas as pd
import xml.etree.ElementTree as ET
import pickle

#saracens id - a4d33669-9e99-4626-a811-126bf8e7d52b
conn = http.client.HTTPSConnection("api.sportradar.us")
api_key = 'sdjugyse2z9krqcqzgcn48d2'
conn.request("GET", "/rugby-t1/teams/a4d33669-9e99-4626-a811-126bf8e7d52b/profile.xml?api_key={}".format(api_key))

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
print (type(data))

file = open('teamdump.txt', 'wb')
pickle.dump(data, file)
file.close()
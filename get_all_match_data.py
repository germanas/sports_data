import pickle
import http.client
import pprint
import xml.etree.ElementTree as ET
match_list = open('matcheslist.txt', 'rb')
match_list = pickle.load(match_list)

#print (match_list)



query = []

for match_id in match_list:
    conn = http.client.HTTPSConnection("api.sportradar.us")
    api_key = 'sdjugyse2z9krqcqzgcn48d2'
    conn.request("GET", "/rugby-t1/matches/{}/summary.xml?api_key={}".format(match_id, api_key))
    res = conn.getresponse()
    data = res.read()
    #data.decode("utf-8")
    query.append(data)

print (len(query))
file = open('saracens_matches.xml', 'wb')
pickle.dump(query, file)
file.close()
import xml.etree.ElementTree as ET
import pickle
import pprint

tree = ET.parse('scheduledump.xml')
root = tree.getroot()
list = []
for root_elem in root:
    #print (root_elem.attrib['id'])
    #print (root_elem[3].attrib['id'])
    if root_elem[3].attrib['id'] == 'a4d33669-9e99-4626-a811-126bf8e7d52b':
        tag = root_elem.attrib['id']
        list.append(tag)
pprint.pprint(list)
file = open('matcheslist.txt', 'wb')
pickle.dump(list, file)
file.close()
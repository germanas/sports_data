import pickle

list = open('saracens_matches.xml', 'rb')
list = pickle.load(list)
print (len(list))
import pickle

file = open('dump.txt', 'rb')
data = pickle.load(file)
data = data.decode("utf-8")
print (data)

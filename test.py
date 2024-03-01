import pickle

with open('artifacts/proprocessor.pkl','rb') as file:
    obj = pickle.load(file)
    print(obj)
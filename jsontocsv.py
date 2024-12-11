import pandas as pd
import json
import os

data_name = []
data_to_csv = []
img = {}
dir = os.listdir("/Users/jaidynvankirk/Downloads/json 2/image")

dir.remove('.DS_Store')
dir.remove('extension')
dir.remove('android')
for file_name in dir:
    for file_name2 in os.listdir('image/' + file_name):
        preprocessed = (file_name2[0:len(file_name)+11])
        while preprocessed[-1].isdigit() == False:
            preprocessed = preprocessed[0:-1]
        data_to_csv.append(preprocessed)
        data_name.append(file_name)
        if img.__contains__(preprocessed):
            img[preprocessed] = img[preprocessed] +'|'+ file_name2
        else:
            img[preprocessed] = file_name2

cols = ['Application Name', 'Body', 'Image', 'Date Opened']
df = pd.DataFrame(columns = cols)


for i in range(len(data_to_csv)):
    try:
        with open(data_name[i]+'/'+data_to_csv[i]+'.json', 'r') as f:
            data = json.load(f) 
            lst_dict=({'Application Name':'Aegis','Body':data['body'], 'Image': img.get(data_to_csv[i]), 'Date Opened':data['created_at'][0:10]})
            df = df.append(lst_dict, ignore_index=True)
    except FileNotFoundError:
        print("File not found.")

df.to_csv("output.csv", index=False)
df.to_json("output.json")
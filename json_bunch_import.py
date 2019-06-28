# -*- coding: utf-8 -*-
# import all *.json files in (sub)folders and save into MongoDB

from pathlib import Path
import json

root_dir = "./json_folders"

#def parse_dir(root_dir):
path = Path(root_dir)
all_json_file = list(path.glob('**/*.json'))


from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['collection_name']
collection = db['db_name']

for file in all_json_file:

    data = []
    with open(file,'r') as f:
        for line in f:
            data.append(json.loads(line))
            
    try:
        collection_hp.insert(data)
    except:
        continue
    
client.close() 
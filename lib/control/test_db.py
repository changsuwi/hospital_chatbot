# -*- coding: utf-8 -*-


import pymongo

from datetime import datetime, timedelta

#  Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://localhost:27017'
client = pymongo.MongoClient(uri)
db = client.hospital
Category = db['kcom_output_0622_2']
total_data = Category.find()
count = 0
for data in total_data:
    data_list = []
    for i in range(1, 10):
        if(data['Kcom_' + str(i)] != ""):
            data_list.append(data['Kcom_' + str(i)])
    query = {'Pno': data['Pno']}
    Category.update(query, {'$set': {'list': data_list}})
    count = count + 1
    print(count)

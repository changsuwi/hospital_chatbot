# -*- coding: utf-8 -*-


import pymongo
import random
from ..json_fb import json_message
from datetime import datetime, timedelta

#  Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://localhost:27017'
client = pymongo.MongoClient(uri)
db = client.hospital
###############################################################################
# main
###############################################################################


def upload_flag(flag, sender_id):
    Category = db['flag']
    query = {'ID': sender_id}
    if(Category.count(query) == 0):
        Category.insert_one({'ID': sender_id, 'flag': flag})
    else:
        query = {'ID': sender_id}
        Category.update(query, {'$set': {'flag': flag}})


def get_flag(sender_id):
    Category = db['flag']
    dat = Category.find_one({'ID': sender_id})
    return dat['flag']


# match user's sym with data in database


def match_sym(sym_list):
    Category = db['kcom']
    total_data = Category.find()
    count = 0  # total match number
    time = 0  # total time
    result = {}  # key is Cresult and value is probobility
    for data in total_data:

        # make a list to store kcom
        data_list = []
        for i in range(1, 10):
            if(data['Kcom_' + str(i)] != ""):
                data_list.append(data['Kcom_' + str(i)])
        match = 1
        for item in sym_list:
            if item not in data_list:
                match = 0
                break

        if match:
            count = count + 1

            # calculate time in hospital
            bdate = datetime.strptime(data['Bdate'], '%Y/%m/%d %H:%M')
            edate = datetime.strptime(data['Edate'], '%Y/%m/%d %H:%M')
            time = time + (edate - bdate).days

            # replace some keyword
            if u"病房" in data['Cresult']:
                data['Cresult'] = "一般病房"
            if "ICU" in data['Cresult']:
                data['Cresult'] = "ICU"
            # store Cresult in dict
            if data['Cresult'] in result:
                result[data['Cresult']] = result[data['Cresult']] + 1
            else:
                result[data['Cresult']] = 1
    if count != 0:
        # mean
        meantime = time / count
        for key in result:
            result[key] = result[key] / count
        return result, meantime
    else:
        print("no data\n")
        return {}, 0

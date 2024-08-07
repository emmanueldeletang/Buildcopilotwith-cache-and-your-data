import os
import pymongo
from bson.json_util import dumps



client = pymongo.MongoClient("mongodb://mongoperformancetest:19aX3dUpWKL6fnjUWUIHIo8U7JDVR9ZNw9D1ueLthAT6xICTIOKldorG5mLebhcv5EUWmdDrmTWRxSytbM6exA==@mongoperformancetest.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mongoperformancetest@")

db = client['toto']
col = db['toto']

db = client.toto
col = db.toto


with col.watch(  [
        { '$match': { 'operationType': { '$in': ['insert', 'update', 'replace'] } } },
        { '$project': {  "fullDocument": 1  } }
    ],  "updateLookup" ) as stream:
       for change in stream:
           doc = change ['fullDocument']
           print(dumps(doc))

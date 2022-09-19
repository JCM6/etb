import requests, json
import pymongo

def MongoTestDB():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    dbConnection = client["etb_testdb"]
    return dbConnection

def SelectStatsModelCollection(_dbConnection):
    collection = _dbConnection["stats_models"]
    return collection

def InsertOneRecord(_collection, _record):
    record = _collection.insert_one(_record)
    return record

def InsertOneSetRecord(_recordJson):
    db = MongoTestDB()
    colle = SelectStatsModelCollection(_dbConnection=db)
    rec = InsertOneRecord(_collection=colle, _record=_recordJson)
    print(rec.inserted_id, rec)
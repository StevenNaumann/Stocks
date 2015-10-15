# Provides and interface to the mongodb database
from pymongo import MongoClient


# insert a row of data from the stock
def insert_data(stock, open, high, low, close, volume, adjClose, date):
    client = MongoClient()
    db = client.stockDB

    result = db.findOne({"stockIndex": stock, "date": date})

    # only insert data if we don't already have info for this date
    if result is not None:

        db.stockDB.insert_one(
            {
                "stockIndex": stock,
                "date": date,
                "open": open,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
                "adjClose": adjClose
            }
        )
    return


# clean out the database
def clear_db():
    client = MongoClient()
    db = client.stockDB

    db.dropDatabase()
    return

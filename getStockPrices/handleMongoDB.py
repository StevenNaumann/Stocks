# Provides and interface to the mongodb database
from pymongo import MongoClient


def insert_data(stock, open, high, low, close, volume, adjClose, date):
    client = MongoClient()
    db = client.stockDB  # switches the client to point at 'stockDB' database

    result = db.restaurants.insert_one(
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

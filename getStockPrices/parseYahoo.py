from __future__ import division
from lxml import html
import datetime
import math
import requests
import handleMongoDB


stockFile = open('stockIndexes.txt', 'r')

# loop over every stock index in the file and store in the database
for stock in stockFile:

    page = requests.get('http://finance.yahoo.com/q/hp?s=%s+Historical+Prices' % stock)
    tree = html.fromstring(page.text)

    # grab the data out of the yahoo finance table
    headers = tree.xpath('//th[@class="yfnc_tablehead1"]/text()')
    dataArray = tree.xpath('//td[@class="yfnc_tabledata1"]/text()')

    num_of_columns = len(headers)
    num_of_rows = len(dataArray)

    # number of rows of actual data to process
    num_of_loops = int(math.floor(num_of_rows / num_of_columns))

    print '%s' % stock

    # process the data in order
    counter = 0
    for data in range(0, num_of_loops):
        infoDate = dataArray[counter]
        infoOpen = dataArray[counter + 1]
        infoHigh = dataArray[counter + 2]
        infoLow = dataArray[counter + 3]
        infoClose = dataArray[counter + 4]
        infoVolume = dataArray[counter + 5]
        infoAdjClose = dataArray[counter + 6]

        # make sure that each date entered is a date object,
        # that way we don't need to worry about formatting any more
        dateObject = datetime.datetime.strptime(infoDate, "%b %d, %Y")

        # store the data in the database
        handleMongoDB.insert_data(stock, infoOpen, infoHigh, infoLow,
                                  infoClose, infoVolume, infoAdjClose, dateObject)

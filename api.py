import requests 
import time


def information():

    try:

        url = 'https://api.diadata.org/v1/assetQuotation/Bitcoin/0x0000000000000000000000000000000000000000'

        page = requests.get(url)

        data = page.json()

        symbol = data['Symbol']
        name = data['Name']
        price = data['Price']
        yesterdey_price = data['PriceYesterday']
        Time = data['Time']

        return symbol,name, price, yesterdey_price, Time
    
    except Exception as e:
        raise e

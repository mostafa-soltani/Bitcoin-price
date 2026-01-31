import csv
from api import information
import os
import time, datetime





def write(symbol,name, price, yesterdey_price, Time):

    file_name = 'price_bitcoin.csv'
    exsist_file = os.path.exists(file_name)

    try:

        with open(file_name,'a',newline='') as f:
            writer = csv.writer(f)
            if not exsist_file:
                writer.writerow(['symbol','name','Price','yesterdey_price','Time'])

            writer.writerow([symbol,name,price,yesterdey_price,Time])

    except Exception as e:
        raise e


end_time = '21:00:00'

while True:

    time_now = datetime.datetime.now().strftime("%H:%M:%S")

    if time_now >= end_time:
        break

    symbol,name, price, yesterdey_price, Time = information()

    print(f'writing price. time now {time_now} . end {end_time}')
    write(symbol,name,price,yesterdey_price,Time)
    time.sleep(180)

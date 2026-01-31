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


interval = 60 # sec


user = input("timer or round? ").strip().lower()




if user in ['timer', 'time']:
    minutes = int(input('How many minutes do you want to run? '))

    end_time = time.time() + minutes * 60

    while time.time() < end_time:
        symbol, name, price, yesterday_price, Time = information()
        write(symbol, name, price, yesterday_price, Time)
        print(f'Written at {Time}')

        time.sleep(interval)



elif user in ['round', 'times']:
    rounds = int(input('How many rounds do you want? '))

    for i in range(rounds):
        symbol, name, price, yesterday_price, Time = information()
        write(symbol, name, price, yesterday_price, Time)
        print(f'Written at {Time}')

        time.sleep(interval)

else:
    print("Invalid option. Choose 'timer' or 'round'")




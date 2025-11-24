import time 
from fetch_price import get_bitcoin_price
from add_data import add_price
from analyze import check_for_anomalies

print("--- Starting Market Tracker ----")
print('Press Ctrl+C to stop the bot')

while True:
    price = get_bitcoin_price()

    if price is not None:
        add_price("BTC", price)
        print("Updating...")
        check_for_anomalies()
    else:
        print("Skipping save due to error")

    time.sleep(5)
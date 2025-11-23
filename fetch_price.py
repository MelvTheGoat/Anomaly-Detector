import requests

def get_bitcoin_price():
    # url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    # try:
    #     response = requests.get(url)

    #     if response.status_code == 200:
    #         data = response.json()

    #         price = float(data['price'])
    #         print(f"Current Bitcoin Price ${price}")
    #         return get_bitcoin_price
    #     else:
    #         print("Error: Could not reach price from Binance")
    #         return None
    # except Exception as e:
    #     print(f"Connection Error: {e}")
    #     return None
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"

    try: 
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            price = data['solana']['usd']

            print(f"Current Bitcoin Price: ${price}")
            return price
        else:
            print(f"Error: API returned status code {response.status_code}")
            return None
        
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

# get_bitcoin_price()


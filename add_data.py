import sqlite3
from datetime import datetime 

def add_price(symbol, price):
    conn = sqlite3.connect('market_data.db')
    cursor = conn.cursor()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    query = 'INSERT INTO prices (symbol, price, timestamp) VALUES (?, ?, ?)'

    cursor.execute(query, (symbol, price, current_time))

    conn.commit()
    conn.close()

    print(f'Saved: {symbol} at ${price} on {current_time}')

add_price('BTC', 96000)
add_price('ETH', 3000)
add_price('SOL', 200)


import sqlite3 

def check_for_anomalies():
    conn = sqlite3.connect('market_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT price, timestamp FROM prices ORDER BY id DESC LIMIT 2")
    rows = cursor.fetchall()

    conn.close()

    if len(rows) < 2:
        print("Not enough data yet")
        return
    current_price = rows[0][0]
    current_time = rows[0][1]

    previous_price = rows[1][0]

    difference = current_price - previous_price
    percent_change = (difference/previous_price) * 100

    print(f"Time: {current_time}")
    print(f"Price moved from ${previous_price} to ${current_price}")

    threshold = 0.001

    if abs(percent_change) > threshold:
        print('ALERT: Price spike detected')
    else:
        print("Market is stable")

check_for_anomalies()
import sqlite3
conn = sqlite3.connect("market_data.db")
cursor = conn.cursor()

table = """
CREATE TABLE IF NOT EXISTS prices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    price REAL NOT NULL,
    timestamp TEXT NOT NULL
    );
    """

cursor.execute(table)
conn.commit()
conn.close()
import sqlite3
import pandas as pd
from datetime import datetime

DB_FILE = "mood.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS mood_entries (
            date TEXT,
            mood INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_entry(mood):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    # Always save with timestamp
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("INSERT INTO mood_entries (date, mood) VALUES (?, ?)", (date_str, mood))
    conn.commit()
    conn.close()

def get_entries():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM mood_entries ORDER BY date", conn)
    # Auto-detect format for each date string
    df['date'] = pd.to_datetime(df['date'], format='mixed')
    conn.close()
    return df

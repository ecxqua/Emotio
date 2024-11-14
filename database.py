import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS emotions
                          (id INTEGER PRIMARY KEY,
                           image_path TEXT,
                           emotion TEXT,
                           timestamp TEXT)''')
        self.conn.commit()

    def save_record(self, image_path, emotion):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO emotions (image_path, emotion, timestamp) VALUES (?, ?, ?)",
                       (image_path, emotion, timestamp))
        self.conn.commit()

    def get_history(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM emotions")
        return cursor.fetchall()

    def close(self):
        self.conn.close()

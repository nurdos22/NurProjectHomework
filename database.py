import sqlite3
class Database:
    def __init__(self, path):
        self.path = path
    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS complaints(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    instagram TEXT,
                    rate INTEGER,
                    comments TEXT
                )        
            """)
            conn.commit()
    def add_complaint(self, data: dict):
        print(data)
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO complaints (name, instagram, rate, comments) VALUES (?, ?, ?, ?)
            """,
                (data["name"], data["instagram"], data["rate"], data["comments"]),
            )
            conn.commit()
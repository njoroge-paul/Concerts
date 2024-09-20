import sqlite3

class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @classmethod
    def all_introductions(cls, conn):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT v.city, b.name, b.hometown 
            FROM bands b 
            JOIN concerts c ON b.id = c.band_id 
            JOIN venues v ON c.venue_id = v.id
        """)
        return [f"Hello {row[0]}!!!!! We are {row[1]} and we're from {row[2]}" for row in cursor.fetchall()]

    @classmethod
    def most_performances(cls, conn):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.name 
            FROM bands b 
            JOIN concerts c ON b.id = c.band_id 
            GROUP BY b.id 
            ORDER BY COUNT(c.id) DESC 
            LIMIT 1
        """)
        return cursor.fetchone()
    
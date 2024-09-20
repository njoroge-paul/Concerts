import sqlite3

class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city

    @classmethod
    def concerts(cls, conn, venue_id):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE venue_id = ?", (venue_id,))
        return cursor.fetchall()

    @classmethod
    def most_frequent_band(cls, conn, venue_id):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.name 
            FROM bands b 
            JOIN concerts c ON b.id = c.band_id 
            WHERE c.venue_id = ? 
            GROUP BY b.id 
            ORDER BY COUNT(c.id) DESC 
            LIMIT 1
        """, (venue_id,))
        return cursor.fetchone()

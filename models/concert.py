import sqlite3

class Concert:
    def __init__(self, band_id, venue_id, date):
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @classmethod
    def hometown_show(cls, conn, concert_id):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.hometown, v.city 
            FROM concerts c 
            JOIN bands b ON c.band_id = b.id 
            JOIN venues v ON c.venue_id = v.id 
            WHERE c.id = ?
        """, (concert_id,))
        hometown, city = cursor.fetchone()
        return hometown == city

    @classmethod
    def introduction(cls, conn, concert_id):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT v.city, b.name, b.hometown 
            FROM concerts c 
            JOIN bands b ON c.band_id = b.id 
            JOIN venues v ON c.venue_id = v.id 
            WHERE c.id = ?
        """, (concert_id,))
        city, name, hometown = cursor.fetchone()
        return f"Hello {city}!!!!! We are {name} and we're from {hometown}"

    @classmethod
    def create_concert(cls, conn, band_id, venue_id, date):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (band_id, venue_id, date))
        conn.commit()

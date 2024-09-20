import sqlite3
from models.band import Band
from models.venue import Venue
from models.concert import Concert
from migrations.create_tables import create_tables

def main():
    conn = sqlite3.connect('concerts.db')
    create_tables(conn)

    # Example data creation
    conn.execute("INSERT INTO bands (name, hometown) VALUES ('The Beatles', 'Liverpool')")
    conn.execute("INSERT INTO venues (title, city) VALUES ('Madison Square Garden', 'New York')")
    conn.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-09-20')")
    conn.commit()

    # Example method calls
    print(Band.all_introductions(conn))
    print(Band.most_performances(conn))
    
    conn.close()

if __name__ == "__main__":
    main()

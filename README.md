# Concerts Code Challenge

## Overview
This project implements a Concert domain using raw SQL to manage a simple database of bands, venues, and concerts. The relationships are structured such that a band can have multiple concerts, a venue can host multiple concerts, and each concert is associated with one band and one venue.

## Requirements
- Python 3.x
- SQLite3 (built-in with Python)

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd concerts

## Running the application
1. Run the following command to create the database and tables:
    python migrations/create_tables.py
2. Run the following to run the challenge    
    python main.py


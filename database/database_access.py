import sqlite3

def connect_to_database(database_name):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(database_name)
    return conn

def fetch_national_parks(conn):
    """Fetch all national parks from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM national_parks")
    rows = cursor.fetchall()
    return rows


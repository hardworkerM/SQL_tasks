import sqlite3 as lite


def connect_to_db():
    conn = lite.connect('users.db')
    cursor = conn.cursor()
    return conn, cursor

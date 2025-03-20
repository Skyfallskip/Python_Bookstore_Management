import sqlite3

def connect():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.commit()
    conn.close()

def insert_book(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_book(id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_book(id, title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

def insert_user(name, email):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO user VALUES (NULL, ?, ?)", (name, email))
    conn.commit()
    conn.close()

def view_users():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_user(id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM user WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_user(id, name, email):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE user SET name=?, email=? WHERE id=?", (name, email, id))
    conn.commit()
    conn.close()

connect()
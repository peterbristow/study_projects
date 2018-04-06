"""Database file for crud operations."""
import psycopg2


def connect():
    """To open a python REPL use: python -i db.py."""
    c = psycopg2.connect("dbname=flask-toys user=peter")
    return c


def create_table():
    """Cretae table in the database."""
    conn = connect()
    cur = conn.cursor()
    sql = ('CREATE TABLE IF NOT EXISTS toys '
           '(id serial PRIMARY KEY, name text);')
    cur.execute(sql)
    conn.commit()
    connect().close()


def get_all_toys():
    """Get all toys."""
    conn = connect()
    cur = conn.cursor()
    sql = 'SELECT * FROM toys'
    cur.execute(sql)
    toys = cur.fetchall()
    cur.close()
    conn.close()
    return toys


def add_toy(name):
    """Add a toy to the database."""
    conn = connect()
    cur = conn.cursor()
    sql = 'INSERT INTO toys (name) VALUES (%s)'
    data = (name, )
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()


def get_toy(id):
    """Get toy."""
    conn = connect()
    cur = conn.cursor()
    sql = 'SELECT * FROM toys WHERE id = (%s)'
    data = (id, )
    cur.execute(sql, data)
    toy = cur.fetchone()
    cur.close()
    conn.close()
    return toy


def edit_toy(id, name):
    """Edit toy."""
    conn = connect()
    cur = conn.cursor()
    sql = 'UPDATE toys SET name = (%s) WHERE id = (%s)'
    data = (name, id, )
    print(data)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()


def delete_toy(id):
    """Delete toy."""
    conn = connect()
    cur = conn.cursor()
    sql = 'DELETE FROM toys WHERE id = (%s)'
    data = (id, )
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()

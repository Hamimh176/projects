import sqlite3 as sql
import hashlib as ha

conn = sql.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "hamimh10", ha.sha256("HamimH10".encode()).hexdigest()
username2, password2 = "bla", ha.sha256("bla".encode()).hexdigest()
username3, password3 = "bored", ha.sha256("bored".encode()).hexdigest()
username4, password4 = "learning", ha.sha256("idk".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username4, password4))

conn.commit()

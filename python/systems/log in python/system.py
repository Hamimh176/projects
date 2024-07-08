import sqlite3 as sql
import hashlib as ha
import socket as sock
import threading as thr
server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()

def handle_connection(c):
    c.send("Username: ".encode()) # send only encoded data
    username = c.recv(1024).decode() # decode the recieved data
    c.send("Password:".encode())
    password = c.recv(1024).decode()
    password = ha.sha256(password).hexdigest()

    conn = sql.connect("userdata.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        c.send("Login successful.".encode())
    else:
        c.send("Login failed.".encode())

while True:
    client, addr = server.accept()
    thr.Thread(target = handle_connection, args = (client)).start()
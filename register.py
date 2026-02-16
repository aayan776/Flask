from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL)""")
    con.commit()
    con.close()
init_db()
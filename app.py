from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(**name**)

def db():
conn = sqlite3.connect("store.db")
conn.row_factory = sqlite3.Row
return conn

@app.route("/")
def home():
return "Website Running Successfully"

if **name** == "**main**":
app.run()

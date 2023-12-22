from flask_mysqldb import MySQL
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()
import os

# create the flask app
app = Flask(__name__, template_folder='todolist')

# Required
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_PORT"] = int(os.getenv("MYSQL_PORT"))
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
app.config["MYSQL_AUTOCOMMIT"] = True
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM task_view")
    todolist = cur.fetchall()
    cur.nextset()
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()
    cur.close()
    return render_template("index.html", todolist=todolist, categories=categories)
import flask
from flask import Flask, render_template, url_for, jsonify
import sqlite3

# Constants:
HTML_SNIPPET: str = '<h1> Hello, World </h1>'
MAIN_NAME: str = '__main__'
ENTRY_POINT_NAME: str = "index.html"

# Create a flask application object.
application: Flask = Flask(__name__)


# FOR TESTING PURPOSES

connection: sqlite3.Connection = sqlite3.connect("database.db")
cursor: sqlite3.Cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, forename TEXT, surname TEXT);")
connection.close()

# !FOR TESTING PURPOSES

# Define the application's entry point.
@application.route("/")
def app_main() -> str:
    return render_template(ENTRY_POINT_NAME)


@application.route("/home")
def home() -> str:
    return render_template("test_home.html")

@application.route("/get_home_data")
def get_home_data() -> flask.Response:
    connection: sqlite3.Connection = sqlite3.connect("database.db")
    cursor: sqlite3.Cursor = connection.cursor()
    cursor.execute("SELECT forename, surname FROM customers")
    data = cursor.fetchall()
    connection.close()

    return jsonify(data)


# Call the application's entry point:
if __name__ == MAIN_NAME:
    application.run(debug=True)

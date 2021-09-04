from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/list")
def bklist():
    conn = sqlite3.connect("dbfile/bookbase.db")
    conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    cur.execute("SELECT * FROM booklist")
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html", rows = rows)

if __name__ == "__main__":
    app.run(debug=True)
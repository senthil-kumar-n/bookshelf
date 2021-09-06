from sqlite3.dbapi2 import connect
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/list", methods = ['POST', 'GET'])
def bklist():
    if request.method == 'GET':
        conn = sqlite3.connect("dbfile/bookbase.db")
        conn.row_factory = sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM booklist")
        rows = cur.fetchall()
        conn.close()
        return render_template("list.html", rows = rows)
    elif request.method == 'POST':
        searchvar = request.form['bsearch']
        searchvar1 = request.form['bauthor']          
        conn = sqlite3.connect("dbfile/bookbase.db")    
        conn.row_factory = sqlite3.Row
        cur=conn.cursor()    
        cur.execute("SELECT * FROM booklist WHERE bookname like ? or author like ? ",('%'+searchvar+'%','%'+searchvar1+'%',))
        #cur.execute("SELECT * FROM booklist WHERE author like ? ",('%'+searchvar1+'%',))
        rows = cur.fetchall()
        conn.close()
        print(rows)                      
        return render_template("list.html", rows = rows)
    

if __name__ == "__main__":
    app.run(debug=True)
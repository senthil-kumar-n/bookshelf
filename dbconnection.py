import sqlite3

def view():
    conn = sqlite3.connect("dbfile/bookbase.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM booklist")
    rows = cur.fetchall()
    conn.close()
    print (rows)
    print(type(rows))

print(view())

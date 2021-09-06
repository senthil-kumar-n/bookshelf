import sqlite3

def view():
    conn = sqlite3.connect("dbfile/bookbase.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM booklist")
    rows = cur.fetchall()
    conn.close()
    #return render_template("list.html", rows = rows)
    return rows
    

def searchfun(bauthor=""):
    conn = sqlite3.connect("dbfile/bookbase.db")
    cur=conn.cursor()    
    cur.execute("SELECT * FROM booklist WHERE author OR bookname like ?" ,('%'+bauthor+'%',))
    #  "select string from stringtable where string like ? and type = ?", ('%'+searchstr+'%', type))
    #cur.execute("SELECT * FROM booklist WHERE bookname like ? OR author like ? ",('%'+searchvar+'%','%'+searchvar1+'%'))
    rows = cur.fetchall()
    conn.close()
    return rows    
print(searchfun("walt"))
#print(view()
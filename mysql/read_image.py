import MySQLdb as mdb 
def writeImage(data):
    fout = open('sid2.jpg', 'wb')
    with fout:
        fout.write(data)
con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
with con:
    cur = con.cursor()
    cur.execute("SELECT Data FROM Images WHERE Id=1")
    data = cur.fetchone()[0]
    writeImage(data)  
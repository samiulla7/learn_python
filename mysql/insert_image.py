import MySQLdb as mdb
def read_image():
    with open("download.jpeg",'rb') as f:
        img = f.read()
        return img
con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
with con:
    cur = con.cursor()
    data = read_image()
    cur.execute("INSERT INTO Images VALUES(1, %s)", (data, ))
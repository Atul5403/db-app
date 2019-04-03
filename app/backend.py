import sqlite3

def connect():
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS kharch (id INTEGER PRIMARY KEY, name TEXT, cost INTEGER)")
	conn.commit()
	conn.close()

def insert(name, cost):
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO kharch VALUES (NULL,?,?)",(name, cost))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM kharch")
	rows = cur.fetchall()
	conn.close()
	return rows

def search(name="",cost=""):
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM kharch WHERE name = ? OR cost = ?",(name,cost))
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("DELETE FROM kharch WHERE id = ?",(id,))
	conn.commit()
	conn.close()

def update(id,name,cost):
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("UPDATE kharch SET name = ?, cost = ? WHERE id = ?",(name,cost,id))
	conn.commit()
	conn.close()
	
connect()
update(2,"haria",3000)
#insert('hari',2000)
print(view())
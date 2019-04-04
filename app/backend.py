import sqlite3

def connect():
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS kharch (id INTEGER PRIMARY KEY, name TEXT, cost INTEGER)")
	conn.commit()
	conn.close()
	print("connected to database")

# working in both 
def view():
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM kharch")
	rows = cur.fetchall()
	conn.close()
	return rows
	print("fetched all data")

# working in both
def search(id="",name="",cost=""):
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM kharch WHERE id = ? OR name = ? OR cost = ?",(id,name,cost))
	rows = cur.fetchall()
	conn.close()
	return rows

# working in both
def insert(name, cost):
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO kharch VALUES (NULL,?,?)",(name, cost))
	conn.commit()
	conn.close()

# working in both
def update(id="",name="",cost=""):
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	if name == "":
		cur.execute("UPDATE kharch SET  cost = ? WHERE id = ?",(cost,id))
	elif cost == "":
		cur.execute("UPDATE kharch SET name = ? WHERE id = ?",(name,id))
	elif name != "" and cost != "":
		cur.execute("UPDATE kharch SET name = ?,cost = ? WHERE id = ?",(name,cost,id))
	conn.commit()
	conn.close()

# working in both
def delete(id):
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("DELETE FROM kharch WHERE id = ?",(id,))
	conn.commit()
	conn.close()

def summation():
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("SELECT SUM(cost) FROM kharch")
	a = cur.fetchall()[0][0]
	conn.commit()
	conn.close()
	return a



	
connect()

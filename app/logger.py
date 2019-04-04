import sqlite3

def connect():
	conn = sqlite3.connect('kharcha.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, type TEXT, name TEXT,cost INTEGER,at DATETIME)")
	conn.commit()
	conn.close()
	print("connected to database")
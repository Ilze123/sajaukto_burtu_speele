import sqlite3
import json

JSON = 'dati/rez.json'
DB = sqlite3.connect('dati/dat_b.db')
SQL = DB.cursor()
  
SQL.execute("""CREATE TABLE IF NOT EXISTS rez ( 
              id INTEGER NOT NULL UNIQUE,
              vards TEXT,
              punkti INTEGER,
              burti INTEGER,
              PRIMARY KEY("id" AUTOINCREMENT)
           )""")

with open(JSON, 'r', encoding="UTF-8") as f:
  dati = f.read()
  datiJson = json.loads(dati)

  for dati in datiJson:
    SQL.execute("INSERT INTO rez (vards, punkti, burti) VALUES (:vards, :punkti, :burti)", {'vards': dati['vards'], 'punkti': dati['punkti'], 'burti':dati['burti']})



DB.commit()

SQL.execute("SELECT * FROM rez ORDER BY punkti DESC,  burti DESC")

print(SQL.fetchall())
    
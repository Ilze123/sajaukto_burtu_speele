import sqlite3

def savienot():
  DB = sqlite3.connect('dat_b.db')
  return DB.cursor()
  

def top():
  SQL = savienot()
  SQL.execute("SELECT * FROM rez")
  rezultati = SQL.fetchall()
  dati = []
  for rezultati in rez:
    dati.append({
      "id":rez[0],
      "vards":rez[1],
      "punkti":rez[2],
      "burti":rez[3],

    })

  # print(dati)
  return dati

def pievienot(dati):
  SQL = savienot()
  SQL.execute("INSERT INTO rezultati (vards, punkti, burti) VALUES (:vards, :punkti, :burti)", {'vards': dati['vards'], 'punkti': dati['punkti'], 'burti':dati['burti']})
  
from flask import Flask, render_template, jsonify, request, json
import sqlite3

app = Flask('app')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def galvenais():
  return render_template("index.html")

@app.route('/top', methods=["GET", "POST"])
def rezultati():
  print(request.json ["vards"],request.json["punkti"],request.json["burti"])
  with open("dati/top.json", "r",encoding="utf-8") as f:
    rezultats = f.read()
  return jsonify(rezultats)

@app.route('/rezultativecie', methods=["GET", "POST"])
def rezultati_1():
  # print(request.json ["vards"],request.json["punkti"])
  if request.method=="POST":
    dati=request.json
    if dati!=None:
      f=open("dati/rez.json", "r")
      reslist=json.load(f)
      f.close()
      reslist.append(dati)
      f=open("dati/rez.json", "w")
      json.dump(reslist,f)
      f.close()
  f=open("dati/rez.json", "r")
  reslist=json.load(f)
  f.close()
  return json.dumps(sorted(reslist,key=lambda vi:(vi["punkti"]), reverse=True))

@app.route('/rezultati',methods=["GET", "POST"])
def topData():
  DB = sqlite3.connect('dati/dat_b.db')
  SQL = DB.cursor()
  if request.method=="POST":
    dati=request.get_json()
    
  
    # sqldata ={'vards': dati['vards'], 'punkti': dati['punkti'], 'burti':dati['burti']}
    # SQL.execute("INSERT INTO rez (vards, punkti, burti) VALUES (?,?,?)", sqldata)
    sqldata=(dati['vards'], dati['punkti'], dati['burti'])
    SQL.execute("INSERT INTO rez (vards, punkti, burti) VALUES (?, ?, ?)", sqldata)
    # SQL.execute("INSERT INTO rez (vards, punkti, burti) VALUES (:vards, :punkti, :burti)", {'vards': dati['vards'], 'punkti': dati['punkti'], 'burti':dati['burti']}) 
    # val = (dati["vards"], dati["punkti"],dati["burti"])
      # SQL.execute(ievietot)
    DB.commit()
  # SQL.execute("SELECT * FROM rez ORDER BY punkti DESC, burti DESC")
  SQL.execute("SELECT * FROM rez ORDER BY punkti DESC, burti DESC LIMIT 10")
  atbilde=SQL.fetchall()
  resList=[]
  for v in atbilde:
        resList.append({"vards":v[1],"punkti":v[2],"burti":v[3]})
  return json.dumps(resList)

  # return jsonify(SQL.fetchall())

# SQL.execute("INSERT INTO rezultati (vards, punkti, burti) VALUES (:vards, :punkti, :burti)", {'vards': dati['vards'], 'punkti': dati['punkti'], 'burti':dati['burti']})












  
# @app.route('/top/labakais')
# def labakais():
#   with open("dati/labakais", "r") as f:
#     rezultats = f.read()
#   return rezultats


# @app.route('/top/rekords/')
# def rekords(jaunais):
#   with open ("dati/top", "r") as f:
#     top = int(f.read())
#   try:
#     jaunais_skaitlis = int(jaunais)
#   except:
#       return str(top)
#   if jaunais_skaitlis > top:

#     with open("dati/top", "w") as f:
#       f.write(jaunais)
#     return jaunais
#   else:
#     return str(top) 


 
  












app.run(host='0.0.0.0', port=8080)

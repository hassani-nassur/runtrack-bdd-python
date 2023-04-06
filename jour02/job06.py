#encode : utf-8
import mysql.connector as MC

dbhost = "localhost"
dbname = "laplateforme"
mdp = ""
user = "root"

try:
   con = MC.connect(host = dbhost, user = user, database = dbname, passwd = mdp) 
   cursor = con.cursor()
   requette = "SELECT SUM(`capacite`) FROM `salles`"
   
   cursor.execute(requette)
   
   resultat = cursor.fetchone()
   print("la capacitée de tous les salles est de {}".format(resultat[0]))
except Exception as e:
    print("[ERROR] ",e)
finally:
    if con.connect():
        con.close()
        cursor.close()
#encode : utf-8
import mysql.connector as MC

dbhost = "localhost"
dbname = "laplateforme"
mdp = ""
user = "root"

try:
    
   con = MC.connect(host = dbhost, user = user, database = dbname, passwd = mdp) 
   cursor = con.cursor()
   requette = "SELECT SUM(`superficie`) as sup FROM `etage`"
   
   cursor.execute(requette)
   
   resultat = cursor.fetchone()
   print("La superficie de Laplateforme est de {} m²".format(resultat[0]))

except Exception as e:
    print("[ERROR] ",e)

finally:
    if con.connect():
        con.close()
        cursor.close()
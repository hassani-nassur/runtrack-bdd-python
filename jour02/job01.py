# encode : utf-8
import mysql.connector as MC

try:
    con = MC.connect(host="localhost",user="root",passwd="",database="Laplateforme")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM `etudiants`")
    resultat = cursor.fetchall()
    for i in resultat:
        print(i)
except Exception as e:
    print("[ERROR]",e)
finally:
    if con.connect():
        con.close()
        cursor.close()
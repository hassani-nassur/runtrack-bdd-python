# encode : utf-8

# la base de donnée utiliser se nomme "gestion_employes"

import mysql.connector as MC

dbhost = "localhost"
dbname = "gestion_employes"
mdp = ""
user = "root"

try:
    con = MC.connect(host = dbhost, user = user, database = dbname, passwd = mdp) 
except Exception as e:
    print("[ERROR] ",e)

class Employes:
    def __init__(self,con) :
        self.con = con
        self.cursor = con.cursor()
    
    # insertion d'un employer
    def insert(self,nom,prenom,salaire,id_service):
        
        requete = "INSERT INTO employes(id_employer,nom,prenom,salaire,id_service) VALUES (%s,%s,%s,%s,%s)"
        dataTo_insert = (self.cursor.lastrowid,nom,prenom,salaire,id_service)
        
        self.cursor.execute(requete,dataTo_insert)
        self.con.commit()
    
    # 
    def select(self,id= None):
        if(id != None):
            requete = "SELECT * FROM `employes` WHERE `id_employer` = %s"
            self.cursor.execute(requete,(id,))
            resultat = self.cursor.fetchone()
        else:
            requete = "SELECT * FROM `employes`" 
            self.cursor.execute(requete)
            resultat = self.cursor.fetchall()
        
        return resultat
    
    # suprimer un element
    def delete(self,id):
        requete = "DELETE FROM `employes` WHERE `id_employer`=%s"
        self.cursor.execute(requete,(id,))
    
    def update_name(self,id_employe,nom):
        requete = "UPDATE `employes`SET `nom` = %s WHERE `id_employer` = %s"
        self.cursor.execute(requete,(nom,id_employe))
    def update_firstName(self,id_employe,prenom):
        requete = "UPDATE `employes`SET `prenom` = %s WHERE `id_employer` = %s"
        self.cursor.execute(requete,(prenom,id_employe))
    def update_salaire(self,id_employe,salaire):
        requete = "UPDATE `employes`SET `salaire` = %s WHERE `id_employer` = %s"
        self.cursor.execute(requete,(salaire,id_employe))
    def update_service(self,id_employe,id_service):
        requete = "UPDATE `employes`SET `id_service` = %s WHERE `id_employer` = %s"
        self.cursor.execute(requete,(id_service,id_employe))
    
    def close_connection(self):
        self.con.close()
        self.cursor.close()
        
mabase = Employes(con)  

# mabase.insert("Nasra","Hassani",3600,1)

# mabase.delete(21)

mabase.update_name(10,"jordan")

employers = mabase.select()

print(employers)

mabase.close_connection()
# encode: utf-8

class Animal:
    
    def __init__(self,con):
        self.con = con
        self.cursor = con.cursor()
    
    def insert(self,nom,race,date_naisse,pay_naissance,id_cage):
        
        requete = "INSERT INTO `animal`(`nom`,`race`,`date_naissance`,`pays_naissance`,`id_cage`) VALUES(%s,%s,%s,%s,%s)"
        
        data = (nom,race,date_naisse,pay_naissance,id_cage)
        self.cursor.execute(requete,data)
        self.con.commit()
    
    def delete(self,id_animal):
        
        requete = "DELETE FROM `animal` WHERE `id_animal`=%s"
        self.cursor.execute(requete,(id_animal,))
        self.con.commit()
        
    def select(self,id_animal=None):
        
        if(id_animal == None):
            requete = "SELECT * FROM `animal`"
            self.cursor.execute(requete)
            
            resultat = self.cursor.fetchall()
        else:
            requete = "SELECT * FROM `animal` WHERE `id_animal`=%s"
            self.cursor.execute(requete,(id_animal,))   
            resultat = self.cursor.fetchone()
        
        return resultat
    
    def update(self,id_animal,nom,race,date_naiss,pays_naiss,id_cage):
        
        requete = "UPDATE `animal `SET` nom = %s, race =%s, date_naissance = %s, pays_naissance = %s, id_cage = %s WHERE `id_animal`=%s" 
        data = (nom,race,date_naiss,pays_naiss,id_cage,id_animal)
        
        self.cursor.execute(requete,data)
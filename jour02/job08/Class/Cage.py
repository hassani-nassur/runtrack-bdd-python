class Cage:
    
    def __init__(self,con):
        self.con = con
        self.cursor = con.cursor()
    
    def insert(self,superficie,capacite_max):
        requete = "INSERT INTO `cage`(`superficie`,`capacite_max`) VALUES (%s,%s)"
        self.cursor.execute(requete,(superficie,capacite_max))
        self.con.commit()
    
    def delete(self,id_cage):
        requete = "DELETE FROM `animal` WHERE `id_cage` = %s"
        self.cursor.execute(requete,(id_cage,))
        
        requete = "DELETE FROM `cage` where `id_cage` = %s"
        self.cursor.execute(requete,(id_cage,))
        self.con.commit()
    
    def update(self,id_cage,superficie,capacite_max):
        requete = "UPDATE `cage` SET `capacite` = %s,`superficie`=%s WHERE `id_cage` = %s"
        self.cursor.execute(requete,(capacite_max,superficie,id_cage))
    
    def select(self,id_cage =None):
        if id_cage == None:
            requete = "SELECT * FROM `cage`"
            self.cursor.execute(requete)
            resultat = self.cursor.fetchall()
        else:
            requete = "SELECT * FROM `cage` WHERE `id_cage` = %s"
            self.cursor.execute(requete,(id_cage,))
            resultat = self.cursor.fetchone()
        return resultat
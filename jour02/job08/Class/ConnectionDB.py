import mysql.connector as MC

class Connection:
    def __init__(self):
        try:
            self.con = MC.connect(host="localhost",user="root",passwd="",database="zoo")
        except Exception as e:
            print("[ERROR]",e)
    def get_connection(self):
        return self.con
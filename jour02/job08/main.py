import tkinter as tk
from tkinter import ttk
from Class.ConnectionDB import *
from Class.Animal import *
from Class.Cage import *
from tkcalendar import *
from tkinter import messagebox,StringVar

class Main:
    
    def __init__(self,fenetre,con):
        
        self.fenetre = fenetre
        self.con = con
        self.cage = Cage(self.con)
        self.animal = Animal(self.con)
        
        self.display()
        self.config()
        self.fenetre.mainloop()
    
    # affichage
    def display(self):
        
        # formulaire d'ajout d'un animal 
        self.formulaire_add_animal()
        
        #liste des cages
        self.show_cage()
        
        # button lists animal et ajout cage
        btn_list_anmal = tk.Button(self.fenetre,text="Lister des animeaux",command=self.list_animal)
        btn_list_anmal.place(x=110,y=450)
        
        # button ajout cage
        btn_Ajout_cage = tk.Button(self.fenetre,text="Ajouter une cage",command=self.formulaire_add_cage)
        btn_Ajout_cage.place(x=450,y=450)
    
    def list_animal(self):
        
        self.screen = tk.Tk()
        
        self.screen.geometry("820x350")
        self.screen.title("Liste des Animaux")
        
        self.Tableau = ttk.Treeview(self.screen,columns=(1,2,3,4,5,6),heigh=18,show="headings")
        self.Tableau.place(x=9,y=10,width=800,height=270)
        
        self.Tableau.heading(1,text="ID")
        self.Tableau.heading(2,text="Nom")
        self.Tableau.heading(3,text="Race")
        self.Tableau.heading(4,text="Pays de naissance")
        self.Tableau.heading(5,text="Date de naissance")
        self.Tableau.heading(6,text="Numero de cage")
        
        self.Tableau.column(1,width=2)
        self.Tableau.column(2,width=2)
        self.Tableau.column(3,width=2)
        self.Tableau.column(4,width=2)
        self.Tableau.column(5,width=2)
        self.Tableau.column(6,width=2)
        
        animals = self.animal.select()
        
        for animal in animals:
            self.Tableau.insert('','end',iid=animal[0],values=animal)
        
        btn_sup_animal = tk.Button(self.screen,text="Supprimer", command=self.delete_data)
        btn_sup_animal.place(x=20,y=300)
        
    def delete_data(self):
        
        if(self.Tableau.focus() !=''):
            row_id = int(self.Tableau.focus())
            
            if messagebox.askyesno("Suppression","Cette action est irreversible,\n êtes vous sûr de vouloir supprimer l'animal?"):
                
                self.animal.delete(row_id)
                self.Tableau.delete(row_id)
                messagebox.showinfo("Suppression","Operation effectuer")
            
    # formulaire d'ajout d'un animal 
    def formulaire_add_animal(self):
        
        self.canvas_animal = tk.Canvas(self.fenetre,width=300,height=400)
        self.canvas_animal.place(x=10,y=20)
        
        #Nom animal
        tk.Label(self.canvas_animal,text="Nom animal",font=('times new roman',14)).place(x=10,y=10)
        self.nom_animal = tk.Entry(self.canvas_animal,font=("times new roman",15))
        self.nom_animal.place(x=10,y=40,width=250)
        
        #Race animal
        tk.Label(self.canvas_animal,text="Race de l'animal",font=('times new roman',14)).place(x=10,y=80)
        self.race_animal = tk.Entry(self.canvas_animal,font=("times new roman",15))
        self.race_animal.place(x=10,y=110,width=250)
        
        #Date de naissance de l'animal
        tk.Label(self.canvas_animal,text="Date de naissance de l'animal",font=('times new roman',14)).place(x=10,y=150)
        self.date_naiss_animal = DateEntry(self.canvas_animal,date_pattern="dd/mm/yy",font=("times new roman",15),state="readonly")
        self.date_naiss_animal.place(x=10,y=180,width=250)
        
        #pays de naissance animal
        tk.Label(self.canvas_animal,text="Pays de Naissance de l'animal",font=('times new roman',14)).place(x=10,y=220)
        self.pays_naiss_animal = tk.Entry(self.canvas_animal,font=("times new roman",15),width=20)
        self.pays_naiss_animal.place(x=10,y=250,width=250)
        
        nombre_cage = len(self.cage.select())
        #pays de naissance animal
        tk.Label(self.canvas_animal,text="Numero de la cage",font=('times new roman',14)).place(x=10,y=290)
        self.numero_cage = tk.Spinbox(self.canvas_animal,font=("times new roman",15),from_= 1,to=nombre_cage)
        self.numero_cage.place(x=10,y=320,width=250)
        
        btn_ajout_animal = tk.Button(self.canvas_animal,text="Enregistrer",bg="#828bf7",font=('times new roman',14),command=self.save_animal)
        btn_ajout_animal.place(x=100,y=370)
    
    def save_animal(self):
        
        nom_animal = self.nom_animal.get()
        race_animal = self.race_animal.get()
        date_naiss = self.date_naiss_animal.get()
        pays_naiss = self.pays_naiss_animal.get()
        id_cage = self.numero_cage.get() 
        
        self.animal.insert(nom_animal,race_animal,date_naiss,pays_naiss,id_cage)
        
        if self.canvas_animal in self.fenetre.winfo_children():
            self.canvas_animal.destroy()
            self.formulaire_add_animal()
          
    # list des cages
    def show_cage(self):
        
        self.canvas_cage = tk.Canvas(self.fenetre,width=300,height=400,bg="green")
        self.canvas_cage.place(x=350,y=10)
        
        titre = tk.Label(self.canvas_cage,text="Liste des Cage",font=("Times new roman",14)).place(x=100,y=10)
        self.list_cage = ttk.Treeview(self.canvas_cage,columns=(1,2,3),heigh=16,show="headings")
        self.list_cage.place(x=9,y=50,width=285)
        self.list_cage.heading(1,text="Numero")
        self.list_cage.heading(2,text="Superficie")
        self.list_cage.heading(3,text="Capacité Max")
        
        self.list_cage.column(1,width=2)
        self.list_cage.column(2,width=3)
        self.list_cage.column(3,width=12)
        cages = self.cage.select()
        
        for cage in cages:
            self.list_cage.insert('','end',iid=cage[0],values=cage)
        
        btn_sup_cage = tk.Button(self.fenetre,text="Supprimer", command=self.delete_cage)
        btn_sup_cage.place(x=670,y=340,width=70)
    
    def delete_cage(self):
        
        if(self.list_cage.focus() !=''):
            row_id = int(self.list_cage.focus())
            if messagebox.askyesno("Attention","Cette action est irreversible,Cette action entrenera la suppression des animeaux enregistrer dans cette case\n êtes vous sûr de vouloir supprimer l'animal?"):
                    
                self.cage.delete(row_id)
                self.list_cage.delete(row_id)
                messagebox.showinfo("Suppression","Operation effectuer")
                
    
       
    def config(self):
        self.fenetre.geometry("750x500+160+120")
        self.fenetre.title("Zoo")

    
    def formulaire_add_cage(self):
        self.fen = tk.Tk()
        #Superficie
        tk.Label(self.fen,text="Superficie",font=('times new roman',14)).place(x=10,y=10)
        self.superficie_cage = tk.Entry(self.fen,font=("times new roman",15))
        self.superficie_cage.place(x=10,y=40,width=140)
        
        #Capacité Maximal
        tk.Label(self.fen,text="Capacité Maximal",font=('times new roman',14)).place(x=10,y=80)
        self.capacite_cage = tk.Entry(self.fen,font=("times new roman",15))
        self.capacite_cage.place(x=10,y=110,width=140)
        
        btn_Ajout_cage = tk.Button(self.fen,text="Enregistrer",command=self.save_cage)
        btn_Ajout_cage.place(x=40,y=140)
    
    
    def save_cage(self):
        superficie = self.superficie_cage.get()
        capacite_cage = self.capacite_cage.get()
        
        self.cage.insert(superficie,capacite_cage)
        
        self.fen.destroy()
        
        if self.canvas_cage in self.fenetre.winfo_children():
            self.canvas_cage.destroy()
            self.show_cage() 
        


# creation d'une fenete et d'une connexion

#connexion à la base de donnée
ma_connection = Connection()
con = ma_connection.get_connection()

#premier fenetre 
fenetre = tk.Tk()

main = Main(fenetre,con)
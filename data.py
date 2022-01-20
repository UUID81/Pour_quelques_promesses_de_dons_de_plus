import mysql.connector as msql

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor

    bdd = msql.connect(user='root', password='root', host='localhost', port='8081', database='datas_dons')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()

def get_donnateurs() :
    global cursor

    connexion()
    query = "SELECT * FROM donnateurs"
    cursor.execute(query)
    donnateurs = []

    for enregistrement in cursor :
        donnateur = {}
        donnateur['id_nom'] = enregistrement[0]
        donnateur['nom'] = enregistrement[1]
        donnateur['prenom'] = enregistrement[2]
        donnateur['don'] = enregistrement[3]
        donnateurs.append(donnateur)
    
    print(donnateurs)
    deconnexion()
    return donnateurs

def get_donnateur():
    global cursor

    connexion()
    query = "SELECT * FROM donnateurs"
    # query = "SELECT nom, prenom, don FROM donnateurs"
    cursor.execute(query)
    donnateur = {}

    for enregistrement in cursor :
        
        donnateur['id_nom'] = enregistrement[0]
        donnateur['nom'] = enregistrement[1]
        donnateur['prenom'] = enregistrement[2]
        donnateur['don'] = enregistrement[3]
    
    deconnexion()
    return donnateur

def set_donnateurs(nom, prenom, don):
    global bdd
    global cursor

    connexion()

    query='INSERT INTO donnateurs(nom, prenom, don) VALUES (%s, %s, %s);'
    valeurs = (nom, prenom, don)
    cursor.execute(query, valeurs)
    bdd.commit()

    deconnexion()

def total_dons() :
    global bdd
    global cursor
    
    connexion()
    query = "SELECT don FROM form"
    cursor.execute(query)
    total=0
    
    for enregistrement in cursor : 
        total += enregistrement[0]
        
    deconnexion()
    return total    

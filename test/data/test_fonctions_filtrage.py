import pandas as pd
import fonctions_filtrage as ff
import numpy as np




#Crée les deux dataframes qui seront utilisés pour les tests
def creedfexemple(numéro_test):
    if numéro_test==1:        
        data = pd.DataFrame({'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                             'Âge': [25, 30, None, 22, 28],
                             'Ville': ['Paris', 'New York', 'Los Angeles', None, 'Berlin'],
                             'Salaire': [50000, None, 60000, None, 75000],
                             'Ville2': ['Paris', 'New York', 'Los Angeles', None, 'Berlin']})
    elif numéro_test==2:
        data = pd.DataFrame({'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                             'Âge': [25, 30, None, 22, 28],
                             'Ville': ['Paris', 'New York', 'Los Angeles', None, 'Berlin'],
                             'Salaire': [50000, None, 60000, None, 75000],
                             'Passions': ['lecture, cuisine, sport', 
                                          'cuisine, sport, dessin', 
                                          'manga, informatique, tiboinshape', 
                                          None, 
                                          'sport']})
    return(data)

#Compare deux dataframes 
def comparedf(df1,df2):
    compare = (df1 == df2) | (df1.isna() & df2.isna())
    return(compare.all().all())

#Voulant rendre le script de nettoyage le plus flexible possible, la mention
#de colonnes n'existant plus risque d'arriver fréquemment. Afin d'éviter d'avoir
#à modifier le script à chaque fois, chaque programme pouvoir renvoyer le 
#dataframe initiale si la colonne mentionnée n'existe pas
nom_colonnefictive = 'mescheveux'





#supprimer_lignes_na
data = creedfexemple(1)
datasol = pd.DataFrame({'Nom': ['Alice', 'Charlie', 'Eva'],
                     'Âge': [25, None, 28],
                     'Ville': ['Paris', 'Los Angeles', 'Berlin'],
                     'Salaire': [50000, 60000, 75000],
                     'Ville2': ['Paris', 'Los Angeles', 'Berlin']})
nom_colonne = 'Salaire'
data=ff.supprimer_lignes_na(data,nom_colonne).reset_index(drop=True)
if comparedf(data,datasol):
    print("supprimer_lignes_na OK")
else:
    print("!!!!supprimer_lignes_na ERREUR!!!!")
data = creedfexemple(1)
data1=ff.supprimer_lignes_na(data,nom_colonnefictive).reset_index(drop=True)
if comparedf(data,data1):
    print("")
else:
    print("!!!!supprimer_lignes_na ne gère pas les colonnes fictives!!!!")



#remplacer_valeurs
data = creedfexemple(1)
datasol = pd.DataFrame({'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                     'Âge': [25, 30, None, 22, 28],
                     'Ville': ['Paris', 'Dunkerque', 'Los Angeles', None, 'Berlin'],
                     'Salaire': [50000, None, 60000, None, 75000],
                     'Ville2': ['Paris', 'New York', 'Los Angeles', None, 'Berlin']})
nom_colonne = 'Ville'
valeur_a = 'New York'
valeur_b = 'Dunkerque' #miskine
data=ff.remplacer_valeurs(data, nom_colonne, valeur_a, valeur_b).reset_index(drop=True)

if comparedf(data,datasol):
    print("remplacer_valeurs OK")
else:
    print("!!!!remplacer_valeurs ERREUR!!!!")
data = creedfexemple(1)
data1=ff.remplacer_valeurs(data, nom_colonnefictive, valeur_a, valeur_b).reset_index(drop=True)
if comparedf(data,data1):
    print("")
else:
    print("!!!!remplacer_valeurs ne gère pas les colonnes fictives!!!!")


#scinde_colonnes
data = creedfexemple(2)
datasol = pd.DataFrame({'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                     'Âge': [25, 30, None, 22, 28],
                     'Ville': ['Paris', 'New York', 'Los Angeles', None, 'Berlin'],
                     'Salaire': [50000, None, 60000, None, 75000],
                     'Passions lecture':[1,0,0,None,0],
                     'Passions cuisine':[1,1,0,None,0],
                     'Passions sport':[1,1,0,None,1],
                     'Passions manga':[0,0,1,None,0],
                     'Passions informatique':[0,0,1,None,0],
                     'Passions dessin':[0,1,0,None,0]
                     })
nom_colonne = 'Passions'
noms_colonnes_personnalisees = ['lecture', 'cuisine', 'sport',
                                'manga', 'informatique', 'dessin']


data=ff.scinde_colonnes(data, nom_colonne, noms_colonnes_personnalisees).reset_index(drop=True)
if comparedf(data,datasol):
    print("scinde_colonnes OK")
else:
    print("!!!!scinde_colonnes ERREUR!!!!")

data1=ff.scinde_colonnes(data, nom_colonnefictive, noms_colonnes_personnalisees)
if comparedf(data,data1):
    print("")
else:
    print("!!!!scinde_colonnes ne gère pas les colonnes fictives!!!!")



    
#compter_virgules
chaine1="tito,toto,teuteu,tata,,,virgule balhblahvlah"
chaine2="il n'y a pas de virgules"
chaine3=None 
nb1=6
nb2=0
nb3=None
if ff.compter_virgules(chaine1) != 7:
    print("!!!!compter_virgule ERREUR1!!!!")
elif ff.compter_virgules(chaine2) != 1:
    print("!!!!compter_virgule ERREUR2!!!!")
elif not np.isnan(ff.compter_virgules(chaine3)):
    print("!!!!compter_virgule ERREUR3!!!!")
else:
    print("compter_virgules OK")
    
    
#convertir_listes_en_nombre
data = creedfexemple(2)
datasol = pd.DataFrame({'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                     'Âge': [25, 30, None, 22, 28],
                     'Ville': ['Paris', 'New York', 'Los Angeles', None, 'Berlin'],
                     'Salaire': [50000, None, 60000, None, 75000],
                     'Passions': [3, 
                                  3, 
                                  3, 
                                  None, 
                                  1]})
nom_colonne = "Passions"
data=ff.convertir_listes_en_nombre(data, nom_colonne).reset_index(drop=True)
if comparedf(data,datasol):
    print("convertir_listes_en_nombre OK")
else:
    print("!!!!convertir_listes_en_nombre ERREUR!!!!")


data1=ff.convertir_listes_en_nombre(data, nom_colonnefictive)
if comparedf(data,data1):
    print("")
else:
    print("!!!!convertir_listes_en_nombre ne gère pas les colonnes fictives!!!!")

    
#selectionner_colonnes
data = creedfexemple(1)
datasol = pd.DataFrame({'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                     'Ville': ['Paris', 'New York', 'Los Angeles', None, 'Berlin'],
                     'Salaire': [50000, None, 60000, None, 75000],
                     })
colonnes_a_garder = ['Nom', 'Ville', 'Salaire']

data=ff.selectionner_colonnes(data, colonnes_a_garder).reset_index(drop=True)
if comparedf(data,datasol):
    print("selectionner_colonnes OK")
else:
    print("!!!!selectionner_colonnes ERREUR!!!!")    

    
    
#deplacer_colonne_en_premier(df, nom_colonne)
data = creedfexemple(1)
datasol = pd.DataFrame({'Salaire': [50000, None, 60000, None, 75000],
                     'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                     'Âge': [25, 30, None, 22, 28],
                     'Ville': ['Paris', 'New York', 'Los Angeles', None, 'Berlin'],
                     'Ville2': ['Paris', 'New York', 'Los Angeles', None, 'Berlin']}) 
nom_colonne = "Salaire"
data=ff.deplacer_colonne_en_premier(data, nom_colonne).reset_index(drop=True)
if comparedf(data,datasol):
    print("deplacer_colonne_en_premier OK")
else:
    print("!!!!deplacer_colonne_en_premier ERREUR!!!!")    
    


data1=ff.deplacer_colonne_en_premier(data, nom_colonnefictive)
if comparedf(data,data1):
    print("")
else:
    print("!!!!deplacer_colonne_en_premier ne gère pas les colonnes fictives!!!!")

    
    
#remplacer_na_par_valeur
data = creedfexemple(1)
datasol = pd.DataFrame({'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                     'Âge': [25, 30, 'inconnu', 22, 28],
                     'Ville': ['Paris', 'New York', 'Los Angeles', None, 'Berlin'],
                     'Salaire': [50000, None, 60000, None, 75000],
                     'Ville2': ['Paris', 'New York', 'Los Angeles', None, 'Berlin']})
nom_colonne = 'Âge'
valeur_remplacement = 'inconnu'
data=ff.remplacer_na_par_valeur(data, nom_colonne, valeur_remplacement).reset_index(drop=True)
if comparedf(data,datasol):
    print("remplacer_na_par_valeur OK")
else:
    print("!!!!remplacer_na_par_valeur ERREUR!!!!")  
    
data1=ff.remplacer_na_par_valeur(data, nom_colonnefictive, valeur_remplacement).reset_index(drop=True)
if comparedf(data,data1):
    print("")
else:
    print("!!!!remplacer_na_par_valeur ne gère pas les colonnes fictives!!!!")    
    


#count_na_per_column
data = creedfexemple(1)
datasol = pd.DataFrame({'Column': ['Nom', 'Âge', 'Ville', 'Salaire', 'Ville2'],
                     'NA_Count': [0, 1, 1, 2, 1]})


data=ff.count_na_per_column(data).reset_index(drop=True)
if comparedf(data,datasol):
    print("count_na_per_column OK")
else:
    print("!!!!count_na_per_column ERREUR!!!!")  
    

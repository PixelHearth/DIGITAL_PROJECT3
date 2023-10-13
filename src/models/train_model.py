from sklearn.neighbors import KNeighborsClassifier

def k_neighbors(dataframe,new_variable):
    """ création d'un algorithme de k_neighbors sur les données properties
    parameter "dataframe", est le dataframe de l'ademe nettoyé
    """
    neigh = KNeighborsClassifier(n_neighbors=5)
    
    Dependent_variable = dataframe.iloc[0].values
    independent_variable = dataframe.iloc[:,[0,1]].values
    #entrainement des données
    neigh.fit(independent_variable,Dependent_variable)

    #création d'un individu afin de déterminer son dpe à remplir avec le formulaire vba
    prediction = neigh.predict(new_variable)


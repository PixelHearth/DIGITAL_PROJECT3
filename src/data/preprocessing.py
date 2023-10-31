from sklearn.preprocessing import OrdinalEncoder   
class CustomPreprocessor:
    """ 
    fait un encodage des variables string en variables ordinales
    """
    def __init__(self,dataframe):
        """
        Initialise un objet CustomPreprocessor.

        Parameters:
        dataframe (pandas.DataFrame): Le DataFrame contenant les données à prétraiter.

        Attributes:
        encoder (OrdinalEncoder): L'encodeur qui transforme les valeurs de type chaîne en valeurs ordinales.
        dataframe (pandas.DataFrame): Le DataFrame utilisé pour entraîner l'encodeur.
        indices (list): Une liste des indices des colonnes qui seront transformées en valeurs ordinales.
        object_columns (Index): Un index répertoriant les noms des colonnes considérées comme des objets (chaînes).

        """

        # chargement du modele d'encodage
        self.encoder = OrdinalEncoder()

        #dataframe à convertir, entrainer ou transformer
        self.dataframe = dataframe

        #  on garde les colonnes qui sont types Objets
        self.object_columns = dataframe.select_dtypes(include=['object']).columns
        
        # liste des noms des colonnes object
        self.indices = [column for column in (dataframe.columns) if column in self.object_columns]

        # liste ordonnées des valeurs  au sein des colonnes 
        self.unique_values = [sorted(list(set(self.dataframe[col])) ) for col in self.object_columns]
        
        #dictionnaires avec titre de la colonnes, les valeurs uniques au sein de la colonne ordonnées avec leur index correspondants
        self.inverse_encoder = {index: {j: v for j, v in enumerate(values)}
                                 for (index, values) in zip(self.indices, self.unique_values)}


    def fit(self):
        """
        permet d'entrainer l'encodeur sur le dataframe de la classe
        """
                
        self.encoder.fit(self.dataframe[self.object_columns])

    def transform(self,df_to_transform):
        """
        Transforme un DataFrame en utilisant l'entraînement effectué sur la base de données de la classe.

        Parameters:
        df_to_transform (pandas.DataFrame): Le DataFrame à transformer.
        """

        df_to_transform[self.object_columns] = self.encoder.transform(df_to_transform[self.object_columns])
        return df_to_transform
    
    def inverse_transform(self,df_test):
        """
        Effectue la transformation inverse en utilisant l'encodeur.

        Parameters:
        df_test (pandas.DataFrame): Le DataFrame à transformer inversement.

        Returns:
        pandas.DataFrame: Le DataFrame avec la transformation inverse appliquée.
        """

        # On vérifie que notre dictionnaire inverse_encoder est pas vide, le 
        if self.inverse_encoder is not None:
            for col_name in self.indices:
                if col_name in df_test.columns:
                    df_test[col_name] = df_test[col_name].map(self.inverse_encoder[col_name])

        return df_test
    
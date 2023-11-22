from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def scaler(df):
    if isinstance(df, pd.DataFrame):
        raise TypeError("the input must be a dataframe")
    # Extraction des valeurs du DataFrame
    values = df.values

    # Création d'un objet scaler
    scaler = MinMaxScaler()

    # Normalisation des données
    normalized_values = scaler.fit_transform(values)

    # Création d'un nouveau DataFrame avec les données normalisées
    normalized_data = pd.DataFrame(normalized_values, columns=df.columns)

    print("Données d'origine :\n", df)
    print("\nDonnées normalisées :\n", normalized_data)

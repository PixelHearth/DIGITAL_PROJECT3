
import matplotlib.pyplot as plt
def plot_feature_importance(importances_df, nb_feature):
    """
    Crée un graphique à barres montrant l'importance des caractéristiques dans un modèle.

    Args:
        importances_df (DataFrame): Le DataFrame contenant les informations sur l'importance des caractéristiques.
        nb_feature (int): Le nombre de caractéristiques à inclure dans le graphique en fonction de leur importance.

    Returns:
        None

    Ce graphique affiche l'importance des caractéristiques dans un modèle. Les caractéristiques sont affichées sur l'axe des x
    et leur importance sur l'axe des y. Le pourcentage total d'importance représenté par les caractéristiques les plus
    importantes est également indiqué.

    Args:
        importances_df (DataFrame): Le DataFrame contenant les informations sur l'importance des caractéristiques.
        nb_feature (int): Le nombre de caractéristiques à inclure dans le graphique en fonction de leur importance.

    Returns:
        None
    """
    # Créer le graphique à barres
    plt.figure(figsize=(10, 6))
    
    # Triez le DataFrame par importance et prenez les 10 premières caractéristiques
    top_importances_df = importances_df.sort_values(by='Importance', ascending=False).head(nb_feature)
    
    plt.bar(top_importances_df['Feature'], top_importances_df['Importance'], color='b')

    # Titre du graphique, Nom des axes
    plt.xlabel('Caractéristique')
    plt.ylabel('Importance')
    plt.title('Importance des Caractéristiques dans le Modèle Random Forest')

    # Lisibilité du graphique
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Calcul du pourcentage total d'importance représenté par les caractéristiques les plus importantes
    total_importance = importances_df['Importance'].sum()
    top_features_importance = top_importances_df['Importance'].sum()
    percentage = (top_features_importance / total_importance) * 100

    # Ajout du texte indiquant le pourcentage total d'importance représenté par les caractéristiques les plus importantes
    plt.annotate(f"Top {nb_feature} Features: {percentage:.2f}%", xy=(0.5, 0.9), xycoords='axes fraction')
    plt.savefig("report/features_importance.png")


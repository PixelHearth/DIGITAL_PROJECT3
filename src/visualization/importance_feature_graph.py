import matplotlib.pyplot as plt
import pandas as pd

def plot_feature_importance(importances_df, nb_feature):
    """
    This chart displays the importance of features in a model. Features are shown on the x-axis,
    and their importance on the y-axis. The total percentage of importance represented by the
    most important features is also indicated.

    Args:
        importances_df (DataFrame): The DataFrame containing information about feature importance.
        nb_feature (int): The number of features to include in the chart based on their importance.

    Returns:
        A chart in docs with features selected
    """
    # Create the bar chart
    plt.figure(figsize=(10, 6))
    
    # Sort the DataFrame by importance and take the top 'nb_feature' features
    top_importances_df = importances_df.sort_values(by='Importance', ascending=False).head(nb_feature)
    
    plt.bar(top_importances_df['Feature'], top_importances_df['Importance'], color='b')

    # Chart title, axis labels
    plt.xlabel('Feature')
    plt.ylabel('Importance')
    plt.title('Feature Importance in the Random Forest Model')

    # Improve chart readability
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Add text indicating the total percentage of importance represented by the most important features
    plt.savefig("docs/features_importance.png")

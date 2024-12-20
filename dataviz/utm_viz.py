"""
Script: utm_viz.py
Description: Functions for visualizing UTM data trends and metrics.
"""

# TAG: DataViz, UTM Visualization, SaaS
import matplotlib.pyplot as plt
import seaborn as sns

def plot_traffic_trends(df):
    """Plots traffic trends by UTM source."""
    traffic = df.groupby(['utm_source', 'date'])['user_id'].count().reset_index()
    sns.lineplot(data=traffic, x='date', y='user_id', hue='utm_source')
    plt.title('Traffic Trends by UTM Source')
    plt.show()

def plot_retention(df):
    """Visualizes retention periods."""
    sns.boxplot(data=df, x='utm_campaign', y='retention_period')
    plt.title('Retention Analysis by Campaign')
    plt.show()

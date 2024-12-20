"""
Script: utm_analysis.py
Description: Functions for exploratory data analysis of UTM parameters.
"""

# TAG: EDA, UTM Analysis, SaaS
import pandas as pd

def summarize_utm(df):
    """Summarizes UTM parameter performance."""
    return df.groupby(['utm_source', 'utm_medium', 'utm_campaign']).agg({
        'user_id': 'nunique',
        'revenue': 'sum'
    }).reset_index()

def retention_analysis(df):
    """Analyzes retention trends."""
    df['retention_period'] = (df['last_active'] - df['signup_date']).dt.days
    return df.groupby('utm_campaign')['retention_period'].mean()

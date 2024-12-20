"""
Script: utm_features.py
Description: Functions for feature extraction and encoding UTM parameters.
"""

# TAG: Feature Engineering, UTM Parameters, SaaS
import pandas as pd

def encode_utm_parameters(df):
    """Encodes UTM parameters into numerical features."""
    for col in ['utm_source', 'utm_medium', 'utm_campaign']:
        df[col] = df[col].astype('category').cat.codes
    return df

def extract_utm_details(df):
    """Extracts additional details from UTM campaigns."""
    df['campaign_length'] = df['utm_campaign'].apply(len)
    return df

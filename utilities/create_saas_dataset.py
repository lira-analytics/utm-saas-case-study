# TAG: Data Creation | Dataset Generation
# This script generates a synthetic dataset for a SaaS company analysis.
# The data includes UTM parameters, customer behavior, and subscription details.

import pandas as pd
import random
import numpy as np

# Set a random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the dataset structure
num_records = 100
data = {
    "customer_id": [f"CUST-{i+1:03}" for i in range(num_records)],
    "utm_source": random.choices(["facebook", "google", "linkedin", "twitter", "email"], k=num_records),
    "utm_medium": random.choices(["cpc", "organic", "referral", "email"], k=num_records),
    "utm_campaign": random.choices(["brand-awareness", "product-launch", "discount-offer"], k=num_records),
    "utm_term": random.choices(["keyword1", "keyword2", "keyword3"], k=num_records),
    "utm_content": random.choices(["ad1", "ad2", "ad3"], k=num_records),
    "subscription_start_date": pd.date_range(start="2023-01-01", periods=num_records).tolist(),
    "subscription_end_date": pd.date_range(start="2023-04-01", periods=num_records).tolist(),
    "monthly_revenue": np.random.randint(20, 200, size=num_records),
    "login_frequency": np.random.randint(1, 30, size=num_records),
    "feature_usage": np.random.randint(1, 50, size=num_records),
}

# Convert to a DataFrame
saas_data = pd.DataFrame(data)

# Save to a CSV file for analysis
output_file = "data/saas_data.csv"
saas_data.to_csv(output_file, index=False)
print(f"Dataset created and saved to {output_file}")

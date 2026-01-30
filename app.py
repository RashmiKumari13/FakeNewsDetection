import pandas as pd

# Load datasets
fake = pd.read_csv('data/raw/Fake.csv')
true = pd.read_csv('data/raw/True.csv')

# Add labels
fake['label'] = 1
true['label'] = 0

# Merge and shuffle
df = pd.concat([fake, true]).reset_index(drop=True)
df = df.sample(frac=1).reset_index(drop=True) # Shuffle for better training

print(df.head())
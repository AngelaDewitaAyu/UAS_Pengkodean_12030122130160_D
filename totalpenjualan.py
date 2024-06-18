import pandas as pd

# Load the datasets
diskon_df = pd.read_csv('diskon.csv', sep=';')
influencer_df = pd.read_csv('influencer.csv', sep=';')
review_df = pd.read_csv('review.csv', sep=';')

# Convert 'Diskon' and 'Review (Bintang)' columns to numeric values
diskon_df['Diskon'] = diskon_df['Diskon'].str.replace('%', '').astype(float)
review_df['Review (Bintang)'] = review_df['Review (Bintang)'].str.replace(',', '.').astype(float)

# Calculate total unit penjualan from each dataset
total_unit_penjualan_diskon = diskon_df['Unit Penjualan'].sum()
total_unit_penjualan_review = review_df['Unit Penjualan'].sum()
total_unit_penjualan_influencer = influencer_df['Unit Penjualan'].sum()

# Calculate overall total unit penjualan
total_unit_penjualan = total_unit_penjualan_diskon + total_unit_penjualan_review + total_unit_penjualan_influencer
total_unit_penjualan

# Display the result
print(f"Total Unit Penjualan secara keseluruhan: {total_unit_penjualan}")

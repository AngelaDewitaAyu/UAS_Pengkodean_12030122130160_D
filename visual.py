import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
diskon_df = pd.read_csv('diskon.csv', sep=';')
influencer_df = pd.read_csv('influencer.csv', sep=';')
review_df = pd.read_csv('review.csv', sep=';')

# Convert 'Diskon' and 'Review (Bintang)' columns to numeric values
diskon_df['Diskon'] = diskon_df['Diskon'].str.replace('%', '').astype(float)
review_df['Review (Bintang)'] = review_df['Review (Bintang)'].str.replace(',', '.').astype(float)

# Scatter plot unit penjualan dan review
plt.figure(figsize=(10, 6))
sns.scatterplot(x=review_df['Unit Penjualan'], y=review_df['Review (Bintang)'])
plt.title('Scatter Plot of Unit Penjualan and Review')
plt.xlabel('Unit Penjualan')
plt.ylabel('Review (Bintang)')
plt.show()

# Scatter plot unit penjualan dan diskon
plt.figure(figsize=(10, 6))
sns.scatterplot(x=diskon_df['Unit Penjualan'], y=diskon_df['Diskon'])
plt.title('Scatter Plot of Unit Penjualan and Diskon')
plt.xlabel('Unit Penjualan')
plt.ylabel('Diskon (%)')
plt.show()

# Scatter plot unit penjualan dan jumlah followers
plt.figure(figsize=(10, 6))
sns.scatterplot(x=influencer_df['Unit Penjualan'], y=influencer_df['Jumlah Followers'])
plt.title('Scatter Plot of Unit Penjualan and Jumlah Followers')
plt.xlabel('Unit Penjualan')
plt.ylabel('Jumlah Followers')
plt.show()

# Bar chart unit penjualan, review, dan platform review
plt.figure(figsize=(10, 6))
sns.barplot(x='Platform Review', y='Unit Penjualan', hue='Review (Bintang)', data=review_df)
plt.title('Bar Chart of Unit Penjualan, Review, and Platform Review')
plt.xlabel('Platform Review')
plt.ylabel('Unit Penjualan')
plt.show()

# Bar chart unit penjualan, diskon, dan platform penjualan
plt.figure(figsize=(10, 6))
sns.barplot(x='Platform Penjualan', y='Unit Penjualan', hue='Diskon', data=diskon_df)
plt.title('Bar Chart of Unit Penjualan, Diskon, and Platform Penjualan')
plt.xlabel('Platform Penjualan')
plt.ylabel('Unit Penjualan')
plt.show()

# Bar chart unit penjualan dan jumlah followers
plt.figure(figsize=(10, 6))
sns.barplot(x='Nama Produk', y='Unit Penjualan', hue='Jumlah Followers', data=influencer_df)
plt.title('Bar Chart of Unit Penjualan and Jumlah Followers')
plt.xlabel('Nama Produk')
plt.ylabel('Unit Penjualan')
plt.xticks(rotation=45)
plt.show()

# Histogram unit penjualan
plt.figure(figsize=(10, 6))
sns.histplot(diskon_df['Unit Penjualan'], bins=10)
plt.title('Histogram of Unit Penjualan')
plt.xlabel('Unit Penjualan')
plt.ylabel('Frequency')
plt.show()

# Pie chart komposisi penjualan pada nama produk
plt.figure(figsize=(10, 6))
diskon_df.groupby('Nama Produk')['Unit Penjualan'].sum().plot.pie(autopct='%1.1f%%')
plt.title('Pie Chart of Penjualan by Nama Produk')
plt.ylabel('')
plt.show()

# Pie chart komposisi penjualan pada platform review
plt.figure(figsize=(10, 6))
review_df.groupby('Platform Review')['Unit Penjualan'].sum().plot.pie(autopct='%1.1f%%')
plt.title('Pie Chart of Penjualan by Platform Review')
plt.ylabel('')
plt.show()

# Pie chart komposisi penjualan pada platform penjualan
plt.figure(figsize=(10, 6))
diskon_df.groupby('Platform Penjualan')['Unit Penjualan'].sum().plot.pie(autopct='%1.1f%%')
plt.title('Pie Chart of Penjualan by Platform Penjualan')
plt.ylabel('')
plt.show()

# Heatmap (assuming a correlation matrix is desired from existing data)
plt.figure(figsize=(10, 6))
corr_matrix = diskon_df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Diskon Data')
plt.show()

# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
try:
    df = pd.read_csv("data/metadata.csv")
except FileNotFoundError:
    print("Error: metadata.csv not found. Place it in the data/ folder.")
    exit()

# Explore data
print(df.shape)
print(df.info())
print(df.isnull().sum())

# Clean data
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# Analysis
year_counts = df['year'].value_counts().sort_index()
top_journals = df['journal'].value_counts().head(10)

# --- Visualizations ---
# 1. Publications over time
plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.tight_layout()
plt.savefig("pubs_by_year.png")
plt.show()

# 2. Top journals
plt.figure(figsize=(10,6))
sns.barplot(y=top_journals.index, x=top_journals.values)
plt.title("Top 10 Journals")
plt.xlabel("Number of Publications")
plt.ylabel("Journal")
plt.tight_layout()
plt.savefig("top_journals.png")
plt.show()

# 3. Histogram of abstract word counts
plt.figure(figsize=(8,5))
plt.hist(df['abstract_word_count'], bins=50, color="skyblue")
plt.title("Distribution of Abstract Word Count")
plt.xlabel("Word Count")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("abstract_word_count.png")
plt.show()

# 4. Scatter plot: year vs abstract word count
plt.figure(figsize=(8,5))
plt.scatter(df['year'], df['abstract_word_count'], alpha=0.5)
plt.title("Abstract Word Count Over Years")
plt.xlabel("Year")
plt.ylabel("Word Count")
plt.tight_layout()
plt.savefig("scatter_year_wordcount.png")
plt.show()

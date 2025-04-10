import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load India trending videos dataset
df = pd.read_csv('INvideos.csv', encoding='ISO-8859-1')

# Basic info
print("Dataset Shape:", df.shape)
print(df.columns)

# Convert publish time to datetime
df['publishedAt'] = pd.to_datetime(df['publish_time']).dt.date

# Top 10 trending video titles
top_titles = df['title'].value_counts().head(10)
print("\nTop Trending Video Titles:\n", top_titles)

# Most frequent channels
top_channels = df['channel_title'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y=top_channels.index, x=top_channels.values, palette='mako')
plt.title('Top 10 Trending YouTube Channels in India')
plt.xlabel('Number of Trending Videos')
plt.ylabel('Channel Name')
plt.tight_layout()
plt.savefig('filename.png', dpi=300, bbox_inches='tight')

plt.show()

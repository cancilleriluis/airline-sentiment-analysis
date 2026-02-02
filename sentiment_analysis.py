import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load the dataset
df = pd.read_csv('Tweets.csv')  # Change filename if yours is different

# First look at the data
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())
print("\nSentiment distribution:")
print(df['airline_sentiment'].value_counts())

# Let's see some actual tweets from each sentiment
print("\n" + "="*50)
print("SAMPLE TWEETS:")
print("="*50)

print("\n--- POSITIVE TWEETS ---")
print(df[df['airline_sentiment'] == 'positive']['text'].head(3).tolist())

print("\n--- NEGATIVE TWEETS ---")
print(df[df['airline_sentiment'] == 'negative']['text'].head(3).tolist())

print("\n--- NEUTRAL TWEETS ---")
print(df[df['airline_sentiment'] == 'neutral']['text'].head(3).tolist())

# Let's see which airlines are in the dataset, I want to see if it's the real airlines names mentioned in the tweets or not.
print("\n" + "="*50)
print("AIRLINES IN DATASET:")
print("="*50)
print(df['airline'].value_counts())

# Let's see a few tweets with their airline label
print("\n" + "="*50)
print("SAMPLE: Tweet + Airline:")
print("="*50)
print(df[['text', 'airline', 'airline_sentiment']].head(10))

import re  # For pattern matching

# Function to clean tweets
def clean_tweet(tweet):
    # Remove @mentions
    tweet = re.sub(r'@\w+', '', tweet)
    
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+', '', tweet)
    
    # Remove special HTML characters like &amp;
    tweet = re.sub(r'&\w+;', '', tweet)
    
    # Remove extra spaces
    tweet = re.sub(r'\s+', ' ', tweet).strip()
    
    # Convert to lowercase
    tweet = tweet.lower()
    
    return tweet

# Create a new column with cleaned text
df['text_clean'] = df['text'].apply(clean_tweet)

# Let's compare original vs cleaned
print("\n" + "="*50)
print("BEFORE vs AFTER CLEANING:")
print("="*50)
for i in range(3):
    print(f"\nOriginal: {df['text'].iloc[i]}")
    print(f"Cleaned:  {df['text_clean'].iloc[i]}")

    import matplotlib.pyplot as plt

# Chart 1: Overall Sentiment Distribution
print("\n" + "="*50)
print("Creating visualizations...")
print("="*50)

# Count sentiments
sentiment_counts = df['airline_sentiment'].value_counts()

# Create the bar chart
plt.figure(figsize=(10, 6))  # Size of the chart
plt.bar(sentiment_counts.index, sentiment_counts.values, 
        color=['red', 'gray', 'green'])  # Colors for neg/neutral/pos
plt.title('Overall Airline Sentiment Distribution', fontsize=16)
plt.xlabel('Sentiment', fontsize=12)
plt.ylabel('Number of Tweets', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add count labels on top of bars
for i, v in enumerate(sentiment_counts.values):
    plt.text(i, v + 200, str(v), ha='center', fontsize=12, fontweight='bold')

plt.tight_layout()  # Makes sure everything fits nicely
plt.savefig('sentiment_distribution.png')  # Save the chart
plt.show()  # Display it

print("✅ Chart saved as 'sentiment_distribution.png'")

# Chart 2: Sentiment by Airline
plt.figure(figsize=(12, 6))

# Create data for grouped bar chart
airlines = df['airline'].unique()
negative_counts = []
neutral_counts = []
positive_counts = []

for airline in airlines:
    airline_data = df[df['airline'] == airline]
    negative_counts.append(len(airline_data[airline_data['airline_sentiment'] == 'negative']))
    neutral_counts.append(len(airline_data[airline_data['airline_sentiment'] == 'neutral']))
    positive_counts.append(len(airline_data[airline_data['airline_sentiment'] == 'positive']))

# Create positions for bars
x = range(len(airlines))
width = 0.25  # Width of each bar

# Create the grouped bars
plt.bar([i - width for i in x], negative_counts, width, label='Negative', color='red')
plt.bar(x, neutral_counts, width, label='Neutral', color='gray')
plt.bar([i + width for i in x], positive_counts, width, label='Positive', color='green')

plt.xlabel('Airline', fontsize=12)
plt.ylabel('Number of Tweets', fontsize=12)
plt.title('Sentiment Distribution by Airline', fontsize=16)
plt.xticks(x, airlines, rotation=45)  # Rotate airline names so they fit
plt.legend()
plt.tight_layout()
plt.savefig('sentiment_by_airline.png')
plt.show()

print("✅ Chart saved as 'sentiment_by_airline.png'")


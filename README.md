# Airline Sentiment Analysis

Analyzed 14,640 tweets about US airlines to understand customer sentiment patterns and identify key complaint areas.

## Key Findings

- 63% of tweets are negative — airlines face significant customer dissatisfaction
- United Airlines received the most mentions (3,822 tweets)
- Virgin America has the smallest sample size (504 tweets)
- Negative sentiment dominates across all major US carriers

## Project Structure

```
airline_sentiment_analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── sentiment_analysis.py
├── data/
│   ├── Tweets.csv
│   └── database.sqlite
├── outputs/
│   ├── sentiment_distribution.png
│   └── sentiment_by_airline.png
└── notebooks/
```

## Tech Stack

- Python 3.x
- pandas — Data manipulation
- matplotlib — Data visualization
- TextBlob — Sentiment analysis
- re (regex) — Text cleaning

## Visualizations

### Overall Sentiment Distribution
![Sentiment Distribution](outputs/sentiment_distribution.png)

### Sentiment by Airline
![Sentiment by Airline](outputs/sentiment_by_airline.png)

## How to Run

```bash
pip install -r requirements.txt
python sentiment_analysis.py
```

## Dataset

**Source:** [Twitter US Airline Sentiment Dataset](https://www.kaggle.com/crowdflower/twitter-airline-sentiment) from Kaggle

- 14,640 tweets
- Airlines: United, US Airways, American, Southwest, Delta, Virgin America
- Period: February 2015

## Analysis Steps

1. Data Loading — Import and explore the dataset
2. Data Cleaning — Remove @mentions, URLs, special characters
3. Sentiment Analysis — Count and categorize tweets by sentiment
4. Visualization — Create charts showing patterns
5. Insights — Identify key trends and findings

## Future Improvements

- Word cloud analysis of common complaint terms
- Time-series analysis of sentiment trends
- Machine learning model to predict sentiment
- Topic modeling to categorize complaint types

## Author

**Luis** — Account Manager & Data Analyst
Based in Galicia, Spain

## License

This project is open source and available for educational purposes.

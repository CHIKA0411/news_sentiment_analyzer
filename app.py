import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# get headlines
from scraper import scrape_ndtv
from sentiment import analyze_sentiment

headlines=scrape_ndtv()
df= pd.DataFrame({'Headline': headlines})
df['Sentiment']=df['Headline'].apply(analyze_sentiment)
df['Headline'].apply(analyze_sentiment)

print(df.head())

sns.countplot(x='Sentiment', data=df, hue='Sentiment', palette='Set2', legend=False)
plt.title("Sentiment Distribution of NDTV Headlines")
plt.xlabel("Sentiment")
plt.ylabel("Number of Headlines")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

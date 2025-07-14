import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scraper import scrape_ndtv
from sentiment import analyze_sentiment
from wordcloud import WordCloud
import datetime
st.caption(f"Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Set Streamlit config
st.set_page_config(page_title="News Sentiment Dashboard", layout="wide")

st.title("📰 NDTV News Sentiment Analyzer")
# Auto-refresh every 60 seconds (can change to 3000 for 3 sec, etc.)
st_autorefresh(interval=60000, key="datarefresh")
if st.button("🔄 Refresh News Headlines"):
    st.rerun()

# Scrape headlines
with st.spinner("Scraping headlines..."):
    headlines = scrape_ndtv()

# Analyze sentiment
df = pd.DataFrame({'Headline': headlines})
df['Sentiment'] = df['Headline'].apply(analyze_sentiment)

# Display table
st.subheader("📋 Latest Headlines with Sentiment")
st.dataframe(df)

# Bar chart
st.subheader("📊 Sentiment Distribution")
fig, ax = plt.subplots()
sns.countplot(x='Sentiment', data=df, palette='Set2', ax=ax)
st.pyplot(fig)

# Pie chart
st.subheader("🧁 Sentiment Proportion")
pie_data = df['Sentiment'].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', colors=sns.color_palette('Set2'))
st.pyplot(fig2)

# Word Cloud
st.subheader("☁️ Word Cloud (All Headlines)")
all_text = " ".join(df['Headline'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

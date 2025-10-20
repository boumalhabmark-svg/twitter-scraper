# scrape.py
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

# 👇 Change your target account here
query = "from:MTVLebanon since:2025-10-01"

tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= 1000:
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.url])

df = pd.DataFrame(tweets, columns=["Date", "User", "Text", "URL"])

# 👇 Save with a timestamped filename
date_str = datetime.now().strftime("%Y-%m-%d")
df.to_csv(f"tweets_{date_str}.csv", index=False)

print(f"✅ Saved {len(df)} tweets to tweets_{date_str}.csv")

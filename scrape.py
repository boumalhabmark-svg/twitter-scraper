import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

# Change the account or search terms here
query = "from:MTVLebanon since:2025-10-01"

tweets = []
limit = 100

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i > limit:
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.url])

df = pd.DataFrame(tweets, columns=["Date", "User", "Text", "URL"])
df.to_csv("tweets.csv", index=False)

print(f"Saved {len(df)} tweets to tweets.csv at {datetime.now()}")

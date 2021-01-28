import twint

tw = twint.Config()

tw.Search = "couvrefeu OR reconfinement OR confinement"
tw.Since = "2021-01-01 12:00:00"
tw.Custom["tweet"] = ["id"]
tw.Pandas = True
tw.Lang = "fr"

twint.run.Search(tw)
tweet = twint.storage.panda.Tweets_df

tweet.to_csv('tweet_covid.csv')


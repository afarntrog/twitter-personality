from textblob import TextBlob 
import twint

# Short script to see a twitter users 'online personality'. This is not meant to be comprehensive!

def get_tweets():
    c = twint.Config()
    c.Username = "ENTER USER NAME HERE"
    c.Store_object = True 

    # get the tweets - they will be stored
    twint.run.Search(c)

    # stored tweets
    tweets_as_objects = twint.output.tweets_list
    tweet_list = []
    for tweet in tweets_as_objects:
        try:
            tweet_list.append( tweet.tweet )
        except:
            pass
    return tweet_list

def get_tweet_sentiment(): 
    ''' 
    Utility function to classify sentiment of passed tweet 
    using textblob's sentiment method 
    '''

    # Get tweets and store list.
    tweets = get_tweets()

    neg = 0
    pos = 0
    neutral = 0

    for tweet in tweets:
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(tweet[0]) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            pos += 1
        elif analysis.sentiment.polarity == 0: 
            neutral += 1
        else: 
            neg += 1

    total_tweets = neg + pos + neutral
    print(f'{total_tweets} tweets were analyzed. {neg} were negative, {pos} were positive and {neutral} were neutral')
    print(f"The negative percentage is {((neg/total_tweets) * 100) if neg > 0 else 0}")
    print(f"The positive percentage is {((pos/total_tweets) * 100) if pos > 0 else 0}")
    print(f"The neutral percentage is {((neutral/total_tweets) * 100) if neutral > 0 else 0}")



get_tweet_sentiment()

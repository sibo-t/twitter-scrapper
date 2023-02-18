import unittest
import Tweet
import datetime

class TestTweet(unittest.TestCase):

    def test_create_tweet(self):
        tweet_date = datetime.date(2023, 2, 18)
        tweet = Tweet.Tweet(tweet_date, "Hello, world!", "@Sibonelo")
        self.assertEqual(tweet.getDate(), tweet_date)
        self.assertEqual(tweet.getMessage(), "Hello, world!")
        self.assertEqual(tweet.getAuthor(), "@Sibonelo")

    def test_compare_same_tweets(self):
        tweet_date = datetime.date(2023, 2, 18)
        msg = "Hello, world!"
        aut =  "@Sibonelo"
        tweet = Tweet.Tweet(tweet_date, msg, aut)
        tweet2 = Tweet.Tweet(tweet_date, msg, aut)
        self.assertEqual(tweet, tweet2)

    def test_compare_diff_tweets(self):
        tweet_date = datetime.date(2023, 2, 18)
        msg = "Hello, world!"
        msg2 = "Bye, world!"
        aut =  "@Sibonelo"
        tweet = Tweet.Tweet(tweet_date, msg, aut)
        tweet2 = Tweet.Tweet(tweet_date, msg2, aut)
        self.assertNotEqual(tweet, tweet2)

        


if __name__ == '__main__':
    unittest.main()
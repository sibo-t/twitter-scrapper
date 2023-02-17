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


if __name__ == '__main__':
    unittest.main()
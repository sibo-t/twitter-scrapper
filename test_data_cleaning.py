import unittest
import data_cleaning


class TestDataCleaning(unittest.TestCase):
    
    def test_correct_formatted_date_to_datetime(self):
        the_date = "May 16, 2019"
        date_not_found = True
        date_not_found, new_datetime = data_cleaning.convert_date(the_date)
        correct_datetime = data_cleaning.datetime.datetime(2019, 5, 16)
        self.assertEqual(correct_datetime, new_datetime)
        self.assertFalse(date_not_found)

    def test_correct_formatted_date2_to_datetime(self):
        the_date = "Jan 06, 2019"
        date_not_found = True
        date_not_found, new_datetime = data_cleaning.convert_date(the_date)
        correct_datetime = data_cleaning.datetime.datetime(2019, 1, 6)
        self.assertEqual(correct_datetime, new_datetime)
        self.assertFalse(date_not_found)

    def test_incorrect_formatted_date_to_datetime(self):
        the_date = "16 May 2019"
        date_not_found = True
        date_not_found, new_datetime = data_cleaning.convert_date(the_date)
        correct_datetime = None
        self.assertEqual(correct_datetime, new_datetime)
        self.assertTrue(date_not_found)

    def test_incorrect_formatted_date2_to_datetime(self):
        the_date = "May 2019"
        date_not_found = True
        date_not_found, new_datetime = data_cleaning.convert_date(the_date)
        correct_datetime = None
        self.assertEqual(correct_datetime, new_datetime)
        self.assertTrue(date_not_found)

    ##############################################################################################
    ###                                                                                        ###
    ###                           Retrieve tweet message                                       ###
    ##############################################################################################

    def test_retrieve_tweet_message(self):
        tweet_msg = "Hello, world!\n"
        look_f_msg, retrieved_msg = data_cleaning.retrieve_msg(tweet_msg)
        self.assertEqual("Hello, world!", retrieved_msg)
        self.assertFalse(look_f_msg)

    def test_retrieve_tweet2_message(self):
        tweet_msg = "Hello, world!"
        look_f_msg, retrieved_msg = data_cleaning.retrieve_msg(tweet_msg)
        self.assertEqual("Hello, world!", retrieved_msg)
        self.assertFalse(look_f_msg)

    ##############################################################################################
    ###                                                                                        ###
    ###                           Retrieve tweet's author                                      ###
    ##############################################################################################

    def test_retrieve_tweets_author(self):
        tweet_aut = "@MsabalaSibonelo\n"
        look_f_aut, retrieved_aut = data_cleaning.retrieve_aut(tweet_aut)
        self.assertEqual("@MsabalaSibonelo", retrieved_aut)
        self.assertFalse(look_f_aut)

    def test_retrieve_tweet2_author(self):
        tweet_aut = "@MsabalaSibonelo"
        look_f_aut, retrieved_aut = data_cleaning.retrieve_msg(tweet_aut)
        self.assertEqual("@MsabalaSibonelo", retrieved_aut)
        self.assertFalse(look_f_aut)

    def test_retrieve_tweets_author_incorrect(self):
        tweet_aut = "MsabalaSibonelo\n"
        look_f_aut, retrieved_aut = data_cleaning.retrieve_aut(tweet_aut)
        self.assertEqual(None, retrieved_aut)
        self.assertTrue(look_f_aut)

    def test_retrieve_tweet2_author_incorrect(self):
        tweet_aut = "123MsabalaSibonelo"
        look_f_aut, retrieved_aut = data_cleaning.retrieve_aut(tweet_aut)
        self.assertEqual(None, retrieved_aut)
        self.assertTrue(look_f_aut)



if __name__ == '__main__':
    unittest.main()
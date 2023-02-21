"""
Twitter-scraper

    Author : Sibonelo Msabala
    Email  : stmsabala@gmail.com
    Summary: This is an attempt to gather large data on a topic from Twitter using Selenium
             and other tools.
             Data is extracted from Twitter, cleaned (transformed) into understandable date and
             finally loaded into a database
"""
import database
from search import run
from data_cleaning import retrieve_raw_tweets


def generate_dump(topic, tweet_count):
    """Will search for tweets under that specific topic

    Args:
        topic (str): _description_
        tweet_count (int): _description_
    """
    run(tweet_count,topic)
    print("Twitter dump created on this topic "+topic)


def clean_n_store_data(dump, db):
    """Reads the raw data and extracts a tweet's date, message and author, everything
       is stored in the database

    Args:
        dump (txt): Twitter raw data
        db (_type_): Database used to store cleaned data
    """
    retrieve_raw_tweets(dump, db)
    print("Tweet are now stored in the database!!!")


def initialise_db(db_name, topic):
    """Creates a mongodb database with a specific name and topic is the collection for the data
        scraped

    Args:
        db_name (str): The name of the database to be created
        topic (str): The collection of the scraped data
    """
    database.create_database(db_name)
    database.create_collection(topic)
    print("Database initialised!!!")


if __name__ == '__main__':
    print("Greetings, new user!")
    topic = input("What topic are you interested in collecting data on: ")
    count = int(input("How many unique tweets are you interest in: "))
    initialise_db("Twitter", topic)
    generate_dump(topic, count)
    clean_n_store_data("tweetdump.txt",database)
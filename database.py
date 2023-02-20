"""
    Module to perform CRUD operations on a mongoDB
"""

import pymongo

_myclient = pymongo.MongoClient("mongodb://localhost:27017/")
_mydb = None
_subject = None


def create_database(name):
    """Creates a mongoDB with the specified name

    Args:
        name (String): Name of the database
    """
    global _mydb
    _mydb = _myclient[name]
    return True


def create_collection(search_word):
    """Create a collection for the tweets based on the search string used

    Args:
        search_word (String): String used to generate the tweets scraped
    """
    global _subject
    _subject = _mydb[search_word]
    return True


def insert_tweet(id, date, msg, aut):
    """Insert the tweet

    Args:
        id (int): The tweets position in the database
        date (datetime): The date of the tweet
        msg (String): The message of the tweet
        aut (String): The author of the tweet
    """
    tweet = {"id":id, "date":date, "message":msg, "author":aut}
    _subject.insert_one(tweet)
    return True


def retrieve_tweet(id):
    """Retrieve all tweets for that subject

    Args:
        search_word (String): Retrieve all tweets under this subject
    """
    query = {'id': id}
    return _subject.find(query)[0]
    

def count_tweets(search_word):
    """Count number of tweets under that catergory

    Args:
        search_word (String): count all tweets under this subject
    """
    
    return _mydb[search_word].count_documents({})


def delete_all_tweets(search_word):
    """Delete all tweets under that catergory

    Args:
        search_word (String): delete all tweets under this subject
    """
    query = {'id': id}
    return _subject.delete_many(query)

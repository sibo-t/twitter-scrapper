"""
A module to clean raw twitter data collected
                    functions:
                                * retrieve_raw_tweets(tweet_dump)(String) - Returns a 
                                list of unique Tweet onjects
                                * 
"""
import Tweet
from collections import deque
from calendar import month_abbr
import datetime


def retrieve_raw_tweets(tweet_dump):

    tweet_deque = deque()
    look_f_date = True
    look_f_msg = True
    look_f_aut = True
    tweet_date = None
    tweet_msg= ""
    tweet_aut = ""

    with open(tweet_dump) as file:
        for line in file:
            if look_f_date:
                look_f_date, tweet_date = convert_date(line)
                continue
            if look_f_msg:
                look_f_msg, tweet_msg = retrieve_msg(line)
                continue
            if look_f_aut:
                look_f_aut, tweet_aut = retrieve_aut(line)
                continue
            

def convert_date(the_date):
    """Convert date 'mm dd, yyyy' to datetime yyyy/mm/dd. If it cannot be converted throw exception
    and return (True,None) else return (False, new_datetime)

    Args:
        the_date (String): Line containing the date to be converted to datetime
    """
    try:
        removed_comma_date = the_date.replace(',', '').split(' ')
        year = int(removed_comma_date[2])
        month = list(month_abbr).index(removed_comma_date[0])
        day =  int(removed_comma_date[1])
        new_datetime = datetime.datetime(year, month, day)
        return False, new_datetime
    except:
        return True, None


def retrieve_msg(msg):
    """Returns text line

    Args:
        msg (String): Text line representing tweet message
    """
    return False, msg.replace('\n','')


def retrieve_aut(aut):
    """Returns the tweet's author
    a tweet's author must start with char '@'

    Args:
        aut (String): Text line representing the tweet's author
    """
    f_char = aut[0]
    if  f_char == '@' and not f_char.isdigit():
        return False, aut.replace('\n','')
    return True, None

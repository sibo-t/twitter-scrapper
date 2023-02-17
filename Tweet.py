""""
Create a tweet object
            Properties:
                    * _DATE (Datetime)
                    * _MSG  (String)
                    * _AUT  (String)

            Methods:
                    * __eq__() (Boolean) - Compares 2 Tweet objects
                    * getDate (Datetime) - Returns the date of the tweet
                    * getMessage(String) - Returns the message of the Tweet
                    * getAuthor (String) - Returns the author's Twitter handle
"""
import datetime


class Tweet:

    def __init__(self, date, msg, aut):
        self._DATE = date
        self._MSG = msg
        self._AUT = aut

    def getDate(self):
        return self._DATE

    def getMessage(self):
        return self._MSG

    def getAuthor(self):
        return self._AUT
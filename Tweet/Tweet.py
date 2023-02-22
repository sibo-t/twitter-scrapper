""""
Create a tweet object
            Properties:
                    * _DATE (Datetime)
                    * _MSG  (String)
                    * _AUT  (String)

            Methods:
                    * __eq__() (Tweet) - Compares 2 Tweet objects (Boolean)
                    * getDate() - Returns the date of the tweet (Datetime)
                    * getMessage() - Returns the message of the Tweet (String)
                    * getAuthor() - Returns the author's Twitter handle (String)
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

    def __eq__(self, other):
        return (self._AUT == other._AUT ) and (self._MSG == other._MSG ) and (self._DATE == other._DATE )
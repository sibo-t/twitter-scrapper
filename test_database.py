import unittest
import DB.database as database

class TestDatabase(unittest.TestCase):

    def test_database_creation(self):
        database.create_database("test")
        database.create_collection("test_collection")
        database.insert_tweet(1,"2023/02/20", "Hello, world!","@MsabalaSibonelo")

        self.assertEquals("test", database._mydb.name)
        self.assertTrue("test" in database._myclient.list_database_names())
        self.assertEquals(["test_collection"], database._mydb.list_collection_names())
        # self.assertEquals(1, database.count_tweets("test_collection"))
        self.assertTrue("Hello, world!" in list(database.retrieve_tweet(1).values()))

        #Delete database
        database._myclient.drop_database("test")
        

if __name__ == '__main__':
    unittest.main()
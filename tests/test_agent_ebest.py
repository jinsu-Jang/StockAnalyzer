import unittest
from stocklab.agent.ebest import EBest
import inspect
import time
from stocklab.db_handler.mongodb_handler import MongoDBHandler

class TestEbest(unittest.TestCase):
    def setUp(self):
        self.ebest = EBest("DEMO")
        self.ebest.login()
        self.mongodb = MongoDBHandler()
        
    def test_collect_code_list(self):
        print("start")
        result = self.ebest.get_code_list("ALL")
        self.mongodb.delete_items({}, "stocklab", "code_info")
        self.mongodb.insert_items(result, "stocklab", "code_info")

    # def test_get_code_list(self):
    #     print(inspect.stack()[0][3])
    #     result = self.ebest.get_code_list("ALL")
    #     assert result is not None
    #     print(len(result))  
     
    # def test_get_account_info(self):
    #     print("start!!")
    #     result = self.ebest.get_account_info()
    #     assert result is not None
    #     print(result)    

    # def test_get_account_stock_info(self):
    #     result = self.ebest.get_account_stock_info()
    #     assert result is not None
    #     print(result)

    # def test_get_stock_price_by_code(self):
    #     print(inspect.stack()[0][3])
    #     result = self.ebest.get_stock_price_by_code("005930", "30")
    #     assert result is not None
    #     print(result)  

    #     result = self.ebest.get_code_list("ALL")   
    #     print(result) 

    def tearDown(self):
        self.ebest.logout()


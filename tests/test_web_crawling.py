""" 
단위테스트 실행
경로 : D:\DevProject\stock-lab
workon stocklab
 python -m unittest tests.test_web_crawling
"""

import unittest
from stocklab.agent.ebest import EBest
import inspect
import time
from stocklab.db_handler.mongodb_handler import MongoDBHandler
from datetime import datetime, timedelta

class TestWebCrawling(unittest.TestCase):
    def setUp(self):
        print("TestWebCrawling setUp 시작")
        # self.ebest = EBest("DEMO")
        # self.ebest.login()
        # self.mongodb = MongoDBHandler()
        
        
    def test_WebCrawling_from_DART(self):
        print("start")
    #     result = self.ebest.get_code_list("ALL")
    #     print(result)
    #     self.mongodb.delete_items({}, "stocklab", "code_info")
    #     self.mongodb.insert_items(result, "stocklab", "code_info")

 

    def tearDown(self):
        print("TestWebCrawling Tear Down 종료")
        # self.ebest.logout()

        
if __name__ == "__main__":
    unittest.main()        


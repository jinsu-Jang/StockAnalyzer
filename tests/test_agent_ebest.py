""" 
단위테스트 실행
경로 : D:\DevProject\stock-lab
workon stocklab
 python -m unittest tests.test_agent_ebest  
"""

import unittest
from stocklab.agent.ebest import EBest
import inspect
import time
from stocklab.db_handler.mongodb_handler import MongoDBHandler
from stockserver.job.job import Job
from datetime import datetime, timedelta

class TestEbest(unittest.TestCase):
    def setUp(self):
        # self.ebest = EBest("DEMO")
        # self.ebest.login()
        # self.mongodb = MongoDBHandler()
        self.job = Job()
        
        
    # def test_collect_code_list(self):
    #     print("start")
    #     result = self.ebest.get_code_list("ALL")
    #     print(result)
    #     self.mongodb.delete_items({}, "stocklab", "code_info")
    #     self.mongodb.insert_items(result, "stocklab", "code_info")

    def test_getcurrent_price(self):
        result = self.job.get(4)
        # result = self.ebest.get_code_list("ALL")
        # print(result)
        # result = self.ebest.get_current_price_by_shcodes("000225005930")
    #     print("start")
    #     result = self.ebest.get_code_list("ALL")
        print(result)
        

    #     self.mongodb.delete_items({}, "stocklab", "code_info")
    #     self.mongodb.insert_items(result, "stocklab", "code_info")    

    # def test_get_stock_chart_by_code(self):
    #     print("start get_stock_chart_by_code")

    #     code_list = list(self.mongodb.find_items({}, "stocklab", "code_info"))
        
    #     target_code = set([item["단축코드"] for item in code_list])
    #     # print(target_code)
    #     today = datetime.today().strftime("%Y%m%d")
    #     fromday = (datetime.today() - timedelta(days=30)).strftime("%Y%m%d")

    #     inc_codes = []
    #     # print(code_list)
    #     loop_cnt = 0
    #     for code in code_list:
    #         loop_cnt = loop_cnt + 1
    #         if loop_cnt % 100 == 0 and len(inc_codes) > 0 :
    #             print(str(loop_cnt % 100) + "//" + str(len(inc_codes)))
    #             print(code["단축코드"]+ "진행율 : " + str((loop_cnt / len(code_list) * 100)))
    #             self.mongodb.insert_items(inc_codes, "stocklab", "check_volume")  
    #             inc_codes.clear()

    #         print(code["단축코드"])
    #         results = self.ebest.get_stock_chart_by_code(code["단축코드"], "2", fromday, today)
    #         time.sleep(1)
    #         if len(results) > 0:
    #             # 평균 거래량 계산
    #             tot_volume = 0
    #             i_count = 0
    #             for result in results:
    #                 if  int(result['거래량']) != 0 :
    #                     tot_volume = tot_volume + int(result['거래량'])
    #                     i_count= i_count + 1

    #             if  i_count == 0 or tot_volume == 0:
    #                 continue

    #             avg_volume = tot_volume / i_count
    #             inc_rate = int(result['거래량']) / avg_volume
    #             print("체크 종목 :" + code["종목명"] + "  거래량 [" + result['거래량'] + "] 평균 [" + str(avg_volume) + "]  비율[" + str(inc_rate) + "]")
    #             # 거래량이 5배 이상이면 종목 추가
    #             if inc_rate > 5 :
    #                 inc_code = {"code": code["단축코드"], "종목명": code["종목명"], "sdate": today, "avg_volume": int(avg_volume),  "volume":int(result['거래량'])}
    #                 inc_codes.append(inc_code)
    #                 print("추가된 종목 :" + code["종목명"] + " 건수 : " + str(len(inc_codes))) 

    #     if len(inc_codes) > 0 :
    #         self.mongodb.insert_items(inc_codes, "stocklab", "check_volume")  

    # def test_get_company_fi_rank(self):
    #     print("start get_company_fi_rank")
    #     result = self.ebest.get_company_fi_rank("ALL", "1")
    #     # print(result)
    #     print(len(result))

    # def test_get_code_list(self):
    #     fromday = (datetime.today() - timedelta(days=30)).strftime("%Y%m%d")
    #     print(fromday)
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
        # self.ebest.logout()
        print("tearDown")

        
if __name__ == "__main__":
    unittest.main()        


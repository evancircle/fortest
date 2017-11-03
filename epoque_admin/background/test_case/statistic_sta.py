# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
import os

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.statisticPage import statistic
from selenium.webdriver.common.by import By


class statisticTest(myunit.MyTest):
    """公众号统计查询测试"""

    def statistic_login_verify(self, username="admin", password="000000"):
        statistic(self.driver).surf_statistic(username, password)

    def test_search_statisticcontrastdate(self):
        """查询、对比日期"""
        self.statistic_login_verify()
        sleep(2)
        po = statistic(self.driver)
        po.statistic_search_contrastdate(start_date="2017-07-04", end_date="2017-07-04")
        po.statistic_search_checkdate(start_date="2017-07-05", end_date="2017-07-05")
        po.statistic_lostfocus()
        po.statistic_search_button()
        sleep(1)
        self.assertEqual(po.statistic_info_check(),"10313")
        self.assertEqual(po.statistic_info_contrast(),"9972")
        self.assertEqual(po.statistic_info_contrastdate(),"2017-07-05")
        function.insert_img(self.driver, "statisticdate_search_successs.jpg")


    def test_statisticexport(self):
        """导出列表"""
        self.statistic_login_verify()
        sleep(2)
        po = statistic(self.driver)
        po.statistic_search_contrastdate(start_date="2017-07-04", end_date="2017-07-04")
        po.statistic_search_checkdate(start_date="2017-07-05",end_date="2017-07-05")
        po.statistic_lostfocus()
        po.statistic_search_button()
        self.assertTrue(po.statistic_export(),True)
        function.insert_img(self.driver, "statistic_export_successs.jpg")

    def test_statistictype(self):
        """渠道类型"""
        self.statistic_login_verify()
        sleep(2)
        po = statistic(self.driver)
        po.statistic_search_contrastdate(start_date="2017-07-04", end_date="2017-07-04")
        po.statistic_search_checkdate(start_date="2017-07-05", end_date="2017-07-05")
        po.statistic_lostfocus()
        po.statistic_search_type(type="2")
        po.statistic_lostfocus()
        po.statistic_search_button()
        sleep(1)
        self.assertEqual(po.statistic_info_check(), "12")
        self.assertEqual(po.statistic_info_contrast(), "17")
        function.insert_img(self.driver, "statistic_exportsummary_successs.jpg")


if __name__ == "__main__":
    unittest.main()


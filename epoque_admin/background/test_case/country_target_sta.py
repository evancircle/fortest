# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
import os

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.country_targetPage import ctarget
from selenium.webdriver.common.by import By


class ctargetTest(myunit.MyTest):
    """总部目标查询测试"""

    def ctarget_login_verify(self, username="admin", password="000000"):
        ctarget(self.driver).surf_ctarget(username, password)

    def test_ctarget_export(self):
        """导出"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.ctarget_export()
        self.assertTrue(po.ctarget_export(), True)
        function.insert_img(self.driver, "ctarget_export_successs.jpg")

    def test_search_ctarget_id_summary(self):
        """汇总-设备编号搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.ctarget_search_id(id="BL160127")
        po.ctarget_search_date(start_date='2017-10-01',end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_summary_info_region(),u"华中")
        self.assertEqual(po.ctarget_summary_info_goal(),"1")
        function.insert_img(self.driver, "country_target_summary_id_search_successs.jpg")

    def test_search_ctarget_id_detail(self):
        """明细-设备编号搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.target_switch_detail()
        po.ctarget_search_id(id="BL160127")
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_detail_info_id(),u"BL160127")
        self.assertEqual(po.ctarget_detail_info_goal(),"1")
        function.insert_img(self.driver, "country_target_detail_target_id_search_successs.jpg")

    def test_search_ctarget_code_summary(self):
        """汇总-门店代码搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.ctarget_search_code(code="HA45BL")
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_summary_info_region(),u"华中")
        self.assertEqual(po.ctarget_summary_info_goal(),"1")
        function.insert_img(self.driver, "country_target_summary_code_search_successs.jpg")

    def test_search_ctarget_code_detail(self):
        """明细-门店代码搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.target_switch_detail()
        po.ctarget_search_code(code="HA45BL")
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_detail_info_id(),u"BL160127")
        self.assertEqual(po.ctarget_detail_info_shop(),u'武汉中商销品茂BL')
        self.assertEqual(po.ctarget_detail_info_goal(),"1")
        function.insert_img(self.driver, "country_target_detail_target_code_search_successs.jpg")

    def test_search_ctarget_shop_summary(self):
        """汇总-门店名称搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.ctarget_search_shop(shop=u"武汉中商销品茂BL")
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_summary_info_region(),u"华中")
        self.assertEqual(po.ctarget_summary_info_goal(),"1")
        function.insert_img(self.driver, "country_target_summary_shop_search_successs.jpg")

    def test_search_ctarget_shop_detail(self):
        """明细-门店名称搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.target_switch_detail()
        po.ctarget_search_shop(shop=u"武汉中商销品茂BL")
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_detail_info_id(),u"BL160127")
        self.assertEqual(po.ctarget_detail_info_shop(),u'武汉中商销品茂BL')
        self.assertEqual(po.ctarget_detail_info_goal(),"1")
        function.insert_img(self.driver, "country_target_detail_target_shop_search_successs.jpg")

    def test_search_ctarget_region_summary(self):
        """汇总-地区搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.ctarget_search_area(area='4')
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_summary_info_region(),u"华北")
        self.assertEqual(po.ctarget_summary_info_goal(),"80")
        function.insert_img(self.driver, "country_target_summary_area_search_successs.jpg")

    def test_search_ctarget_region_detail(self):
        """明细-地区搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.target_switch_detail()
        po.ctarget_search_area(area='4')
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_detail_info_region(),u"华北")
        function.insert_img(self.driver, "country_target_detail_target_area_search_successs.jpg")

    def test_search_ctarget_procince_detail(self):
        """明细-省份搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.target_switch_detail()
        po.ctarget_search_province(area=4,province=3)
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_detail_info_region(),u"华北")
        self.assertEqual(po.ctarget_detail_info_province(),u'山西省')
        function.insert_img(self.driver, "country_target_detail_target_province_search_successs.jpg")

    def test_search_ctarget_city_detail(self):
        """明细-城市搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.target_switch_detail()
        po.ctarget_search_city(area=4,province=3,city=3)
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.ctarget_search_button()
        sleep(1)
        self.assertEqual(po.ctarget_detail_info_region(),u"华北")
        self.assertEqual(po.ctarget_detail_info_province(),u'山西省')
        self.assertEqual(po.ctarget_detail_info_city(),u'临汾市')
        function.insert_img(self.driver, "country_target_detail_target_city_search_successs.jpg")

    def test_search_ctarget_date_detail(self):
        """明细-时间搜索"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.target_switch_detail()
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-06')
        po.ctarget_search_button()
        sleep(1)
        self.assertGreaterEqual(po.ctarget_detail_date_info,'2017-10-01')
        self.assertLessEqual(po.ctarget_detail_info_date(),'2017-10-06')
        function.insert_img(self.driver, "country_target_detail_target_date_search_successs.jpg")

    def test_search_ctarget_nextpage_detail(self):
        """明细-下一页"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.target_switch_detail()
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-06')
        po.ctarget_search_button()
        sleep(1)
        po.ctarget_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scan-target/analy-country?page_type=detail&scanner_id=&shop_code=&shop_name=&regionid=0&provinceid=0&cityid=0&date_from=2017-10-01&date_to=2017-10-06&page=2')
        function.insert_img(self.driver, "country_target_detail_target_nextpage_search_successs.jpg")

    def test_search_ctarget_lastpage_detail(self):
        """明细-上一页"""
        self.ctarget_login_verify()
        sleep(2)
        po = ctarget(self.driver)
        po.target_switch_detail()
        po.ctarget_search_date(start_date='2017-10-01', end_date='2017-10-06')
        po.ctarget_search_button()
        sleep(1)
        po.ctarget_nextpage()
        po.ctarget_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scan-target/analy-country?page_type=detail&scanner_id=&shop_code=&shop_name=&regionid=0&provinceid=0&cityid=0&date_from=2017-10-01&date_to=2017-10-06&page=1')
        function.insert_img(self.driver, "country_target_detail_target_lastpage_search_successs.jpg")

if __name__ == "__main__":
    unittest.main()


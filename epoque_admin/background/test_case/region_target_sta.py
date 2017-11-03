# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
import os

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.region_targetPage import rtarget
from selenium.webdriver.common.by import By


class rtargetTest(myunit.MyTest):
    """地区目标查询测试"""

    def rtarget_login_verify(self, username="admin", password="000000"):
        rtarget(self.driver).surf_rtarget(username, password)

    def test_rtarget_export(self):
        """导出"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.rtarget_export()
        self.assertTrue(po.rtarget_export(), True)
        function.insert_img(self.driver, "rtarget_export_successs.jpg")

    def test_search_rtarget_id_summary(self):
        """汇总-设备编号搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.rtarget_search_id(id="BL160095")
        po.rtarget_search_date(start_date='2017-10-01',end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_summary_info_region(),u"华北")
        self.assertEqual(po.rtarget_summary_info_goal(),"2")
        function.insert_img(self.driver, "region_target_summary_id_search_successs.jpg")

    def test_search_rtarget_id_detail(self):
        """明细-设备编号搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.target_switch_detail()
        po.rtarget_search_id(id="BL160095")
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_detail_info_id(),u"BL160095")
        self.assertEqual(po.rtarget_detail_info_goal(),"1")
        function.insert_img(self.driver, "region_target_detail_target_id_search_successs.jpg")

    def test_search_rtarget_code_summary(self):
        """汇总-门店代码搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.rtarget_search_code(code="DB03MA")
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_summary_info_region(),u"华北")
        self.assertEqual(po.rtarget_summary_info_goal(),"2")
        function.insert_img(self.driver, "region_target_summary_code_search_successs.jpg")

    def test_search_rtarget_code_detail(self):
        """明细-门店代码搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.target_switch_detail()
        po.rtarget_search_code(code="DB03MA")
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_detail_info_id(),u"BL160157")
        self.assertEqual(po.rtarget_detail_info_shop(),u'北京华润五彩城店MAP')
        self.assertEqual(po.rtarget_detail_info_goal(),"1")
        function.insert_img(self.driver, "region_target_detail_target_code_search_successs.jpg")

    def test_search_rtarget_shop_summary(self):
        """汇总-门店名称搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.rtarget_search_shop(shop=u"北京华润五彩城店MAP")
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_summary_info_region(),u"华北")
        self.assertEqual(po.rtarget_summary_info_goal(),"2")
        function.insert_img(self.driver, "region_target_summary_shop_search_successs.jpg")

    def test_search_rtarget_shop_detail(self):
        """明细-门店名称搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.target_switch_detail()
        po.rtarget_search_shop(shop=u"北京华润五彩城店MAP")
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_detail_info_id(),u"BL160157")
        self.assertEqual(po.rtarget_detail_info_shop(),u'北京华润五彩城店MAP')
        self.assertEqual(po.rtarget_detail_info_goal(),"1")
        function.insert_img(self.driver, "region_target_detail_target_shop_search_successs.jpg")

    def test_search_rtarget_region_summary(self):
        """汇总-地区搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.rtarget_search_area(area='4')
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_summary_info_region(),u"华北")
        self.assertEqual(po.rtarget_summary_info_goal(),"45")
        function.insert_img(self.driver, "region_target_summary_area_search_successs.jpg")

    def test_search_rtarget_region_detail(self):
        """明细-地区搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.target_switch_detail()
        po.rtarget_search_area(area='4')
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_detail_info_region(),u"华北")
        function.insert_img(self.driver, "region_target_detail_target_area_search_successs.jpg")

    def test_search_rtarget_procince_detail(self):
        """明细-省份搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.target_switch_detail()
        po.rtarget_search_province(area=4,province=6)
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_detail_info_region(),u"华北")
        self.assertEqual(po.rtarget_detail_info_province(),u'北京市')
        function.insert_img(self.driver, "region_target_detail_target_province_search_successs.jpg")

    def test_search_rtarget_city_detail(self):
        """明细-城市搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.target_switch_detail()
        po.rtarget_search_city(area=4,province=6,city=2)
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.rtarget_search_button()
        sleep(1)
        self.assertEqual(po.rtarget_detail_info_region(),u"华北")
        self.assertEqual(po.rtarget_detail_info_province(),u'北京市')
        self.assertEqual(po.rtarget_detail_info_city(),u'北京市')
        function.insert_img(self.driver, "region_target_detail_target_city_search_successs.jpg")

    def test_search_rtarget_date_detail(self):
        """明细-时间搜索"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.target_switch_detail()
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-06')
        po.rtarget_search_button()
        sleep(1)
        self.assertGreaterEqual(po.rtarget_detail_date_info,'2017-10-01')
        self.assertLessEqual(po.rtarget_detail_info_date(),'2017-10-06')
        function.insert_img(self.driver, "region_target_detail_target_date_search_successs.jpg")

    def test_search_rtarget_nextpage_detail(self):
        """明细-下一页"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.target_switch_detail()
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-06')
        po.rtarget_search_button()
        sleep(1)
        po.rtarget_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scan-target/analy?page_type=detail&scanner_id=&shop_code=&shop_name=&regionid=0&provinceid=0&cityid=0&date_from=2017-10-01&date_to=2017-10-06&page=2')
        function.insert_img(self.driver, "region_target_detail_target_nextpage_search_successs.jpg")

    def test_search_rtarget_lastpage_detail(self):
        """明细-上一页"""
        self.rtarget_login_verify()
        sleep(2)
        po = rtarget(self.driver)
        po.target_switch_detail()
        po.rtarget_search_date(start_date='2017-10-01', end_date='2017-10-06')
        po.rtarget_search_button()
        sleep(1)
        po.rtarget_nextpage()
        po.rtarget_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scan-target/analy?page_type=detail&scanner_id=&shop_code=&shop_name=&regionid=0&provinceid=0&cityid=0&date_from=2017-10-01&date_to=2017-10-06&page=1')
        function.insert_img(self.driver, "region_target_detail_target_lastpage_search_successs.jpg")

if __name__ == "__main__":
    unittest.main()


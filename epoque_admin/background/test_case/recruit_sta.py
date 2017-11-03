# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.recruitPage import recruit
from selenium.webdriver.common.by import By


class recruitTest(myunit.MyTest):
    """会员招募表测试"""

    def recruit_login_verify(self, username="admin", password="000000"):
        recruit(self.driver).surf_recruit(username, password)

    def test_search_recruitdate(self):
        """查询日期搜索-明细表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_switchtodetail()
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual("2017-08-04", po.recruit_info_date())
        self.assertEqual(po.recruit_detail(), u"统计明细表")
        function.insert_img(self.driver, "recruitdate_search_successs.jpg")

    def test_search_recruitregionsummary(self):
        """所在地区搜索-汇总表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_search_region(region="4")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_info_region(), u'华北')
        self.assertEqual(po.recruit_summary(), u"统计汇总表")
        function.insert_img(self.driver, "recruitregionsummary_search_successs.jpg")

    def test_search_recruitregiondetail(self):
        """所在地区搜索-明细表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_switchtodetail()
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_search_region(region="4")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_info_region(), u'华北')
        self.assertEqual(po.recruit_detail(), u"统计明细表")
        function.insert_img(self.driver, "recruitregiondetail_search_successs.jpg")

    def test_search_recruitprovincesummary(self):
        """所在省份搜索-汇总表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_search_province(region="4", province="3")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_info_province(), u'山西省')
        self.assertEqual(po.recruit_summary(), u"统计汇总表")
        function.insert_img(self.driver, "recruitprovincesummary_search_successs.jpg")

    def test_search_recruitprovincedetail(self):
        """所在省份搜索-明细表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_switchtodetail()
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_search_province(region="4", province="3")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_info_province(), u'山西省')
        self.assertEqual(po.recruit_detail(), u"统计明细表")
        function.insert_img(self.driver, "recruitprovincedetail_search_successs.jpg")

    def test_search_recruitcitysummary(self):
        """所在城市搜索-汇总表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_search_city(region="4", province="3", city="3")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_info_city(), u'临汾市')
        self.assertEqual(po.recruit_summary(), u"统计汇总表")
        function.insert_img(self.driver, "recruitcitysummary_search_successs.jpg")

    def test_search_recruitcitydetail(self):
        """所在城市搜索-明细表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_switchtodetail()
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_search_city(region="4", province="3", city="3")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_info_city(), u'临汾市')
        self.assertEqual(po.recruit_detail(), u"统计明细表")
        function.insert_img(self.driver, "recruitcitydetail_search_successs.jpg")

    def test_recruitexportsummary(self):
        """汇总表导出列表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_lostfocus()
        po.recruit_search_brand(brand="2")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_export(), True)
        self.assertEqual(po.recruit_summary(), u"统计汇总表")
        function.insert_img(self.driver, "recruit_exportsummary_successs.jpg")

    def test_recruitexportdetail(self):
        """明细表导出列表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_switchtodetail()
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_lostfocus()
        po.recruit_search_brand(brand="2")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_export(), True)
        self.assertEqual(po.recruit_detail(), u"统计明细表")
        function.insert_img(self.driver, "recruit_exportdetail_successs.jpg")

    def test_recruitbrandsummary(self):
        """品牌搜索-汇总表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_lostfocus()
        po.recruit_search_brand(brand="7")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_info_brand(), "BL")
        function.insert_img(self.driver, "recruit_exportsummary_successs.jpg")

    def test_recruitbranddetail(self):
        """品牌搜索-明细表"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_switchtodetail()
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_lostfocus()
        po.recruit_search_brand(brand="7")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        self.assertEqual(po.recruit_info_brand(), "BL")
        function.insert_img(self.driver, "recruit_exportdetail_successs.jpg")

    def test_recruitnextpage(self):
        """下一页"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        po.recruit_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage,'http://bossdev.epoque.cn/admin/recruit/summary?brand=&date_from=2017-08-04&date_to=2017-08-04&regionid=0&provinceid=0&cityid=0&page=2')
        function.insert_img(self.driver, "recruit_nextpage_success.jpg")

    def test_scanmgtlastpage(self):
        """上一页"""
        self.recruit_login_verify()
        sleep(2)
        po = recruit(self.driver)
        po.recruit_search_date(start_date="2017-08-04", end_date="2017-08-04")
        po.recruit_lostfocus()
        po.recruit_search_button()
        sleep(1)
        po.recruit_nextpage()
        po.recruit_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage,'http://bossdev.epoque.cn/admin/recruit/summary?brand=&date_from=2017-08-04&date_to=2017-08-04&regionid=0&provinceid=0&cityid=0&page=1')
        function.insert_img(self.driver, "recruit_lastpage_success.jpg")

if __name__ == "__main__":
    unittest.main()


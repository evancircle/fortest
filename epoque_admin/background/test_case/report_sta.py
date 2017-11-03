# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.reportPage import report
from selenium.webdriver.common.by import By

class reportTest(myunit.MyTest):

    """设备日报测试"""
    def report_login_verify(self, username="admin", password="000000"):
        report(self.driver).surf_report(username, password)

    def test_search_reportid(self):
        """设备编号搜索"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_search_scanner_id(id="BL160094")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        self.assertEqual(po.report_info_scanner_id(), 'BL160094')
        function.insert_img(self.driver, "reportid_search_successs.jpg")

    def test_search_reportshopname(self):
        """门店名称搜索"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_lostfocus()
        po.report_search_shop_name(name=u"上海嘉定万达广场店Mart")
        sleep(1)
        po.report_search_button()
        sleep(1)
        self.assertEqual(po.report_info_shop_name(), u"上海嘉定万达广场店Mart")
        function.insert_img(self.driver, "reportshopname_search_successs.jpg")

    def test_search_reportshopcode(self):
        """门店代码搜索"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_lostfocus()
        po.report_search_shop_code(code="CA03MA")
        sleep(1)
        po.report_search_button()
        sleep(1)
        self.assertEqual(po.report_info_shop_code(), 'CA03MA')
        function.insert_img(self.driver, "reportshopcode_search_successs.jpg")

    def test_search_reportdate(self):
        """查询日期搜索"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-02")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        self.assertIn("2017-07-02",po.report_info_date() )
        function.insert_img(self.driver, "reportdate_search_successs.jpg")

    def test_search_reportregion(self):
        """所在地区搜索"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_search_region(region="4")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        self.assertEqual(po.report_info_region(), u'华北')
        function.insert_img(self.driver, "reportregion_search_successs.jpg")

    def test_search_reportprovince(self):
        """所在省份搜索"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_search_province(region="4",province="3")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        self.assertEqual(po.report_info_province(), u'山西省')
        function.insert_img(self.driver, "reportprovince_search_successs.jpg")

    def test_search_reportcity(self):
        """所在城市搜索"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_search_city(region="3",province="2",city="4")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        self.assertEqual(po.report_info_city(), u'怀化市')
        function.insert_img(self.driver, "reportcity_search_successs.jpg")

    def test_search_reporttype(self):
        """门店类型搜索"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_shop_type(type="1")
        po.report_search_date(date="2017-07-01")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        self.assertEqual(po.report_info_shop_type(), u'购物中心')
        function.insert_img(self.driver, "reporttype_search_successs.jpg")

    def test_search_reportbrand(self):
        """品牌搜索"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_search_brand(brand="7")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        self.assertIn('BL', po.report_info_shop_name())
        function.insert_img(self.driver, "reportbrand_search_successs.jpg")

    def test_reportexport(self):
        """导出列表"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_lostfocus()
        po.report_search_scanner_id(id="BL160091")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        self.assertEqual(po.report_export(),True)
        function.insert_img(self.driver, "report_export_successs.jpg")

    def test_reportnextpage(self):
        """下一页"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        po.report_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scanner/daily?scanner_id=&shop_name=&shop_code=&record_date=2017-07-01&regionid=0&provinceid=0&cityid=0&shop_type=&brand=&page=2')
        function.insert_img(self.driver, "report_nextpage_success.jpg")

    def test_scanmgtlastpage(self):
        """上一页"""
        self.report_login_verify()
        sleep(2)
        po = report(self.driver)
        po.report_search_date(date="2017-07-01")
        po.report_lostfocus()
        po.report_search_button()
        sleep(1)
        po.report_nextpage()
        po.report_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scanner/daily?scanner_id=&shop_name=&shop_code=&record_date=2017-07-01&regionid=0&provinceid=0&cityid=0&shop_type=&brand=&page=1')
        function.insert_img(self.driver, "report_lastpage_success.jpg")

if __name__ == "__main__":
    unittest.main()

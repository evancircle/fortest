# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.enquiryPage import enquiry
from selenium.webdriver.common.by import By

class enquiryTest(myunit.MyTest):

    """统计分析测试"""
    def enquiry_login_verify(self, username="admin", password="000000"):
        enquiry(self.driver).surf_enquiry(username, password)

    def test_search_enquiryid_summary(self):
        """设备编号搜索-汇总"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_search_scanner_id(id="BL160094")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_scanner_id(), 'BL160094')
        function.insert_img(self.driver, "enquiryidsummary_search_successs.jpg")

    def test_search_enquiryid_detail(self):
        """设备编号搜索-明细"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_search_scanner_id(id="BL160094")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_scanner_id(), 'BL160094')
        self.assertEqual(po.enquiry_detail(),u"统计明细")
        function.insert_img(self.driver, "enquiryiddetail_search_successs.jpg")

    def test_search_enquiryshopnamesummary(self):
        """门店名称搜索-汇总"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_shop_name(name=u"上海嘉定万达广场店Mart")
        sleep(1)
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_shop_name(), u"上海嘉定万达广场店Mart")
        self.assertEqual(po.enquiry_summary(), u"统计汇总")
        function.insert_img(self.driver, "enquiryshopnamesummary_search_successs.jpg")

    def test_search_enquiryshopnamedetail(self):
        """门店名称搜索-明细"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_shop_name(name=u"上海嘉定万达广场店Mart")
        sleep(1)
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_shop_name(), u"上海嘉定万达广场店Mart")
        self.assertEqual(po.enquiry_detail(), u"统计明细")
        function.insert_img(self.driver, "enquiryshopnamedetail_search_successs.jpg")

    def test_search_enquiryshopcodesummary(self):
        """门店代码搜索-汇总"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_shop_code(code="CA03MA")
        sleep(1)
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_shop_code(), 'CA03MA')
        self.assertEqual(po.enquiry_summary(), u"统计汇总")
        function.insert_img(self.driver, "enquiryshopcodesummary_search_successs.jpg")

    def test_search_enquiryshopcodedetail(self):
        """门店代码搜索-明细"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_shop_code(code="CA03MA")
        sleep(1)
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_shop_code(), 'CA03MA')
        self.assertEqual(po.enquiry_detail(), u"统计明细")
        function.insert_img(self.driver, "enquiryshopcodedetail_search_successs.jpg")

    def test_search_enquirydate(self):
        """查询日期搜索-明细"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual("2017-07-05 00:00:00",po.enquiry_info_date())
        self.assertEqual(po.enquiry_detail(), u"统计明细")
        function.insert_img(self.driver, "enquirydate_search_successs.jpg")

    def test_search_enquiryregionsummary(self):
        """所在地区搜索-汇总"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_region(region="4")
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_region(), u'华北')
        self.assertEqual(po.enquiry_summary(), u"统计汇总")
        function.insert_img(self.driver, "enquiryregionsummary_search_successs.jpg")

    def test_search_enquiryregiondetail(self):
        """所在地区搜索-明细"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_region(region="4")
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_region(), u'华北')
        self.assertEqual(po.enquiry_detail(), u"统计明细")
        function.insert_img(self.driver, "enquiryregiondetail_search_successs.jpg")

    def test_search_enquiryprovincesummary(self):
        """所在省份搜索-汇总"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_province(region="4",province="3")
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_province(), u'山西省')
        self.assertEqual(po.enquiry_summary(), u"统计汇总")
        function.insert_img(self.driver, "enquiryprovincesummary_search_successs.jpg")

    def test_search_enquiryprovincedetail(self):
        """所在省份搜索-明细"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_province(region="4",province="3")
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_province(), u'山西省')
        self.assertEqual(po.enquiry_detail(), u"统计明细")
        function.insert_img(self.driver, "enquiryprovincedetail_search_successs.jpg")

    def test_search_enquirycitysummary(self):
        """所在城市搜索-汇总"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_city(region="4",province="3",city="3")
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_city(), u'临汾市')
        self.assertEqual(po.enquiry_summary(), u"统计汇总")
        function.insert_img(self.driver, "enquirycitysummary_search_successs.jpg")

    def test_search_enquirycitydetail(self):
        """所在城市搜索-明细"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_city(region="4",province="3",city="3")
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_city(), u'临汾市')
        self.assertEqual(po.enquiry_detail(), u"统计明细")
        function.insert_img(self.driver, "enquirycitydetail_search_successs.jpg")

    def test_search_enquirytypesummary(self):
        """门店类型搜索-汇总"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_search_shop_type(type="1")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_shop_type(), u'购物中心')
        self.assertEqual(po.enquiry_summary(), u"统计汇总")
        function.insert_img(self.driver, "enquirytypesummary_search_successs.jpg")

    def test_search_enquirytypedetail(self):
        """门店类型搜索-明细"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_search_shop_type(type="1")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_info_shop_type(), u'购物中心')
        self.assertEqual(po.enquiry_detail(), u"统计明细")
        function.insert_img(self.driver, "enquirytypedetail_search_successs.jpg")

    def test_search_enquirybrandsummary(self):
        """品牌搜索-汇总"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_search_brand(brand="7")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        self.assertIn('BL', po.enquiry_info_shop_name())
        self.assertEqual(po.enquiry_summary(), u"统计汇总")
        function.insert_img(self.driver, "enquirybrandsummary_search_successs.jpg")

    def test_search_enquirybranddetail(self):
        """品牌搜索-明细"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_search_brand(brand="7")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        self.assertIn('BL', po.enquiry_info_shop_name())
        self.assertEqual(po.enquiry_detail(), u"统计明细")
        function.insert_img(self.driver, "enquirybranddetail_search_successs.jpg")

    def test_enquiryexportsummary(self):
        """汇总导出列表"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_scanner_id(id="BL160091")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_export(),True)
        self.assertEqual(po.enquiry_summary(), u"统计汇总")
        function.insert_img(self.driver, "enquiry_exportsummary_successs.jpg")

    def test_enquiryexportdetail(self):
        """明细导出列表"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_switchtodetail()
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_scanner_id(id="BL160091")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        self.assertEqual(po.enquiry_export(),True)
        self.assertEqual(po.enquiry_detail(), u"统计明细")
        function.insert_img(self.driver, "enquiry_exportdetail_successs.jpg")

    def test_enquirynextpage(self):
        """下一页"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        po.enquiry_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/count/scanner-summary?scanner_id=&shop_name=&shop_code=&shop_type=&from_date=2017-07-05&to_date=2017-07-05&brand=&regionid=0&provinceid=0&cityid=0&page=2')
        function.insert_img(self.driver, "enquiry_nextpage_success.jpg")

    def test_scanmgtlastpage(self):
        """上一页"""
        self.enquiry_login_verify()
        sleep(2)
        po = enquiry(self.driver)
        po.enquiry_search_date(start_date="2017-07-05",end_date="2017-07-05")
        po.enquiry_lostfocus()
        po.enquiry_search_button()
        sleep(1)
        po.enquiry_nextpage()
        po.enquiry_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/count/scanner-summary?scanner_id=&shop_name=&shop_code=&shop_type=&from_date=2017-07-05&to_date=2017-07-05&brand=&regionid=0&provinceid=0&cityid=0&page=1')
        function.insert_img(self.driver, "enquiry_lastpage_success.jpg")

if __name__ == "__main__":
    unittest.main()


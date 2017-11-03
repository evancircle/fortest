# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.brandPage import brand
from selenium.webdriver.common.by import By

class brandTest(myunit.MyTest):

    """品牌统计测试"""
    def brand_login_verify(self, username="admin", password="000000"):
        brand(self.driver).surf_brand(username, password)
    
    def test_search_brandid_summary(self):
        """设备编号搜索-汇总"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_search_scanner_id(id="BL160094")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_scanner_id(), 'BL160094')
        function.insert_img(self.driver, "brandidsummary_search_successs.jpg")

    def test_search_brandid_detail(self):
        """设备编号搜索-明细"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_switchtodetail()
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_search_scanner_id(id="BL160094")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_scanner_id(), 'BL160094')
        self.assertEqual(po.brand_detail(),u"品牌明细")
        function.insert_img(self.driver, "brandiddetail_search_successs.jpg")

    def test_search_brandshopnamesummary(self):
        """门店名称搜索-汇总"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_lostfocus()
        po.brand_search_shop_name(name=u"上海嘉定万达广场店Mart")
        sleep(1)
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_shop_name(), u"上海嘉定万达广场店Mart")
        self.assertEqual(po.brand_summary(), u"品牌汇总")
        function.insert_img(self.driver, "brandshopnamesummary_search_successs.jpg")

    def test_search_brandshopnamedetail(self):
        """门店名称搜索-明细"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_switchtodetail()
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_lostfocus()
        po.brand_search_shop_name(name=u"上海嘉定万达广场店Mart")
        sleep(1)
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_shop_name(), u"上海嘉定万达广场店Mart")
        self.assertEqual(po.brand_detail(), u"品牌明细")
        function.insert_img(self.driver, "brandshopnamedetail_search_successs.jpg")

    def test_search_brandshopcodesummary(self):
        """门店代码搜索-汇总"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_lostfocus()
        po.brand_search_shop_code(code="CA03MA")
        sleep(1)
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_shop_name(), u'沈阳华润万象汇MAP')
        self.assertEqual(po.brand_summary(), u"品牌汇总")
        function.insert_img(self.driver, "brandshopcodesummary_search_successs.jpg")

    def test_search_brandshopcodedetail(self):
        """门店代码搜索-明细"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_switchtodetail()
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_lostfocus()
        po.brand_search_shop_code(code="CA03MA")
        sleep(1)
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_shop_name(), u'沈阳华润万象汇MAP')
        self.assertEqual(po.brand_detail(), u"品牌明细")
        function.insert_img(self.driver, "brandshopcodedetail_search_successs.jpg")

    def test_search_branddate(self):
        """查询日期搜索-明细"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_switchtodetail()
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertEqual("2017-07-18",po.brand_info_date())
        self.assertEqual(po.brand_detail(), u"品牌明细")
        function.insert_img(self.driver, "branddate_search_successs.jpg")

    def test_search_brandregionsummary(self):
        """所在地区搜索-汇总"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_search_region(region="4")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_region(), u'华北')
        self.assertEqual(po.brand_summary(), u"品牌汇总")
        function.insert_img(self.driver, "brandregionsummary_search_successs.jpg")

    def test_search_brandregiondetail(self):
        """所在地区搜索-明细"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_switchtodetail()
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_search_region(region="4")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_region(), u'华北')
        self.assertEqual(po.brand_detail(), u"品牌明细")
        function.insert_img(self.driver, "brandregiondetail_search_successs.jpg")

    def test_search_brandprovincesummary(self):
        """所在省份搜索-汇总"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_search_province(region="4",province="3")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_province(), u'山西省')
        self.assertEqual(po.brand_summary(), u"品牌汇总")
        function.insert_img(self.driver, "brandprovincesummary_search_successs.jpg")

    def test_search_brandprovincedetail(self):
        """所在省份搜索-明细"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_switchtodetail()
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_search_province(region="4",province="3")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_province(), u'山西省')
        self.assertEqual(po.brand_detail(), u"品牌明细")
        function.insert_img(self.driver, "brandprovincedetail_search_successs.jpg")

    def test_search_brandcitysummary(self):
        """所在城市搜索-汇总"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_search_city(region="4",province="3",city="3")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_city(), u'临汾市')
        self.assertEqual(po.brand_summary(), u"品牌汇总")
        function.insert_img(self.driver, "brandcitysummary_search_successs.jpg")

    def test_search_brandcitydetail(self):
        """所在城市搜索-明细"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_switchtodetail()
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_search_city(region="4",province="3",city="3")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertEqual(po.brand_info_city(), u'临汾市')
        self.assertEqual(po.brand_detail(), u"品牌明细")
        function.insert_img(self.driver, "brandcitydetail_search_successs.jpg")

    def test_brandexportsummary(self):
        """汇总导出列表"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_lostfocus()
        po.brand_search_scanner_id(id="BL160091")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertTrue(po.brand_export(),True)
        self.assertEqual(po.brand_summary(), u"品牌汇总")
        function.insert_img(self.driver, "brand_exportsummary_successs.jpg")

    def test_brandexportdetail(self):
        """明细导出列表"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_switchtodetail()
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_lostfocus()
        po.brand_search_scanner_id(id="BL160091")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        self.assertTrue(po.brand_export(), True)
        self.assertEqual(po.brand_detail(), u"品牌明细")
        function.insert_img(self.driver, "brand_exportdetail_successs.jpg")

    def test_brandnextpage(self):
        """下一页"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        po.brand_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/brand/summary?shop_code=&shop_name=&period_from=2017-07-18&period_to=2017-07-18&scanner_id=&regionid=0&provinceid=0&cityid=0&page=2')
        function.insert_img(self.driver, "brand_nextpage_success.jpg")

    def test_scanmgtlastpage(self):
        """上一页"""
        self.brand_login_verify()
        sleep(2)
        po = brand(self.driver)
        po.brand_search_date(start_date="2017-07-18",end_date="2017-07-18")
        po.brand_lostfocus()
        po.brand_search_button()
        sleep(1)
        po.brand_nextpage()
        po.brand_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/brand/summary?shop_code=&shop_name=&period_from=2017-07-18&period_to=2017-07-18&scanner_id=&regionid=0&provinceid=0&cityid=0&page=1')
        function.insert_img(self.driver, "brand_lastpage_success.jpg")

if __name__ == "__main__":
    unittest.main()


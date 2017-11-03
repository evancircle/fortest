# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.shopPage import shop
from selenium.webdriver.common.by import By

class shopTest(myunit.MyTest):

    """门店档案测试"""
    def shop_login_verify(self,username="admin", password="000000"):
        shop(self.driver).surf_shop(username,password)

    def test_search_shopbrand(self):
        """品牌搜索"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_brand(brand="2")
        po.shop_search_button()
        sleep(1)
        self.assertEqual(po.search_brand_success(), 'AC')
        function.insert_img(self.driver, "shopbrand_search_successs.jpg")

    def test_search_shoptype(self):
        """类型搜索"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_type(type="3")
        po.shop_search_button()
        sleep(1)
        self.assertEqual(po.search_type_success(), 'TOP SNEAKER')
        function.insert_img(self.driver, "shoptype_search_successs.jpg")

    def test_search_shoparea(self):
        """地区搜索"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_area(area="4")
        po.shop_search_button()
        sleep(1)
        self.assertEqual(po.search_area_success(), u'华北')
        function.insert_img(self.driver, "shoparea_search_successs.jpg")

    def test_search_shopprovince(self):
        """省份搜索"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_province(area="4",province="3")
        po.shop_search_button()
        sleep(1)
        self.assertEqual(po.search_province_success(), u'山西省')
        function.insert_img(self.driver, "shopprovince_search_successs.jpg")

    def test_search_shopcity(self):
        """城市搜索"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_city(area="4",province="3",city="6")
        sleep(1)
        po.shop_search_button()
        sleep(1)
        self.assertEqual(po.search_city_success(), u'晋中市')
        function.insert_img(self.driver, "shopcity_search_successs.jpg")

    def test_search_shopname(self):
        """名称搜索"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_name(name=u"福州仓山万达百货BL")
        po.shop_search_button()
        self.assertEqual(po.search_name_success(), u'福州仓山万达百货BL')
        function.insert_img(self.driver, "shopname_search_successs.jpg")

    def test_search_shopcode(self):
        """代码搜索"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_code(code="DC08TM")
        po.shop_search_button()
        self.assertEqual(po.search_code_success(), 'DC08TM')
        function.insert_img(self.driver, "shopcode_search_successs.jpg")

    def test_shopnextpage(self):
        """下一页"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/shop?page=2')
        function.insert_img(self.driver, "shop_nextpage_success.jpg")

    def test_shoplastpage(self):
        """上一页"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_nextpage()
        po.shop_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/shop?page=1')
        function.insert_img(self.driver, "shop_lastpage_success.jpg")

    def test_3_shopstatus(self):
        """启用/停用"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_code(code="D45T")
        po.shop_search_button()
        po.shop_open_stop_button()
        current_status = po.shop_status_info()
        self.assertEqual(current_status, u'启用')
        function.insert_img(self.driver, "shop_statuson_success.jpg")
        po.shop_search_code(code="D45T")
        po.shop_search_button()
        po.shop_open_stop_button()
        after_status = po.shop_status_info()
        self.assertEqual(after_status, u'停用')
        function.insert_img(self.driver, "shop_statusoff_success.jpg")

    def test_1_shopadd(self):
        """新增门店"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_add(brand="3",area="4",province="5",city="6",code="D45T",name="Toyota",type="7",address=u"深圳罗湖",wechataddress=u"深圳市罗湖区",mall="kkmall",status="1")
        po.shop_search_code(code="D45T")
        po.shop_search_button()
        self.assertEqual(po.shop_brand_info(),"AD")
        self.assertEqual(po.shop_area_info(),u"华北")
        self.assertEqual(po.shop_province_info(),u"山西省")
        self.assertEqual(po.shop_city_info(),u"晋城市")
        self.assertEqual(po.shop_name_info(),"Toyota")
        self.assertEqual(po.shop_code_info(),"D45T")
        self.assertEqual(po.shop_type_info(),u"其他")
        self.assertEqual(po.shop_address_info(),u"深圳罗湖")
        self.assertEqual(po.shop_wechataddress_info(),u"深圳市罗湖区")
        self.assertEqual(po.shop_status_info(),u"启用")
        function.insert_img(self.driver, "shop_add_success.jpg")

    def test_2_shopedit(self):
        """编辑门店"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_code(code="D45T")
        po.shop_edit(brand="1",area="2",province="3",city="4",name="Honda",type="5",address=u"北京海淀",wechataddress=u"北京市海淀区",mall="kkone",status="2")
        po.shop_search_code(code="D45T")
        po.shop_search_button()
        self.assertEqual(po.shop_brand_info(),"FM")
        self.assertEqual(po.shop_area_info(),u"华南")
        self.assertEqual(po.shop_province_info(),u"江西省")
        self.assertEqual(po.shop_city_info(),u"萍乡市")
        self.assertEqual(po.shop_name_info(),"Honda")
        self.assertEqual(po.shop_code_info(),"D45T")
        self.assertEqual(po.shop_type_info(),u"专卖店")
        self.assertEqual(po.shop_address_info(),u"北京海淀")
        self.assertEqual(po.shop_wechataddress_info(),u"北京市海淀区")
        self.assertEqual(po.shop_status_info(),u"停用")
        function.insert_img(self.driver, "shop_edit_success.jpg")

    def test_4_shopdelete(self):
        """删除门店"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_code(code="D45T")
        po.shop_search_button()
        po.shop_delete()
        po.shop_search_code(code="D45T")
        po.shop_search_button()
        sleep(2)
        table = self.driver.find_element_by_xpath("html/body/div/div[2]/div/div/div[2]/div/div/div[1]/div/table/tbody").find_elements(By.TAG_NAME,"tr")
        for i in table:
            p1 = (i.text).split(" ")
            for j in p1:
                self.assertNotEqual(j, "D45T")
        function.insert_img(self.driver, "shop_delete_successs.jpg")

    def test_5_shopexport(self):
        """导出列表"""
        self.shop_login_verify()
        sleep(2)
        po = shop(self.driver)
        po.shop_search_city(area="4", province="3", city="6")
        po.shop_search_button()
        sleep(1)
        self.assertEqual(po.shop_export(),True)
        function.insert_img(self.driver, "shop_export_successs.jpg")

if __name__ == "__main__":
    unittest.main()
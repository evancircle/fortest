# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.scanmgtPage import scanmgt
from selenium.webdriver.common.by import By

class scanmgtTest(myunit.MyTest):

    """扫描仪管理测试"""
    def scanmgt_login_verify(self,username="admin", password="000000"):
        scanmgt(self.driver).surf_scanmgt(username,password)

    def test_search_scanmgtid(self):
        """设备编号搜索"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_id(id="BL170716")
        po.scanmgt_search_button()
        sleep(1)
        self.assertEqual(po.search_id_success_mgt(), 'BL170716')
        function.insert_img(self.driver, "scanmgtid_search_successs.jpg")

    def test_search_scanmgtshopname(self):
        """门店名称搜索"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_shop_name(model=u"高平红旗生活广场BL")
        po.scanmgt_search_button()
        sleep(1)
        self.assertEqual(po.search_shop_name_success_mgt(), u'高平红旗生活广场BL')
        function.insert_img(self.driver, "scanmgtshopname_search_successs.jpg")

    def test_search_scanmgtshopcode(self):
        """门店代码搜索"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_shop_code(shop_code="MG04SD")
        po.scanmgt_search_button()
        self.assertEqual(po.search_shop_code_success_mgt(), "MG04SD")
        function.insert_img(self.driver, "scanmgtshopcode_search_successs.jpg")

    def test_search_scanmgtbrand(self):
        """品牌搜索"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_brand(brand="3")
        po.scanmgt_search_button()
        self.assertEqual(po.search_brand_success_mgt(), "AD")
        function.insert_img(self.driver, "scanmgtbrand_search_successs.jpg")

    def test_search_scanmgtarea(self):
        """地区搜索"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_area(area="2")
        po.scanmgt_search_button()
        self.assertEqual(po.search_area_success_mgt(), u"华南")
        function.insert_img(self.driver, "scanmgtarea_search_successs.jpg")

    def test_search_scanmgtprovince(self):
        """省份搜索"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_province(area='2',province='3')
        po.scanmgt_search_button()
        self.assertEqual(po.search_province_success_mgt(), u"贵州省")
        function.insert_img(self.driver, "scanmgtprovince_search_successs.jpg")

    def test_search_scanmgtcity(self):
        """城市搜索"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_city(area="2",province="4",city="3")
        po.scanmgt_search_button()
        self.assertEqual(po.search_city_success_mgt(), u"海口市")
        function.insert_img(self.driver, "scanmgtcity_search_successs.jpg")

    def test_search_scanmgttype(self):
        """门店类型搜索"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_type(type="1")
        po.scanmgt_search_button()
        self.assertEqual(po.search_type_success_mgt(), u"购物中心")
        function.insert_img(self.driver, "scanmgttype_search_successs.jpg")

    def test_search_scanmgtstatus(self):
        """门店状态搜索"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_status(status="4")
        po.scanmgt_search_button()
        self.assertEqual(po.search_status_success_mgt(), u"维修")
        function.insert_img(self.driver, "scanmgtstatus_search_successs.jpg")

    def test_scanmgtnextpage(self):
        """下一页"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scanner-bind?page=2')
        function.insert_img(self.driver, "scanmgt_nextpage_success.jpg")

    def test_scanmgtlastpage(self):
        """上一页"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_nextpage()
        po.scanmgt_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scanner-bind?page=1')
        function.insert_img(self.driver, "scanmgt_lastpage_success.jpg")

    def test_1_scanmgtadd(self):
        """新增扫描仪"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_add(id="BL188888",status="4",code="MJO94K",name=u"南昌鞋店",email="selenium@163.com",mac="6A:5T:4F:3D:2Q:1X",staff="Ryan",phone="13800138000",time="2017-08-01")
        po.scanmgt_search_id(id="BL188888")
        po.scanmgt_search_button()
        self.assertEqual(po.scanmgt_id_info(),"BL188888")
        self.assertEqual(po.scanmgt_model_info(),"DLO-007")
        self.assertEqual(po.scanmgt_area_info(),u"华南")
        self.assertEqual(po.scanmgt_province_info(),u"江西省")
        self.assertEqual(po.scanmgt_city_info(), u"南昌市")
        self.assertEqual(po.scanmgt_brand_info(),u"BS")
        self.assertEqual(po.scanmgt_shop_name_info(),u"南昌鞋店")
        self.assertEqual(po.scanmgt_code_info(), u"MJO94K")
        self.assertEqual(po.scanmgt_type_info(), u"购物中心")
        self.assertEqual(po.scanmgt_staff_info(), "Ryan")
        self.assertEqual(po.scanmgt_phone_info(), "13800138000")
        self.assertEqual(po.scanmgt_status_info(), u"维修")
        self.assertEqual(po.scanmgt_address_info(), u"南昌鞋店")
        function.insert_img(self.driver, "scanmgt_add_success.jpg")

    def test_2_scanmgtedit(self):
        """编辑扫描仪"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_shop_code(shop_code="MJO94K")
        po.scanmgt_search_button()
        po.scanmgt_edit(code="DB74ST",name=u"北京远洋未来安慧桥店ST",email="python@163.com",
                        mac="1P:2M:3I:4T:5Y:6E",staff="Bryan",phone="13600136000",time="2017-08-03",status="4",
                        history_code_edit="DB74ST",history_name_edit=u"北京远洋未来安慧桥店ST",edit_starttime="2017-07-01",edit_endtime="2017-07-15",
                        history_code_add="NKNN37",history_name_add=u"南宁民生路领跑运动城店NK",add_starttime = '2017-08-12', add_endtime = '2017-09-07')
        self.assertEqual(po.scanmgt_area_info(),u"华北")
        self.assertEqual(po.scanmgt_province_info(),u"北京市")
        self.assertEqual(po.scanmgt_city_info(), u"北京市")
        self.assertEqual(po.scanmgt_brand_info(),u"ST")
        self.assertEqual(po.scanmgt_shop_name_info(),u"北京远洋未来安慧桥店ST")
        self.assertEqual(po.scanmgt_code_info(), u"DB74ST")
        self.assertEqual(po.scanmgt_type_info(), u"购物中心")
        self.assertEqual(po.scanmgt_staff_info(), "Bryan")
        self.assertEqual(po.scanmgt_phone_info(), "13600136000")
        self.assertEqual(po.scanmgt_status_info(), u"维修")
        self.assertEqual(po.scanmgt_address_info(), u"北京市市辖区朝阳区北四环东路73号")
        po.scanmgt_search_shop_code(shop_code="DB74ST")
        po.scanmgt_search_button()
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[14]/div/a').click()
        #'html body div#page-container div#page-content div#wrap div.container div.f-page-content div.row.f-shadow div.collapse.in.listing div.f-table-wrapper.f-fixed-table-wrapper div.f-table-scroll table.table.table-striped.table-bordered.datatables tbody tr td div a.btn.f-button-text'
        function.insert_img(self.driver, "scanmgt_edit_success.jpg")

    def test_3_scanmgtdelete(self):
        """删除扫描仪"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_id(id="BL188888")
        po.scanmgt_search_button()
        po.scanmgt_delete()
        po.scanmgt_search_id(id="BL188888")
        po.scanmgt_search_button()
        sleep(2)
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody').find_elements(By.TAG_NAME,"tr")
        for i in table:
            p1 = (i.text).split(" ")
            for j in p1:
                self.assertNotEqual(j, "BL188888")
        function.insert_img(self.driver, "scanmgt_delete_successs.jpg")

    def test_4_scanmgtexport(self):
        """导出列表"""
        self.scanmgt_login_verify()
        sleep(2)
        po = scanmgt(self.driver)
        po.scanmgt_search_id(id="BL170461")
        po.scanmgt_search_button()
        sleep(1)
        self.assertEqual(po.scanmgt_export(),True)
        function.insert_img(self.driver, "scanmgt_export_successs.jpg")

if __name__ == "__main__":
    unittest.main()
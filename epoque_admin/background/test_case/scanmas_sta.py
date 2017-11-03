# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.scanmasPage import scanmas
from selenium.webdriver.common.by import By

class scanmasTest(myunit.MyTest):

    """扫描仪档案测试"""
    def scanmas_login_verify(self,username="admin", password="000000"):
        scanmas(self.driver).surf_scanmas(username,password)

    def test_search_scanmasbrand(self):
        """品牌搜索"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_search_brand()
        po.scanmas_search_button()
        sleep(1)
        self.assertEqual(po.search_brand_success_mas(), 'DLO')
        function.insert_img(self.driver, "scanmasbrand_search_successs.jpg")

    def test_search_scanmasstatus(self):
        """状态搜索"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_search_status(status="2")
        po.scanmas_search_button()
        sleep(1)
        self.assertEqual(po.search_status_success_mas(), u'停用')
        function.insert_img(self.driver, "scanmasstatus_search_successs.jpg")

    def test_search_scanmasid(self):
        """编号搜索"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_search_id(id="BL170339")
        po.scanmas_search_button()
        self.assertEqual(po.search_id_success_mas(), "BL170339")
        function.insert_img(self.driver, "scanmasid_search_successs.jpg")

    def test_search_scanmasmodel(self):
        """型号搜索"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_search_model(model="TG7788")
        po.scanmas_search_button()
        self.assertEqual(po.search_model_success_mas(), "TG7788")
        function.insert_img(self.driver, "scanmasmodel_search_successs.jpg")

    def test_search_scanmasmodelname(self):
        """型号名称搜索"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_search_model_name(model_name="MYDC022")
        po.scanmas_search_button()
        self.assertEqual(po.search_model_name_success_mas(), "MYDC022")
        function.insert_img(self.driver, "scanmasmodelname_search_successs.jpg")

    def test_scanmasnextpage(self):
        """下一页"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scanner?page=2')
        function.insert_img(self.driver, "scanmas_nextpage_success.jpg")

    def test_scanmaslastpage(self):
        """上一页"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_nextpage()
        po.scanmas_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/scanner?page=1')
        function.insert_img(self.driver, "scanmas_lastpage_success.jpg")

    def test_3_scanmasstatus(self):
        """启用/停用"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_open_stop_button()
        current_status = po.scanmas_status_info()
        self.assertEqual(current_status, u'停用')
        function.insert_img(self.driver, "scanmas_statusoff_success.jpg")
        po.scanmas_open_stop_button()
        current_status = po.scanmas_status_info()
        self.assertEqual(current_status, u'启用')
        function.insert_img(self.driver, "scanmas_statuson_success.jpg")

    def test_1_scanmasadd(self):
        """新增扫描仪"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_add(id="MK-6",model="Iron",model_name="Iron-Man",remark=u"这是钢铁侠",status="2")
        po.scanmas_search_id(id="MK-6")
        po.scanmas_search_button()
        self.assertEqual(po.scanmas_brand_info(),"DLO")
        self.assertEqual(po.scanmas_id_info(),"MK-6")
        self.assertEqual(po.scanmas_model_info(),"Iron")
        self.assertEqual(po.scanmas_model_name_info(),"Iron-Man")
        self.assertEqual(po.scanmas_status_info(),u"停用")
        function.insert_img(self.driver, "scanmas_add_success.jpg")

    def test_2_scanmasedit(self):
        """编辑扫描仪"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_edit(model="Spider",model_name="Spider-Man",remark=u"这是蜘蛛侠",status="1")
        po.scanmas_search_id(id="MK-6")
        po.scanmas_search_button()
        self.assertEqual(po.scanmas_brand_info(),"DLO")
        self.assertEqual(po.scanmas_id_info(),"MK-6")
        self.assertEqual(po.scanmas_model_info(),"Spider")
        self.assertEqual(po.scanmas_model_name_info(),"Spider-Man")
        self.assertEqual(po.scanmas_status_info(),u"启用")
        function.insert_img(self.driver, "scanmas_edit_success.jpg")

    def test_5_scanmasexport(self):
        """导出列表"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_search_id(id="23")
        po.scanmas_search_button()
        sleep(1)
        self.assertEqual(po.scanmas_export(),True)
        function.insert_img(self.driver, "scanmas_export_successs.jpg")

    def test_4_scanmasdelete(self):
        """删除扫描仪"""
        self.scanmas_login_verify()
        sleep(2)
        po = scanmas(self.driver)
        po.scanmas_search_id(id="MK-6")
        po.scanmas_search_button()
        po.scanmas_delete()#新添加扫描仪的id
        po.scanmas_search_id(id="MK-6")
        po.scanmas_search_button()
        sleep(2)
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody').find_elements(By.TAG_NAME,"tr")
        for i in table:
            p1 = (i.text).split(" ")
            for j in p1:
                self.assertNotEqual(j, "MK-6")
        function.insert_img(self.driver, "scanmas_delete_successs.jpg")


if __name__ == "__main__":
    unittest.main()
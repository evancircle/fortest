# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.faultPage import fault
from selenium.webdriver.common.by import By

class faultTest(myunit.MyTest):

    """故障记录测试"""
    def fault_login_verify(self,username="admin", password="000000"):
        fault(self.driver).surf_fault(username,password)

    def test_search_faultid(self):
        """设备编号搜索"""
        self.fault_login_verify()
        sleep(2)
        po = fault(self.driver)
        po.fault_search_id(id="BL170648")
        po.fault_search_button()
        sleep(1)
        self.assertEqual(po.search_id_success_mgt(), 'BL170648')
        function.insert_img(self.driver, "faultid_search_successs.jpg")

    def test_search_faultshopname(self):
        """门店名称搜索"""
        self.fault_login_verify()
        sleep(2)
        po = fault(self.driver)
        po.fault_search_shop_name(name=u"宜昌大洋百货BL")
        po.fault_search_button()
        sleep(1)
        self.assertEqual(po.search_shop_name_success_mgt(), u'宜昌大洋百货BL')
        function.insert_img(self.driver, "faultshopname_search_successs.jpg")

    def test_search_faultshopcode(self):
        """门店代码搜索"""
        self.fault_login_verify()
        sleep(2)
        po = fault(self.driver)
        po.fault_search_shop_code(code="CB62TM")
        po.fault_search_button()
        self.assertEqual(po.search_shop_code_success_mgt(), "CB62TM")
        function.insert_img(self.driver, "faultshopcode_search_successs.jpg")

    def test_search_faultstartdate(self):
        """开始日期搜索"""
        self.fault_login_verify()
        sleep(2)
        po = fault(self.driver)
        po.fault_search_startdate(sdate="2017-08-01")
        po.fault_search_button()
        po.fault_lostfocus()
        self.assertGreaterEqual(po.search_startdate_success_mgt(), "2017-08-01")
        function.insert_img(self.driver, "faultstartdate_search_successs.jpg")

    def test_search_faultenddate(self):
        """结束日期搜索"""
        self.fault_login_verify()
        sleep(2)
        po = fault(self.driver)
        po.fault_search_enddate(edate="2017-08-05")
        po.fault_lostfocus()
        po.fault_search_button()
        self.assertLessEqual(po.search_enddate_success_mgt(), "2017-08-05")
        function.insert_img(self.driver, "faultenddate_search_successs.jpg")

    def test_1_faultadd(self):
        """新增扫描仪"""
        self.fault_login_verify()
        sleep(2)
        po = fault(self.driver)
        po.fault_add(id="BL170619",code='CR69TM',name=u'哈尔滨香坊乐松TM',startdate="2017-08-15", enddate="2017-08-16", record=u"这是故障报告ABCD")
        po.fault_search_id(id="BL170619")
        po.fault_search_button()
        self.assertEqual(po.fault_id_info(), "BL170619")
        self.assertEqual(po.fault_shop_name_info(), u"哈尔滨香坊乐松TM")
        self.assertEqual(po.fault_code_info(), "CR69TM")
        self.assertEqual(po.fault_startdate_info(), "2017-08-15")
        self.assertEqual(po.fault_enddate_info(), "2017-08-16")
        self.assertEqual(po.fault_fault_info(), u"这是故障报告ABCD")
        function.insert_img(self.driver, "fault_add_success.jpg")

    def test_2_faultedit(self):
        """编辑扫描仪"""
        self.fault_login_verify()
        sleep(2)
        po = fault(self.driver)
        po.fault_edit(id="BL170579",code='L342ST',name=u'广州东方宝泰广场ST',startdate="2017-08-18",enddate="2017-08-20",record=u"故障报告DCBA")
        po.fault_search_id(id="BL170579")
        po.fault_search_button()
        self.assertEqual(po.fault_id_info(),"BL170579")
        self.assertEqual(po.fault_shop_name_info(),u"广州东方宝泰广场ST")
        self.assertEqual(po.fault_code_info(), "L342ST")
        self.assertEqual(po.fault_startdate_info(), "2017-08-18")
        self.assertEqual(po.fault_enddate_info(), "2017-08-20")
        self.assertEqual(po.fault_fault_info(), u"故障报告DCBA")
        function.insert_img(self.driver, "fault_edit_success.jpg")

    def test_faultexport(self):
        """导出列表"""
        self.fault_login_verify()
        sleep(2)
        po = fault(self.driver)
        self.assertTrue(po.fault_export(), True)
        function.insert_img(self.driver, "fault_export_successs.jpg")

    def test_3_faultdelete(self):
        """删除扫描仪"""
        self.fault_login_verify()
        sleep(2)
        po = fault(self.driver)
        po.fault_search_id(id="BL170579")
        po.fault_search_button()
        sleep(1)
        po.fault_delete()
        sleep(3)
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody').find_elements(By.TAG_NAME,"tr")
        for i in table:
            p1 = (i.text).split(" ")
            for j in p1:
                self.assertNotEqual(j, "BL170579")
        function.insert_img(self.driver, "fault_delete_successs.jpg")

if __name__ == "__main__":
    unittest.main()
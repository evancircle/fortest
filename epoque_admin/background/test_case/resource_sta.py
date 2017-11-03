# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
import os

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.resourcePage import resource
from selenium.webdriver.common.by import By


class resourceTest(myunit.MyTest):
    """资源管理测试"""

    def resource_login_verify(self, username="admin", password="000000"):
        resource(self.driver).surf_resource(username, password)

    def test_resource_1add(self):
        """新增菜单"""
        self.resource_login_verify()
        sleep(2)
        po = resource(self.driver)
        po.resource_add(part="3",resource="555",url="555",attach="555",module="2")
        po.resource_search(source="3")
        po.resource_search_button()
        self.assertEqual(po.resource_info_menuid6(), u"账号列表")
        self.assertEqual(po.resource_info_name6(), "555")
        self.assertEqual(po.resource_info_url6(), "555")
        self.assertEqual(po.resource_info_attach6(), "555")
        function.insert_img(self.driver, "resource_add_successs.jpg")

    def test_resource_3delete(self):
        """删除菜单"""
        self.resource_login_verify()
        sleep(2)
        po = resource(self.driver)
        po.resource_search(source="3")
        po.resource_search_button()
        sleep(1)
        delete_id = po.resource_info_id6()
        po.resource_delete(delete_id)
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody').find_elements(By.TAG_NAME,"tr")
        for i in table:
            p1 = (i.text).split(" ")
            for j in p1:
                self.assertNotEqual(j, "555")
        function.insert_img(self.driver, "shop_delete_successs.jpg")

    def test_resource_2edit(self):
        """编辑菜单"""
        self.resource_login_verify()
        sleep(2)
        po = resource(self.driver)
        po.resource_edit(resource=u"新增|查看|编辑666",url="admin/user/detail666",attach="admin/user/check-login-name666",module="2")
        po.resource_search(source="3")
        po.resource_search_button()
        self.assertEqual(po.resource_info_name1(), u"新增|查看|编辑666")
        self.assertEqual(po.resource_info_url1(), "admin/user/detail666")
        self.assertEqual(po.resource_info_attach1(), "admin/user/check-login-name666")
        po.resource_edit(resource=u"新增|查看|编辑", url="admin/user/detail", attach="admin/user/check-login-name",module="1")
        po.resource_search(source="3")
        po.resource_search_button()
        self.assertEqual(po.resource_info_name1(), u"新增|查看|编辑")
        self.assertEqual(po.resource_info_url1(), "admin/user/detail")
        self.assertEqual(po.resource_info_attach1(), "admin/user/check-login-name")
        function.insert_img(self.driver, "resource_edit_successs.jpg")

if __name__ == "__main__":
    unittest.main()

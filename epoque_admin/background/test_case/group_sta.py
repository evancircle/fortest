# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
import os

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.groupPage import group
from selenium.webdriver.common.by import By


class groupTest(myunit.MyTest):
    """组织架构测试"""

    def group_login_verify(self, username="admin", password="000000"):
        group(self.driver).surf_group(username, password)

    def test_group_1add(self):
        """新增菜单"""
        self.group_login_verify()
        sleep(2)
        po = group(self.driver)
        po.group_add(name='new_group',group='3')
        self.assertEqual(po.group_info_group4(), u"  |——————  new_group")
        function.insert_img(self.driver, "group_add_successs.jpg")

    def test_group_3delete(self):
        """删除菜单"""
        self.group_login_verify()
        sleep(2)
        po = group(self.driver)
        po.group_delete()
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[2]/div/div/div/div/table/tbody').find_elements(By.TAG_NAME,"tr")
        for i in table:
            p1 = (i.text).split(" ")
            for j in p1:
                self.assertNotEqual(j, u"  |———  new_group_edit")
        function.insert_img(self.driver, "shop_delete_successs.jpg")

    def test_group_2edit(self):
        """编辑菜单"""
        self.group_login_verify()
        sleep(2)
        po = group(self.driver)
        po.group_edit(name='new_group_edit', group='2')
        self.assertEqual(po.group_info_group7(), u"  |———  new_group_edit")
        function.insert_img(self.driver, "group_edit_successs.jpg")

if __name__ == "__main__":
    unittest.main()

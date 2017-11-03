# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
import os

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.menuPage import menu
from selenium.webdriver.common.by import By


class menuTest(myunit.MyTest):
    """菜单管理测试"""

    def menu_login_verify(self, username="admin", password="000000"):
        menu(self.driver).surf_menu(username, password)

    def test_menu_1add(self):
        """新增菜单"""
        self.menu_login_verify()
        sleep(2)
        po = menu(self.driver)
        po.menu_add(part="1",menu="555",url="555",classname="555",sort="0",module="2")
        self.assertEqual(po.menu_info_name(), "555")
        self.assertEqual(po.menu_info_url(), "555")
        self.assertEqual(po.menu_info_classname(), "555")
        self.assertEqual(po.menu_info_sort(), "0")
        function.insert_img(self.driver, "menu_add_successs.jpg")

    def test_menu_3delete(self):
        """删除菜单"""
        self.menu_login_verify()
        sleep(2)
        po = menu(self.driver)
        delete_id = po.menu_info_id()
        po.menu_delete(delete_id)
        self.assertNotEqual(po.menu_info_name(), "666")
        function.insert_img(self.driver, "menu_delete_successs.jpg")

    def test_menu_2edit(self):
        """编辑菜单"""
        self.menu_login_verify()
        sleep(2)
        po = menu(self.driver)
        delete_id = po.menu_info_id()
        po.menu_edit(part="1",menu="666",url="666",classname="666",module="1")
        self.assertEqual(po.menu_info_name(), "666")
        self.assertEqual(po.menu_info_url(), "666")
        self.assertEqual(po.menu_info_classname(), "666")
        function.insert_img(self.driver, "menu_edit_successs.jpg")

if __name__ == "__main__":
    unittest.main()

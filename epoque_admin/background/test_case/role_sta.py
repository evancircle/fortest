# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
import os

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.rolePage import role
from selenium.webdriver.common.by import By


class roleTest(myunit.MyTest):
    """角色管理测试"""

    def role_login_verify(self, username="admin", password="000000"):
        role(self.driver).surf_role(username, password)

    def test_role_1add(self):
        """新增菜单"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_add(group="2",name="new_role",shop="1",city="1")
        po.role_search_name(name="new_role")
        po.role_search_button()
        self.assertEqual(po.role_info_group(), "epoque")
        self.assertEqual(po.role_info_role(), "new_role")
        function.insert_img(self.driver, "role_add_successs.jpg")

    def test_role_6delete(self):
        """删除菜单"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_search_name(name="new_role_edit")
        po.role_search_button()
        sleep(1)
        po.role_delete()
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div/table/tbody').find_elements(By.TAG_NAME,"tr")
        for i in table:
            p1 = (i.text).split(" ")
            for j in p1:
                self.assertNotEqual(j, "new_role_edit")
        function.insert_img(self.driver, "shop_delete_successs.jpg")

    def test_role_2edit(self):
        """编辑菜单"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_edit(group="3",name="new_role_edit",shop="1",city="1")
        po.role_search_name(name="new_role_edit")
        po.role_search_button()
        self.assertEqual(po.role_info_group(), u"运营")
        self.assertEqual(po.role_info_role(), "new_role_edit")
        function.insert_img(self.driver, "role_edit_successs.jpg")

    def test_role_3setmenu(self):
        """修改菜单权限"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_search_name(name="new_role_edit")
        po.role_search_button()
        po.role_set_menu()
        sleep(2)
        self.assertEqual(po.role_info_menu(), 'button chk checkbox_true_full')
        function.insert_img(self.driver, "role_setmenu_successs.jpg")

    def test_role_4setcity(self):
        """修改城市权限"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_search_name(name="new_role_edit")
        po.role_search_button()
        po.role_set_city()
        sleep(2)
        self.assertEqual(po.role_info_city(), 'button chk checkbox_true_full')
        function.insert_img(self.driver, "role_setshop_successs.jpg")


    def test_role_5setshop(self):
        """修改门店权限"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_search_name(name="new_role_edit")
        po.role_search_button()
        po.role_set_shop(shop="K436BL")
        sleep(2)
        po.role_search_name(name="new_role_edit")
        po.role_search_button()
        self.assertEqual(po.role_info_shop(shop='K436BL'), 'true')
        function.insert_img(self.driver, "role_setcity_successs.jpg")

    def test_role_shopnextpage(self):
        """下一页"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/role/index?page=2')
        function.insert_img(self.driver, "role_nextpage_success.jpg")

    def test_role_shoplastpage(self):
        """上一页"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_nextpage()
        po.role_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/role/index?page=1')
        function.insert_img(self.driver, "role_lastpage_success.jpg")

    def test_role_groupsearch(self):
        """角色组织搜索"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_search_group(group="3")
        po.role_search_button()
        self.assertEqual(po.role_info_group(), u"运营")
        function.insert_img(self.driver, "role_search_group_successs.jpg")

    def test_role_namesearch(self):
        """角色名称搜索"""
        self.role_login_verify()
        sleep(2)
        po = role(self.driver)
        po.role_search_name(name=u"测试")
        po.role_search_button()
        self.assertEqual(po.role_info_role(), u"测试二级")
        function.insert_img(self.driver, "role_search_name_successs.jpg")



if __name__ == "__main__":
    unittest.main()

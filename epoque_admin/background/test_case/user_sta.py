# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.userPage import user
from selenium.webdriver.common.by import By

class userTest(myunit.MyTest):

    """账号权限管理测试"""
    def user_login_verify(self,username="admin", password="000000"):
        user(self.driver).surf_user(username,password)

    def test_search_user(self):
        """姓名搜索"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        po.user_search_username(username=u"团团团")
        po.user_search_button()
        self.assertEqual(po.search_username_success(), u'团团团')
        function.insert_img(self.driver, "username_search_successs.jpg")

    def test_search_loginname(self):
        """账号搜索"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        po.user_search_loginname(loginname="evan")
        po.user_search_button()
        self.assertEqual(po.search_loginname_success(), "evan")
        function.insert_img(self.driver, "loginname_search_successs.jpg")

    def test_search_organization(self):
        """组织搜索"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        po.user_organization(organization='4')
        po.user_search_button()
        sleep(1)
        self.assertEqual(po.search_organization_success(), u"运营下级")
        function.insert_img(self.driver, "organization_search_successs.jpg")

    def test_search_part(self):
        """角色搜索"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        po.user_part(organization='2',part='2')
        po.user_search_button()
        self.assertEqual(po.search_part_success(), u"管理员")
        function.insert_img(self.driver, "part_search_successs.jpg")

    def test_3userdelete(self):
        """删除账号"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        po.user_search_username(username="ooo")
        po.user_search_button()
        po.user_delete()
        po.user_search_username(username="ooo")
        po.user_search_button()
        table = self.driver.find_element_by_xpath("//*[@id='wrap']/div/div[2]/div/div/div[1]/div/div/table/tbody").find_elements(By.TAG_NAME,"tr")
        for i in table:
            p1 = (i.text).split(" ")
            for j in p1:
                self.assertNotEqual(j, "bbb")
        function.insert_img(self.driver, "user_delete_successs.jpg")

    def test_userreset(self):
        """重置密码"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        reset_loginname = po.search_loginname_success()
        add_part = po.search_part_success()
        add_organization = po.search_organization_success()
        po.user_reset_password(usernumber='2')
        po.logout()
        self.user_login_verify(reset_loginname,"000000")
        self.assertEqual(po.login_message(),u'登录人：%s    所属组织：%s    所属角色：%s'%(reset_loginname,add_organization,add_part))
        function.insert_img(self.driver, "user_reset_success.jpg")

    def test_usernextpage(self):
        """下一页"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        po.user_nextpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/account?page=2')
        function.insert_img(self.driver, "user_nextpage_success.jpg")

    def test_userlastpage(self):
        """上一页"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        po.user_nextpage()
        po.user_lastpage()
        afterpage = self.driver.current_url
        self.assertEqual(afterpage, 'http://bossdev.epoque.cn/admin/account?page=1')
        function.insert_img(self.driver, "user_lastpage_success.jpg")

    def test_1useradd(self):
        """新增账号"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        po.user_add(loginname="aaa",username="bbb",organization='3',part='2',emael="kaka@163.com",address="GuangDong",telephone="13800138000")
        po.user_search_username(username="bbb")
        po.user_search_button()
        add_loginname = po.search_loginname_success()
        add_part = po.search_part_success()
        add_organization = po.search_organization_success()
        self.assertEqual(po.search_username_success(), 'bbb')
        po.logout()
        self.user_login_verify("aaa", "000000")
        self.assertEqual(po.login_message(),u'登录人：%s    所属组织：%s    所属角色：%s'%(add_loginname,add_organization,add_part))
        function.insert_img(self.driver, "user_add_success.jpg")

    def test_2useredit(self):
        """编辑账号"""
        self.user_login_verify()
        sleep(2)
        po = user(self.driver)
        po.user_edit(username="ooo",organization='2',part='2',email="okok@163.com",address="USA",telephone="13600136000")
        self.driver.find_element_by_xpath("//*[@id='wrap']/div/div[2]/div/div/div[1]/div/div/table/tbody/tr[1]/td[7]/a[1]").click()#进入编辑页查看信息
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='account']/div[2]/div/input").get_attribute("value"), 'ooo')
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='account']/div[3]/div/div/div[1]/div").text, "epoque")
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='account']/div[4]/div/div/div[1]/div").text, u"管理员")
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='account']/div[5]/div/div/input").get_attribute("value"),"okok@163.com")
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='account']/div[6]/div/input").get_attribute("value"),"USA")
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='account']/div[7]/div/input").get_attribute("value"), "13600136000")
        function.insert_img(self.driver, "user_edit_success.jpg")

if __name__ == "__main__":
    unittest.main()
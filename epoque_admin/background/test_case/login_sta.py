# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):

    '''后台登录测试'''

    def user_login_verify(self,username='',password=''):
        login(self.driver).user_login(username,password)

    def test_login1(self):
        """用户名、密码为空"""
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.error_hint(),u'用户名不能为空')
        function.insert_img(self.driver,"user_paws_empty.jpg")

    def test_login2(self):
        """密码为空"""
        self.user_login_verify(username="admin")
        po = login(self.driver)
        self.assertEqual(po.error_hint(),u'密码不能为空')
        function.insert_img(self.driver,"paws_empty.jpg")

    def test_login3(self):
        """用户名为空"""
        self.user_login_verify(password="000000")
        po = login(self.driver)
        self.assertEqual(po.error_hint(),u'用户名不能为空')
        function.insert_img(self.driver,"user_empty.jpg")

    def test_login4(self):
        """密码错误"""
        character = random.choice('qwertyuiopasdfghjklzxcvbnm')
        password='000000'+character
        self.user_login_verify(username="admin",password=password)
        po = login(self.driver)
        self.assertEqual(po.error_hint(),u'输入的用户名密码错误，请重新输入')
        function.insert_img(self.driver,"user_pawd_error.jpg")

    def test_login5(self):
        """用户名、密码、验证码正确"""
        self.user_login_verify(username="admin",password="000000")
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.login_success(),u'登录人：admin    所属组织：epoque    所属角色：总管理员')
        function.insert_img(self.driver,"user_pawd_true.jpg")

if __name__ == "__main__":
    unittest.main()

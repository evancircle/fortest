# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Page

class login(Page):

    url = '/login'

    login_username_loc = (By.ID,'username')#账号编辑框
    login_password_loc = (By.ID, 'password')#密码编辑框
    login_button_loc = (By.ID, 'login_submit')#登录按钮
    login_codebox_loc = (By.ID,"code_box")#验证码位置
    login_code_loc = (By.XPATH,"//*[@id='code']")#验证码编辑框
    hint_loc = (By.XPATH,"//*[@id='login']/div[3]/div/div/div[1]/div")#错误提示
    login_success_loc = (By.XPATH,"//*[@id='page-content']/header/div/div/a/span")#登录成功验证

    #输入账号
    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    #输入密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    #输入验证码
    def login_code(self,*args):
        innerText = self.find_element(*self.login_codebox_loc).get_attribute('innerText')#获取验证码
        self.find_element(*self.login_code_loc).send_keys(innerText)#输入验证码

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #登录后台
    def user_login(self,username,password):
        self.open()
        sleep(5)
        self.login_username(username)
        self.login_password(password)
        self.login_code()
        self.login_button()
        sleep(1)

    #错误提示
    def error_hint(self):
        return self.find_element(*self.hint_loc).text

    #登录成功验证
    def login_success(self):
        return self.find_element(*self.login_success_loc).text



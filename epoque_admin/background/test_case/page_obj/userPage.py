# -*- coding: utf-8 -*-
import email

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class user(Page):

    url = "/admin/account"

    user_serrch_username_loc = (By.NAME,"nickname")#姓名搜索框
    user_search_loginname_loc = (By.NAME,"username")#账号搜索框
    user_search_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[2]/div/div[1]')#查询按钮
    user_delete_comfirm_loc = (By.XPATH,"/html/body/div[3]/div/div/div[2]/button[2]")#删除确认按钮
    user_delete_ok_loc = (By.XPATH,"/html/body/div[3]/div/div/div[2]/button")#删除成功按钮
    user_add_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[2]/div/div[2]')#新增按钮
    user_edit_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/div/table/tbody/tr[1]/td[7]/a[1]')#编辑按钮
    user_nextpage_loc = (By.LINK_TEXT,u'下一頁')#下一页按钮
    user_lastpage_loc = (By.LINK_TEXT,u'上一頁')#上一页按钮
    user_reset_comfirm_loc = (By.XPATH,"/html/body/div[3]/div/div/div[2]/button[2]")#确认重置按钮
    user_organization_loc = (By.XPATH,"//*[@id='epoque-search']/div/div[1]/div[3]/div/div/div[1]/div")#组织搜索框
    user_part_loc = (By.XPATH,"//*[@id='epoque-search']/div/div[1]/div[4]/div/div/div[1]/div")#角色搜索框
    user_info_username = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/div/table/tbody/tr[1]/td[2]')#列表第一行的姓名
    user_info_loginname = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/div/table/tbody/tr[1]/td[3]')#列表第一行的账号
    user_info_organization = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/div/table/tbody/tr[1]/td[4]')#列表第一行的组织
    user_info_part = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/div/table/tbody/tr[1]/td[5]')#列表第一行的角色
    user_reset_ok_loc = (By.XPATH,"/html/body/div[3]/div/div/div[2]/button")#重置成功按钮
    index_loginname_loc = (By.XPATH,"//*[@id='page-content']/header/div/div/a/span")#首页右上角登录名
    #index_user_operation_button = (By.XPATH,"//*[@id='page-content']/header/div/div/a/span/i")#首页右上角账号操作按钮
    index_user_logout_button = (By.ID,"logout-btn")#首页右上角账号退出按钮
    add_edit_loginname_loc = (By.XPATH, "//*[@id='account']/div[1]/div/input")#新增/编辑页面的账号编辑框
    add_edit_username_loc = (By.XPATH, "//*[@id='account']/div[2]/div/input")#新增/编辑页面的姓名编辑框
    add_edit_email_loc = (By.XPATH, "//*[@id='account']/div[5]/div/div/input")#新增/编辑页面的邮箱编辑框
    add_edit_address_loc = (By.XPATH, "//*[@id='account']/div[6]/div/input")#新增/编辑页面的地址编辑框
    add_edit_telephone_loc = (By.XPATH, "//*[@id='account']/div[7]/div/input")#新增/编辑页面的联系方式编辑框
    add_edit_save_button_loc = (By.XPATH, "//*[@id='save-btn']")#新增/编辑页面的保存按钮
    add_edit_ok_button_loc = (By.XPATH, "/html/body/div[3]/div/div/div[2]/button")#新增/编辑页面保存成功后的ok按钮

    #姓名搜索
    def user_search_username(self,username):
        sleep(1)
        self.find_element(*self.user_serrch_username_loc).clear()
        sleep(1)
        self.find_element(*self.user_serrch_username_loc).send_keys(username)
    def search_username_success(self):
        sleep(1)
        return self.find_element(*self.user_info_username).text

    #账号搜索
    def user_search_loginname(self,loginname):
        sleep(1)
        self.find_element(*self.user_search_loginname_loc).clear()
        sleep(1)
        self.find_element(*self.user_search_loginname_loc).send_keys(loginname)
    def search_loginname_success(self):
        sleep(1)
        return self.find_element(*self.user_info_loginname).text

    #组织搜索
    def user_organization(self,organization):
        sleep(1)
        self.find_element(*self.user_organization_loc).click()
        sleep(1)
        organizations = self.driver.find_element_by_name('groupid')
        sleep(1)
        organizations.find_element_by_xpath("//*[@id='epoque-search']/div/div[1]/div[3]/div/div/div[2]/div/div[%s]"%organization).click()
        sleep(1)
    def search_organization_success(self):
        sleep(1)
        return self.find_element(*self.user_info_organization).text

    #角色搜索
    def user_part(self,organization,part):
        sleep(1)
        self.find_element(*self.user_organization_loc).click()
        sleep(1)
        organizations = self.driver.find_element_by_name('groupid')
        sleep(1)
        organizations.find_element_by_xpath("//*[@id='epoque-search']/div/div[1]/div[3]/div/div/div[2]/div/div[%s]"%organization).click()
        sleep(1)
        self.find_element(*self.user_part_loc).click()
        parts = self.driver.find_element_by_name('roleid')
        sleep(1)
        parts.find_element_by_xpath("//*[@id='epoque-search']/div/div[1]/div[4]/div/div/div[2]/div/div[%s]"%part).click()
        sleep(1)
    def search_part_success(self):
        sleep(1)
        return self.find_element(*self.user_info_part).text

    #删除
    def user_delete(self):
        sleep(1)
        self.driver.find_element_by_class_name('delete-btn').click()
        sleep(1)
        self.find_element(*self.user_delete_comfirm_loc).click()
        sleep(1)
        self.find_element(*self.user_delete_ok_loc).click()

    #重置密码
    def user_reset_password(self,usernumber):
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='wrap']/div/div[2]/div/div/div[1]/div/div/table/tbody/tr[%s]/td[7]/button"%usernumber).click()
        sleep(1)
        self.find_element(*self.user_reset_comfirm_loc).click()
        sleep(1)
        self.find_element(*self.user_reset_ok_loc).click()

    #下一页
    def user_nextpage(self):
        sleep(1)
        self.find_element(*self.user_nextpage_loc).click()

    #上一页
    def user_lastpage(self):
        sleep(1)
        self.find_element(*self.user_lastpage_loc).click()

    #查询按钮
    def user_search_button(self):
        sleep(1)
        self.find_element(*self.user_search_button_loc).click()
        sleep(2)

    #新增账号
    def user_add(self,loginname,username,organization,part,emael,address,telephone):
        sleep(1)
        self.find_element(*self.user_add_loc).click()
        sleep(1)
        self.find_element(*self.add_edit_loginname_loc).send_keys(loginname)#输入账号
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='checkUserName']").click()#用户名检测
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button").click()
        sleep(2)
        self.find_element(*self.add_edit_username_loc).send_keys(username)#输入姓名
        #-------组织选择-------
        self.driver.find_element_by_xpath("//*[@id='account']/div[3]/div/div/div[1]/div").click()
        sleep(1)
        organizations = self.driver.find_element_by_name('groupid')
        sleep(1)
        organizations.find_element_by_xpath("//*[@id='account']/div[3]/div/div/div[2]/div/div[%s]" % organization).click()
        sleep(1)
        #-------角色选择-------
        self.driver.find_element_by_xpath("//*[@id='account']/div[4]/div/div/div[1]/div").click()
        sleep(1)
        parts = self.driver.find_element_by_name('roleid')
        sleep(1)
        parts.find_element_by_xpath("//*[@id='account']/div[4]/div/div/div[2]/div/div[%s]" % part).click()
        sleep(1)
        #----------------------
        self.find_element(*self.add_edit_email_loc).send_keys(emael)#输入邮箱
        self.find_element(*self.add_edit_address_loc).send_keys(address)#输入地址
        self.find_element(*self.add_edit_telephone_loc).send_keys(telephone)#输入电话
        self.find_element(*self.add_edit_save_button_loc).click()#点击保存
        self.find_element(*self.add_edit_ok_button_loc).click()#点击ok

    #查看/编辑账号
    def user_edit(self,username,organization,part,email,address,telephone):
        sleep(1)
        self.find_element(*self.user_edit_loc).click()
        sleep(1)
        self.find_element(*self.add_edit_username_loc).clear()#姓名编辑框清空
        sleep(1)
        self.find_element(*self.add_edit_username_loc).send_keys(username)#修改姓名
        sleep(1)
        #-------组织修改-------
        self.driver.find_element_by_xpath("//*[@id='account']/div[3]/div/div/div[1]/div").click()
        sleep(1)
        organizations = self.driver.find_element_by_name('groupid')
        sleep(1)
        organizations.find_element_by_xpath("//*[@id='account']/div[3]/div/div/div[2]/div/div[%s]" % organization).click()
        sleep(1)
        #-------角色修改-------
        self.driver.find_element_by_xpath("//*[@id='account']/div[4]/div/div/div[1]/div").click()
        sleep(1)
        parts = self.driver.find_element_by_name('roleid')
        sleep(1)
        parts.find_element_by_xpath("//*[@id='account']/div[4]/div/div/div[2]/div/div[%s]" % part).click()
        sleep(1)
        #----------------------
        self.find_element(*self.add_edit_email_loc).clear()#邮箱编辑框清空
        self.find_element(*self.add_edit_email_loc).send_keys(email)#修改邮箱
        self.find_element(*self.add_edit_address_loc).clear()#地址编辑框清空
        self.find_element(*self.add_edit_address_loc).send_keys(address)#修改地址
        self.find_element(*self.add_edit_telephone_loc).clear()#电话编辑框清空
        self.find_element(*self.add_edit_telephone_loc).send_keys(telephone)#修改电话
        self.find_element(*self.add_edit_save_button_loc).click()#保存
        self.find_element(*self.add_edit_ok_button_loc).click()#点击ok

    # 访问账号权限管理
    def surf_user(self, username='admin', password='000000'):
        self.driver.get('http://bossdev.epoque.cn/login')
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_xpath(u"//input[@value='登录']").click()
        self.driver.get('http://bossdev.epoque.cn/admin/account')
        self.open()

    #退出登陆
    def logout(self):
        sleep(1)
        self.find_element(*self.index_loginname_loc).click()
        sleep(1)
        self.find_element(*self.index_user_logout_button).click()

    #右上角登录名
    def login_message(self):
        return self.find_element(*self.index_loginname_loc).text

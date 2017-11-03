# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class role(Page):

    url = "/admin/role/index"

    role_search_button_loc = (By.XPATH,'//*[@id="formsearch"]/div/div/div[3]/div[1]')
    role_add_button_loc = (By.XPATH,'//*[@id="formsearch"]/div/div/div[3]/div[2]')
    role_edit_button_loc = (By.XPATH,"//*[@id='wrap']/div[1]/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[7]/a[1]")
    role_group_info = (By.XPATH,"//*[@id='wrap']/div[1]/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[2]")
    role_role_info = (By.XPATH, "//*[@id='wrap']/div[1]/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]")
    role_menu_set = (By.XPATH, "//*[@id='wrap']/div[1]/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]/a")
    role_city_set = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[5]/a')
    role_shop_set = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[6]/a')
    role_search_loc = (By.XPATH, '//*[@id="formsearch"]/div/div/div[1]/div/div[1]/div')
    role_name_search_loc = (By.XPATH,'//*[@id="formsearch"]/div/div/div[2]/input')
    role_nextpage_loc = (By.LINK_TEXT, u'下一頁')  # 下一页按钮
    role_lastpage_loc = (By.LINK_TEXT, u'上一頁')  # 上一页按钮
    role_add_edit_group = (By.XPATH,'//*[@id="formData"]/div[1]/div/div/div[1]/div')
    role_add_edit_name = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-6 input[name="name"]')
    role_add_edit_city = (By.XPATH,'//*[@id="formData"]/div[3]/div/div/div[1]/div')
    role_add_edit_shop = (By.XPATH, '//*[@id="formData"]/div[4]/div/div/div[1]/div')
    role_add_edit_save_button = (By.CSS_SELECTOR, 'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.panel-footer.f-detail-footbtn div.row div.btn-toolbar button#save-btn.btn.f-default-btn')

    role_delete_button_loc = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[7]/a[2]')

    #所属组织
    def role_info_group(self):
        sleep(1)
        return self.find_element(*self.role_group_info).text

    #所属角色
    def role_info_role(self):
        sleep(1)
        return self.find_element(*self.role_role_info).text

    #菜单+资源权限
    def role_info_menu(self):
        sleep(1)
        self.find_element(*self.role_menu_set).click()
        sleep(1)
        return self.driver.find_element_by_id('treeDemo_1_check').get_attribute("class")

    #城市数据权限
    def role_info_city(self):
        sleep(1)
        self.find_element(*self.role_city_set).click()
        sleep(1)
        return self.driver.find_element_by_id('shopsTreeDemo_1_check').get_attribute("class")

    #门店数据权限
    def role_info_shop(self, shop):
        sleep(1)
        roleid = self.driver.find_element_by_xpath('html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/table/tbody/tr/td[1]').text
        self.driver.get('http://bossdev.epoque.cn/admin/role/shopsData?roleid=%s' % roleid)
        sleep(3)
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div/form/div/div/div[1]/input').clear()
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div/form/div/div/div[1]/input').send_keys(shop)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[8]/div').click()
        sleep(1)
        return self.driver.find_element_by_css_selector('.table.table-striped.table-bordered.datatables>tbody>tr>td>input[shopcode="%s"]'%shop).get_attribute("checked")

    #菜单+资源权限设置
    def role_set_menu(self):
        sleep(1)
        self.find_element(*self.role_menu_set).click()
        sleep(1)
        js = 'document.getElementById("treeDemo_1_check").click()'
        self.driver.execute_script(js)
        self.driver.find_element_by_css_selector('html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#menuData.form-horizontal div.panel-footer.f-detail-footbtn div.row div.btn-toolbar button#save-menu.btn.f-default-btn').click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    #城市数据权限设置
    def role_set_city(self):
        sleep(1)
        self.find_element(*self.role_city_set).click()
        sleep(1)
        js = 'document.getElementById("shopsTreeDemo_1_check").click()'
        self.driver.execute_script(js)
        self.driver.find_element_by_css_selector('html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#shopsData.form-horizontal div.panel-footer.f-detail-footbtn div.row div.btn-toolbar button#save-menu.btn.f-default-btn').click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    #门店数据权限设置
    def role_set_shop(self,shop):
        sleep(1)
        roleid = self.driver.find_element_by_xpath('html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/table/tbody/tr/td[1]').text
        self.driver.get('http://bossdev.epoque.cn/admin/role/shopsData?roleid=%s'%roleid)
        sleep(3)
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div/form/div/div/div[1]/input').clear()
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div/form/div/div/div[1]/input').send_keys(shop)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[8]/div').click()
        sleep(1)
        self.driver.find_element_by_css_selector('.table.table-striped.table-bordered.datatables>tbody>tr>td>input[shopcode="%s"]'%shop).click()
        sleep(3)
        self.driver.get('http://bossdev.epoque.cn/admin/role/index')

    #编辑菜单
    def role_edit(self,group,name,city,shop):
        sleep(1)
        self.find_element(*self.role_edit_button_loc).click()
        sleep(1)
        self.find_element(*self.role_add_edit_group).click()
        sleep(1)
        groups = self.driver.find_element_by_name('groupid')
        groups.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[2]/div/div[%s]' % group).click()
        sleep(1)
        self.find_element(*self.role_add_edit_name).clear()
        sleep(1)
        self.find_element(*self.role_add_edit_name).send_keys(name)
        sleep(1)
        self.find_element(*self.role_add_edit_city).click()
        sleep(1)
        citys = self.driver.find_element_by_name('city_auth')
        citys.find_element_by_xpath('//*[@id="formData"]/div[3]/div/div/div[2]/div/div[%s]' % city).click()
        sleep(1)
        self.find_element(*self.role_add_edit_shop).click()
        sleep(1)
        shops = self.driver.find_element_by_name('shop_auth')
        shops.find_element_by_xpath('//*[@id="formData"]/div[4]/div/div/div[2]/div/div[%s]' % shop).click()
        sleep(1)
        self.find_element(*self.role_add_edit_save_button).click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    #删除菜单
    def role_delete(self):
        sleep(1)
        self.find_element(*self.role_delete_button_loc).click()
        sleep(1)
        comfirm = self.driver.switch_to_alert()
        sleep(1)
        comfirm.accept()
        complete = self.driver.switch_to_alert()
        sleep(1)
        complete.accept()

    #新增菜单
    def role_add(self,group,name,city,shop):
        sleep(1)
        self.find_element(*self.role_add_button_loc).click()
        sleep(1)
        self.find_element(*self.role_add_edit_group).click()
        sleep(1)
        groups = self.driver.find_element_by_name('groupid')
        groups.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[2]/div/div[%s]'% group).click()
        sleep(1)
        self.find_element(*self.role_add_edit_name).clear()
        sleep(1)
        self.find_element(*self.role_add_edit_name).send_keys(name)
        sleep(1)
        self.find_element(*self.role_add_edit_city).click()
        sleep(1)
        citys = self.driver.find_element_by_name('city_auth')
        citys.find_element_by_xpath('//*[@id="formData"]/div[3]/div/div/div[2]/div/div[%s]'% city).click()
        sleep(1)
        self.find_element(*self.role_add_edit_shop).click()
        sleep(1)
        shops = self.driver.find_element_by_name('shop_auth')
        shops.find_element_by_xpath('//*[@id="formData"]/div[4]/div/div/div[2]/div/div[%s]'% shop).click()
        sleep(1)
        self.find_element(*self.role_add_edit_save_button).click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    #登录访问角色管理
    def surf_role(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get("http://bossdev.epoque.cn/auth/role/index")
        self.open()

    #查询按钮
    def role_search_button(self):
        sleep(1)
        self.find_element(*self.role_search_button_loc).click()

    #所属角色搜索
    def role_search_group(self,group):
        sleep(1)
        self.find_element(*self.role_search_loc).click()
        sleep(1)
        role = self.driver.find_element_by_name('groupid')
        sleep(1)
        role.find_element_by_xpath('//*[@id="formsearch"]/div/div/div[1]/div/div[2]/div/div[%s]' % group).click()
        sleep(1)

    #角色名称搜索
    def role_search_name(self,name):
        sleep(1)
        self.find_element(*self.role_name_search_loc).clear()
        sleep(1)
        self.find_element(*self.role_name_search_loc).send_keys(name)
        sleep(1)

    #下一页
    def role_nextpage(self):
        sleep(1)
        self.find_element(*self.role_nextpage_loc).click()

    #上一页
    def role_lastpage(self):
        sleep(1)
        self.find_element(*self.role_lastpage_loc).click()
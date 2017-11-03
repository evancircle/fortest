# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class group(Page):

    url = "/admin/group/index"

    group_add_button_loc = (By.XPATH,'//*[@id="wrap"]/div[1]/div[1]/div/div/div')
    group_edit_button_loc = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div/div/div/table/tbody/tr[4]/td[3]/a[1]')
    group_group7 = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div/div/div/table/tbody/tr[7]/td[2]')
    group_group4 = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div/div/div/table/tbody/tr[4]/td[2]')
    group_add_edit_parentid = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-6 div.selectize-control.selectize.single div.selectize-input.items.full.has-options.has-items div.item')
    group_add_edit_name = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-6 input[name="name"]')
    group_add_edit_save_button = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.panel-footer.f-detail-footbtn div.row div.btn-toolbar button#save-btn.btn.f-default-btn')

    def group_info_group4(self):
        sleep(1)
        return self.find_element(*self.group_group4).text

    def group_info_group7(self):
        sleep(1)
        return self.find_element(*self.group_group7).text

    #编辑菜单
    def group_edit(self,name,group):
        sleep(1)
        self.find_element(*self.group_edit_button_loc).click()
        sleep(1)
        self.find_element(*self.group_add_edit_parentid).click()
        sleep(1)
        parts = self.driver.find_element_by_name('parentid')
        parts.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[2]/div/div[%s]' % group).click()
        sleep(1)
        self.find_element(*self.group_add_edit_name).clear()
        sleep(1)
        self.find_element(*self.group_add_edit_name).send_keys(name)
        sleep(1)
        self.find_element(*self.group_add_edit_save_button).click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    #删除菜单
    def group_delete(self):
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[2]/div/div/div/div/table/tbody/tr[7]/td[3]/a[2]').click()
        sleep(1)
        comfirm = self.driver.switch_to_alert()
        sleep(1)
        comfirm.accept()
        complete = self.driver.switch_to_alert()
        sleep(1)
        complete.accept()

    #新增菜单
    def group_add(self,name,group):
        sleep(1)
        self.find_element(*self.group_add_button_loc).click()
        sleep(1)
        self.find_element(*self.group_add_edit_parentid).click()
        sleep(1)
        parts = self.driver.find_element_by_name('parentid')
        parts.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[2]/div/div[%s]' % group).click()
        sleep(1)
        self.find_element(*self.group_add_edit_name).clear()
        sleep(1)
        self.find_element(*self.group_add_edit_name).send_keys(name)
        sleep(1)
        self.find_element(*self.group_add_edit_save_button).click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    def surf_group(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get('http://bossdev.epoque.cn/admin/group/index')
        self.open()
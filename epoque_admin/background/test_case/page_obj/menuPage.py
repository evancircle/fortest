# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class menu(Page):

    url = "/admin/menu/index"

    menu_add_button_loc = (By.XPATH,'//*[@id="wrap"]/div[1]/div[1]/div/div/div')
    menu_edit_button_loc = (By.LINK_TEXT,u"编辑")
    menu_id_info = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]')
    menu_name_info = (By.XPATH,"//*[@id='wrap']/div[1]/div[2]/div/div/div/div[1]/table/tbody/tr[1]/td[2]")
    menu_url_info = (By.XPATH, "//*[@id='wrap']/div[1]/div[2]/div/div/div/div[1]/table/tbody/tr[1]/td[3]")
    menu_classname_info = (By.XPATH, "//*[@id='wrap']/div[1]/div[2]/div/div/div/div[1]/table/tbody/tr[1]/td[4]")
    menu_sort_info = (By.XPATH, "//*[@id='wrap']/div[1]/div[2]/div/div/div/div[1]/table/tbody/tr[1]/td[5]")
    menu_add_edit_name = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-6 input[name="name"]')
    menu_add_edit_url = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-6 input[name="url"]')
    menu_add_edit_classname = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-6 input[name="classname"]')
    menu_add_edit_sort = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-6 input[name="sort"]')
    menu_add_edit_save_button = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.panel-footer.f-detail-footbtn div.row div.btn-toolbar button#save-btn.btn.f-default-btn')

    def menu_info_id(self):
        sleep(1)
        return self.find_element(*self.menu_id_info).text

    def menu_info_name(self):
        sleep(1)
        return self.find_element(*self.menu_name_info).text

    def menu_info_url(self):
        sleep(1)
        return self.find_element(*self.menu_url_info).text

    def menu_info_classname(self):
        sleep(1)
        return self.find_element(*self.menu_classname_info).text

    def menu_info_sort(self):
        sleep(1)
        return self.find_element(*self.menu_sort_info).text

    #编辑菜单
    def menu_edit(self,part,menu,url,classname,module):
        sleep(1)
        self.find_element(*self.menu_edit_button_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[1]/div').click()
        sleep(1)
        parts = self.driver.find_element_by_name('parentid')
        parts.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[2]/div/div[%s]' % part).click()
        sleep(1)
        self.find_element(*self.menu_add_edit_name).clear()
        sleep(1)
        self.find_element(*self.menu_add_edit_name).send_keys(menu)
        sleep(1)
        self.find_element(*self.menu_add_edit_url).clear()
        sleep(1)
        self.find_element(*self.menu_add_edit_url).send_keys(url)
        sleep(1)
        self.find_element(*self.menu_add_edit_classname).clear()
        sleep(1)
        self.find_element(*self.menu_add_edit_classname).send_keys(classname)
        sleep(1)
        self.find_element(*self.menu_add_edit_save_button).click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    #删除菜单
    def menu_delete(self,menuid):
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='%s']" % menuid).click()
        sleep(1)
        comfirm = self.driver.switch_to_alert()
        sleep(1)
        comfirm.accept()
        complete = self.driver.switch_to_alert()
        sleep(1)
        complete.accept()

    #新增菜单
    def menu_add(self,part,menu,url,classname,sort,module):
        sleep(1)
        self.find_element(*self.menu_add_button_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[1]/div').click()
        sleep(1)
        parts = self.driver.find_element_by_name('parentid')
        parts.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[2]/div/div[%s]' % part).click()
        sleep(1)
        self.find_element(*self.menu_add_edit_name).clear()
        sleep(1)
        self.find_element(*self.menu_add_edit_name).send_keys(menu)
        sleep(1)
        self.find_element(*self.menu_add_edit_url).clear()
        sleep(1)
        self.find_element(*self.menu_add_edit_url).send_keys(url)
        sleep(1)
        self.find_element(*self.menu_add_edit_classname).clear()
        sleep(1)
        self.find_element(*self.menu_add_edit_classname).send_keys(classname)
        sleep(1)
        self.find_element(*self.menu_add_edit_sort).clear()
        sleep(1)
        self.find_element(*self.menu_add_edit_sort).send_keys(sort)
        sleep(1)
        self.find_element(*self.menu_add_edit_save_button).click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    def surf_menu(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get("http://bossdev.epoque.cn/admin/menu/index")
        self.open()

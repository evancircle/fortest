# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class resource(Page):

    url = "/admin/resource/index"

    resource_search_button_loc = (By.XPATH,'//*[@id="formsearch"]/div[1]')
    resource_add_button_loc = (By.XPATH,'//*[@id="formsearch"]/div[2]')
    resource_edit_button_loc = (By.LINK_TEXT,u"编辑")
    resource_id_info6 = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[6]/td[1]')
    resource_menuid_info6 = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[6]/td[2]')
    resource_name_info6 = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[6]/td[3]')
    resource_url_info6 = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[6]/td[4]')
    resource_attach_info6 = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[6]/td[5]')
    resource_id_info1 = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[1]')
    resource_menuid_info1 = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[2]')
    resource_name_info1 = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[3]')
    resource_url_info1 = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[4]')
    resource_attach_info1 = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[5]')
    resource_add_edit_name = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-7 input[name="name"]')
    resource_add_edit_url = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-7 input[name="url"]')
    resource_add_edit_attach = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.form-group div.col-sm-7 textarea')
    resource_add_edit_save_button = (By.CSS_SELECTOR,'html body div#layui-layer100001.layui-layer.layui-layer-page.layer-anim div.layui-layer-content div.f-popup-wrapper div.panel-body.collapse.in.detail-page form#formData.form-horizontal div.panel-footer.f-detail-footbtn div.row div.btn-toolbar button#save-btn.btn.f-default-btn')
    resource_search_loc = (By.XPATH,'//*[@id="wrap"]/div[1]/div[1]/div/form/div/div/div[1]/div/div[1]/div')
    resource_nextpage_loc = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div[2]/div[2]/div/ol/li[6]/a')
    resource_lastpage_loc = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div[2]/div[2]/div/ol/li[1]/a')

    def resource_info_id1(self):
        sleep(1)
        return self.find_element(*self.resource_id_info1).text

    def resource_info_name1(self):
        sleep(1)
        return self.find_element(*self.resource_name_info1).text

    def resource_info_url1(self):
        sleep(1)
        return self.find_element(*self.resource_url_info1).text

    def resource_info_menuid1(self):
        sleep(1)
        return self.find_element(*self.resource_menuid_info1).text

    def resource_info_attach1(self):
        sleep(1)
        return self.find_element(*self.resource_attach_info1).text

    def resource_info_id6(self):
        sleep(1)
        return self.find_element(*self.resource_id_info6).text

    def resource_info_name6(self):
        sleep(1)
        return self.find_element(*self.resource_name_info6).text

    def resource_info_url6(self):
        sleep(1)
        return self.find_element(*self.resource_url_info6).text

    def resource_info_menuid6(self):
        sleep(1)
        return self.find_element(*self.resource_menuid_info6).text

    def resource_info_attach6(self):
        sleep(1)
        return self.find_element(*self.resource_attach_info6).text

    #编辑菜单
    def resource_edit(self,resource,url,attach,module):
        sleep(1)
        self.find_element(*self.resource_edit_button_loc).click()
        sleep(1)
        self.find_element(*self.resource_add_edit_name).clear()
        sleep(1)
        self.find_element(*self.resource_add_edit_name).send_keys(resource)
        sleep(1)
        self.find_element(*self.resource_add_edit_url).clear()
        sleep(1)
        self.find_element(*self.resource_add_edit_url).send_keys(url)
        sleep(1)
        self.find_element(*self.resource_add_edit_attach).clear()
        sleep(1)
        self.find_element(*self.resource_add_edit_attach).send_keys(attach)
        sleep(1)
        self.find_element(*self.resource_add_edit_save_button).click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    #删除菜单
    def resource_delete(self,resourceid):
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='%s']" % resourceid).click()
        sleep(1)
        comfirm = self.driver.switch_to_alert()
        sleep(1)
        comfirm.accept()
        complete = self.driver.switch_to_alert()
        sleep(1)
        complete.accept()

    #新增菜单
    def resource_add(self,part,resource,url,attach,module):
        sleep(1)
        self.find_element(*self.resource_add_button_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[1]/div').click()
        sleep(1)
        parts = self.driver.find_element_by_name('menuid')
        parts.find_element_by_xpath('//*[@id="formData"]/div[1]/div/div/div[2]/div/div[%s]' % part).click()
        sleep(1)
        self.find_element(*self.resource_add_edit_name).clear()
        sleep(1)
        self.find_element(*self.resource_add_edit_name).send_keys(resource)
        sleep(1)
        self.find_element(*self.resource_add_edit_url).clear()
        sleep(1)
        self.find_element(*self.resource_add_edit_url).send_keys(url)
        sleep(1)
        self.find_element(*self.resource_add_edit_attach).clear()
        sleep(1)
        self.find_element(*self.resource_add_edit_attach).send_keys(attach)
        sleep(1)
        self.find_element(*self.resource_add_edit_save_button).click()
        sleep(1)
        alert = self.driver.switch_to_alert()
        alert.accept()

    def surf_resource(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get("http://bossdev.epoque.cn/admin/resource/index")
        self.open()

    #查询按钮
    def resource_search_button(self):
        sleep(1)
        self.find_element(*self.resource_search_button_loc).click()

    #资源搜索
    def resource_search(self,source):
        sleep(1)
        self.find_element(*self.resource_search_loc).click()
        sleep(1)
        resource = self.driver.find_element_by_name('menuid')
        sleep(1)
        resource.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[1]/div/form/div/div/div[1]/div/div[2]/div/div[%s]' % source).click()
        sleep(1)
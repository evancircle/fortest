# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class brand(Page):

    url = "/admin/brand/summary"

    brand_search_shop_name_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[2]/input')#门店名称
    brand_search_shop_code_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[1]/input')#门店代码
    brand_search_date_start_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[3]/input')#开始日期
    brand_search_date_end_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[4]/input')#结束日期
    brand_search_scanner_id_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[5]/input')#设备编号
    brand_region_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[6]/div/div[1]/div')#所在地区
    brand_province_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[7]/div/div[1]/div')#所在省份
    brand_city_loc= (By.XPATH, '//*[@id="epoque-search"]/div/div/div[8]/div/div[1]/div')#所在城市
    brand_search_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[9]/div[1]')#查询按钮
    brand_export_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[9]/div[2]')#导出按钮
    brand_nextpage_loc = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[8]/a')#下一页
    brand_lastpage_loc = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[1]/a')#上一页
    brand_scanner_id_info= (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[1]')#设备编号
    brand_region_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[2]')#地区
    brand_province_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]')#省份
    brand_city_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]')#城市
    brand_shop_date_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[7]')#日期
    brand_shop_name_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[5]')#门店名称
    brand_tab_detail = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/ul/li[2]/a')
    brand_tab_summary = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/ul/li[1]/a')

    #切换表格为明细
    def brand_switchtodetail(self):
        self.find_element(*self.brand_tab_detail).click()
    def brand_detail(self):
        return self.find_element(*self.brand_tab_detail).text

    #切换表格为汇总
    def brand_switchtosummary(self):
        self.find_element(*self.brand_tab_summary).click()
    def brand_summary(self):
        return self.find_element(*self.brand_tab_summary).text

    #设备编号搜索
    def brand_search_scanner_id(self, id):
        sleep(1)
        self.find_element(*self.brand_search_scanner_id_loc).clear()
        sleep(1)
        self.find_element(*self.brand_search_scanner_id_loc).send_keys(id)

    def brand_info_scanner_id(self):
        sleep(1)
        return self.find_element(*self.brand_scanner_id_info).text

    #门店名称搜索
    def brand_search_shop_name(self,name):
        sleep(1)
        self.find_element(*self.brand_search_shop_name_loc).clear()
        sleep(1)
        self.find_element(*self.brand_search_shop_name_loc).send_keys(name)
    def brand_info_shop_name(self):
        sleep(1)
        return self.find_element(*self.brand_shop_name_info).text

    #门店代码搜索
    def brand_search_shop_code(self,code):
        sleep(1)
        self.find_element(*self.brand_search_shop_code_loc).clear()
        sleep(1)
        self.find_element(*self.brand_search_shop_code_loc).send_keys(code)
    def brand_info_shop_code(self):
        sleep(1)
        return self.find_element(*self.brand_search_shop_name_loc).text

    #查询日期
    def brand_search_date(self,start_date,end_date):
        sleep(1)
        self.find_element(*self.brand_search_date_start_loc).clear()
        sleep(1)
        self.find_element(*self.brand_search_date_start_loc).send_keys(start_date)
        sleep(1)
        self.find_element(*self.brand_search_date_end_loc).clear()
        sleep(1)
        self.find_element(*self.brand_search_date_end_loc).send_keys(end_date)
    def brand_info_date(self):
        sleep(1)
        return self.find_element(*self.brand_shop_date_info).text

    #所在地区搜索
    def brand_search_region(self,region):
        sleep(1)
        self.find_element(*self.brand_region_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('regionid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[6]/div/div[2]/div/div[%s]' % region).click()
        sleep(1)
    def brand_info_region(self):
        sleep(1)
        return self.find_element(*self.brand_region_info).text

    #所在省份搜索
    def brand_search_province(self,region,province):
        sleep(1)
        self.find_element(*self.brand_region_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('regionid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[6]/div/div[2]/div/div[%s]' % region).click()
        sleep(1)
        self.find_element(*self.brand_province_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('provinceid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[7]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
    def brand_info_province(self):
        sleep(1)
        return self.find_element(*self.brand_province_info).text

    #所在城市搜索
    def brand_search_city(self,region,province,city):
        sleep(1)
        self.find_element(*self.brand_region_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('regionid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[6]/div/div[2]/div/div[%s]' % region).click()
        sleep(1)
        self.find_element(*self.brand_province_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('provinceid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[7]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        self.find_element(*self.brand_city_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('cityid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[8]/div/div[2]/div/div[%s]' % city).click()
        sleep(1)
    def brand_info_city(self):
        sleep(1)
        return self.find_element(*self.brand_city_info).text

    #查询按钮
    def brand_search_button(self):
        sleep(1)
        self.find_element(*self.brand_search_button_loc).click()

    #访问设备日报
    def surf_brand(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get('http://bossdev.epoque.cn/admin/brand/summary')
        self.open()

    #导出文件
    def brand_export(self):
        def brand_cleanDir(rootdir):
            if os.path.isdir(rootdir):
                paths = os.listdir(rootdir)
                for path in paths:
                    filePath = os.path.join(rootdir, path)
                    if os.path.isfile(filePath):
                        try:
                            os.remove(filePath)
                        except os.error:
                            autoRun.exception("remove %s error." % filePath)  # 引入logging
                    elif os.path.isdir(filePath):
                        if filePath[-4:].lower() == ".svn".lower():
                            continue
                        shutil.rmtree(filePath, True)
        rootdir=r'C:\Users\lenovo\Downloads'
        brand_cleanDir(rootdir)
        sleep(3)
        self.find_element(*self.brand_export_button_loc).click()
        sleep(3)
        if os.listdir(rootdir):
            return True

    #下一页
    def brand_nextpage(self):
        sleep(1)
        self.find_element(*self.brand_nextpage_loc).click()
    #上一页
    def brand_lastpage(self):
        sleep(1)
        self.find_element(*self.brand_lastpage_loc).click()

    #使页面失去焦点
    def brand_lostfocus(self):
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/div/ol').click()









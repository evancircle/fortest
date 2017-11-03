# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class report(Page):

    url = "/admin/scanner/daily"

    report_search_scanner_id_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[1]/input')#设备编号
    report_search_shop_name_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[2]/input')#门店名称
    report_search_shop_code_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[3]/input')#门店代码
    report_search_date_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[4]/input')#查询日期
    report_region_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[5]/div/div[1]/div')#所在地区
    report_province_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[6]/div/div[1]/div')#所在省份
    report_city_loc= (By.XPATH, '//*[@id="epoque-search"]/div/div/div[7]/div/div[1]/div')#所在城市
    report_search_shop_type_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[8]/div/div[1]/input')#门店类型
    report_search_brand_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[9]/div/div[1]/input')#品牌
    report_search_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[10]/div[1]')#查询按钮
    report_export_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[10]/div[2]')#导出按钮
    report_nextpage_loc = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[8]/a')#下一页
    report_lastpage_loc = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[1]/a')#上一页
    report_scanner_id_info= (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[1]')#设备编号
    report_region_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[2]')#地区
    report_province_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]')#省份
    report_city_info = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]")#城市
    report_shop_name_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[5]')#门店名称
    report_shop_code_info = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[6]")#门店代码
    report_shop_type_info = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[7]")#门店类型
    report_date_info = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[14]")#当日启动时间

    #设备编号搜索
    def report_search_scanner_id(self,id):
        sleep(1)
        self.find_element(*self.report_search_scanner_id_loc).clear()
        sleep(1)
        self.find_element(*self.report_search_scanner_id_loc).send_keys(id)
    def report_info_scanner_id(self):
        sleep(1)
        return self.find_element(*self.report_scanner_id_info).text

    #门店名称搜索
    def report_search_shop_name(self,name):
        sleep(1)
        self.find_element(*self.report_search_shop_name_loc).clear()
        sleep(1)
        self.find_element(*self.report_search_shop_name_loc).send_keys(name)
    def report_info_shop_name(self):
        sleep(1)
        return self.find_element(*self.report_shop_name_info).text

    #门店代码搜索
    def report_search_shop_code(self,code):
        sleep(1)
        self.find_element(*self.report_search_shop_code_loc).clear()
        sleep(1)
        self.find_element(*self.report_search_shop_code_loc).send_keys(code)
    def report_info_shop_code(self):
        sleep(1)
        return self.find_element(*self.report_shop_code_info).text

    #查询日期
    def report_search_date(self,date):
        sleep(1)
        self.find_element(*self.report_search_date_loc).clear()
        sleep(1)
        self.find_element(*self.report_search_date_loc).send_keys(date)
    def report_info_date(self):
        sleep(1)
        return self.find_element(*self.report_date_info).text

    #所在地区搜索
    def report_search_region(self,region):
        sleep(1)
        self.find_element(*self.report_region_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('regionid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[5]/div/div[2]/div/div[%s]' % region).click()
        sleep(1)
    def report_info_region(self):
        sleep(1)
        return self.find_element(*self.report_region_info).text

    #所在省份搜索
    def report_search_province(self,region,province):
        sleep(1)
        self.find_element(*self.report_region_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('regionid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[5]/div/div[2]/div/div[%s]' % region).click()
        sleep(1)
        self.find_element(*self.report_province_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('provinceid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[6]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
    def report_info_province(self):
        sleep(1)
        return self.find_element(*self.report_province_info).text

    #所在城市搜索
    def report_search_city(self,region,province,city):
        sleep(1)
        self.find_element(*self.report_region_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('regionid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[5]/div/div[2]/div/div[%s]' % region).click()
        sleep(1)
        self.find_element(*self.report_province_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('provinceid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[6]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        self.find_element(*self.report_city_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('cityid')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[7]/div/div[2]/div/div[%s]' % city).click()
        sleep(1)
    def report_info_city(self):
        sleep(1)
        return self.find_element(*self.report_city_info).text

    #门店类型搜索
    def report_search_shop_type(self,type):
        sleep(1)
        self.find_element(*self.report_search_shop_type_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('shop_type')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[8]/div/div[2]/div/div[%s]' % type).click()
        sleep(1)
    def report_info_shop_type(self):
        sleep(1)
        return self.find_element(*self.report_shop_type_info).text

    #品牌搜索
    def report_search_brand(self,brand):
        sleep(1)
        self.find_element(*self.report_search_brand_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('brand')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[9]/div/div[2]/div/div[%s]' % brand).click()
        sleep(1)
    def report_info_brand(self):
        sleep(1)
        return self.find_element(*self.report_shop_name_info).text
    #assertIn

    #查询按钮
    def report_search_button(self):
        sleep(1)
        self.find_element(*self.report_search_button_loc).click()

    #访问设备日报
    def surf_report(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get('http://bossdev.epoque.cn/admin/scanner/daily')
        self.open()

    #导出文件
    def report_export(self):
        def report_cleanDir(rootdir):
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
        report_cleanDir(rootdir)
        sleep(3)
        self.find_element(*self.report_export_button_loc).click()
        sleep(3)
        if os.listdir(rootdir):
            return True

    #下一页
    def report_nextpage(self):
        sleep(1)
        self.find_element(*self.report_nextpage_loc).click()
    #上一页
    def report_lastpage(self):
        sleep(1)
        self.find_element(*self.report_lastpage_loc).click()

    #使页面失去焦点
    def report_lostfocus(self):
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/div/ol').click()









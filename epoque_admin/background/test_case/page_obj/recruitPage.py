# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class recruit(Page):

    url = "/admin/recruit/summary"

    recruit_search_date_start_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[1]/div[2]/input')#开始日期
    recruit_search_date_end_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[1]/div[3]/input')#结束日期
    recruit_region_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[1]/div')#所在地区
    recruit_province_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[2]/div[2]/div/div[1]/div')#所在省份
    recruit_city_loc= (By.XPATH, '//*[@id="epoque-search"]/div/div[2]/div[3]/div/div[1]/div')#所在城市
    recruit_brand_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[1]/div[1]/div/div[1]/input')#品牌
    recruit_search_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[2]/div[4]/div[1]')#查询按钮
    recruit_export_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[2]/div[4]/div[2]')#导出按钮
    recruit_nextpage_loc = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[8]/a')#下一页
    recruit_lastpage_loc = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[1]/a')#上一页
    recruit_region_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[1]')#地区
    recruit_province_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[2]')#省份
    recruit_city_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]')#城市
    recruit_shop_date_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[6]')#统计日期
    recruit_brand_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]')#品牌
    recruit_tab_detail = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/ul/li[2]/a')
    recruit_tab_summary = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/ul/li[1]/a')

    #切换表格为明细
    def recruit_switchtodetail(self):
        self.find_element(*self.recruit_tab_detail).click()
    def recruit_detail(self):
        return self.find_element(*self.recruit_tab_detail).text

    #切换表格为汇总
    def recruit_switchtosummary(self):
        self.find_element(*self.recruit_tab_summary).click()
    def recruit_summary(self):
        return self.find_element(*self.recruit_tab_summary).text

    #查询日期
    def recruit_search_date(self,start_date,end_date):
        sleep(1)
        self.find_element(*self.recruit_search_date_start_loc).clear()
        sleep(1)
        self.find_element(*self.recruit_search_date_start_loc).send_keys(start_date)
        sleep(1)
        self.find_element(*self.recruit_search_date_end_loc).clear()
        sleep(1)
        self.find_element(*self.recruit_search_date_end_loc).send_keys(end_date)
    def recruit_info_date(self):
        sleep(1)
        return self.find_element(*self.recruit_shop_date_info).text

    #品牌搜索
    def recruit_search_brand(self,brand):
        sleep(1)
        self.find_element(*self.recruit_brand_loc).click()
        sleep(1)
        recruits = self.driver.find_element_by_name('brand')
        sleep(1)
        recruits.find_element_by_xpath('//*[@id="epoque-search"]/div/div[1]/div[1]/div/div[2]/div/div[%s]' % brand).click()
        sleep(1)
    def recruit_info_brand(self):
        sleep(1)
        return self.find_element(*self.recruit_brand_info).text

    #所在地区搜索
    def recruit_search_region(self,region):
        sleep(1)
        self.find_element(*self.recruit_region_loc).click()
        sleep(1)
        recruits = self.driver.find_element_by_name('regionid')
        sleep(1)
        recruits.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[2]/div/div[%s]' % region).click()
        sleep(1)
    def recruit_info_region(self):
        sleep(1)
        return self.find_element(*self.recruit_region_info).text

    #所在省份搜索
    def recruit_search_province(self,region,province):
        sleep(1)
        self.find_element(*self.recruit_region_loc).click()
        sleep(1)
        recruits = self.driver.find_element_by_name('regionid')
        sleep(1)
        recruits.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[2]/div/div[%s]' % region).click()
        sleep(1)
        self.find_element(*self.recruit_province_loc).click()
        sleep(1)
        recruits = self.driver.find_element_by_name('provinceid')
        sleep(1)
        recruits.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[2]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
    def recruit_info_province(self):
        sleep(1)
        return self.find_element(*self.recruit_province_info).text

    #所在城市搜索
    def recruit_search_city(self,region,province,city):
        sleep(1)
        self.find_element(*self.recruit_region_loc).click()
        sleep(1)
        recruits = self.driver.find_element_by_name('regionid')
        sleep(1)
        recruits.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[2]/div/div[%s]' % region).click()
        sleep(1)
        self.find_element(*self.recruit_province_loc).click()
        sleep(1)
        recruits = self.driver.find_element_by_name('provinceid')
        sleep(1)
        recruits.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[2]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        self.find_element(*self.recruit_city_loc).click()
        sleep(1)
        recruits = self.driver.find_element_by_name('cityid')
        sleep(1)
        recruits.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[3]/div/div[2]/div/div[%s]' % city).click()
        sleep(1)
    def recruit_info_city(self):
        sleep(1)
        return self.find_element(*self.recruit_city_info).text

    #查询按钮
    def recruit_search_button(self):
        sleep(1)
        self.find_element(*self.recruit_search_button_loc).click()

    #访问设备日报
    def surf_recruit(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get('http://bossdev.epoque.cn/admin/recruit/summary')
        self.open()

    #导出文件
    def recruit_export(self):
        def recruit_cleanDir(rootdir):
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
        recruit_cleanDir(rootdir)
        sleep(3)
        self.find_element(*self.recruit_export_button_loc).click()
        sleep(3)
        if os.listdir(rootdir):
            return True

    #下一页
    def recruit_nextpage(self):
        sleep(1)
        self.find_element(*self.recruit_nextpage_loc).click()
    #上一页
    def recruit_lastpage(self):
        sleep(1)
        self.find_element(*self.recruit_lastpage_loc).click()

    #使页面失去焦点
    def recruit_lostfocus(self):
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/div/ol').click()









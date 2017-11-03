# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class ctarget(Page):

    url = "/admin/scan-target/analy-country"

    ctarget_search_id_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[1]/div[1]/input')#设备编号
    ctarget_search_code_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[1]/div[2]/input')#门店代码
    ctarget_search_shop_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[1]/div[3]/input')#门店代码
    ctarget_search_area_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[1]/div')#所在地区
    ctarget_search_province_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[2]/div[2]/div/div[1]/div')#所在省份
    ctarget_search_city_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[2]/div[3]/div/div[1]/div')#所在城市
    ctarget_search_date_start_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[3]/div[1]/input')#开始日期
    ctarget_search_date_end_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[3]/div[2]/input')#结束日期
    ctarget_export_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[3]/div[3]/div[2]')#导出
    ctarget_search_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div[3]/div[3]/div[1]')#查询按钮
    ctarget_summary_goal_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[5]')#汇总-目标值
    ctarget_summary_region_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]')#汇总-地区
    ctarget_detail_region_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[1]')#明细-地区
    ctarget_detail_province_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[2]')
    ctarget_detail_city_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]')
    ctarget_detail_shop_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]')
    ctarget_detail_id_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[5]')
    ctarget_detail_date_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[6]')
    ctarget_detail_goal_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[8]')
    ctarget_lastpage_loc = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[1]/a')#上一页
    ctarget_nextpage_loc = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[8]/a')#下一页
    ctarget_switch_detail = (By.XPATH,'//*[@id="myTabs"]/li[2]/a')
    ctarget_switch_summary = (By.XPATH,'//*[@id="myTabs"]/li[1]/a')

    # 明细-首行id
    def ctarget_detail_info_id(self):
        sleep(1)
        return self.find_element(*self.ctarget_detail_id_info).text

    # 明细-首行时间
    def ctarget_detail_info_date(self):
        sleep(1)
        return self.find_element(*self.ctarget_detail_date_info).text

    # 明细-首行目标
    def ctarget_detail_info_goal(self):
        sleep(1)
        return self.find_element(*self.ctarget_detail_goal_info).text

    # 明细-首行地区
    def ctarget_detail_info_region(self):
        sleep(1)
        return self.find_element(*self.ctarget_detail_region_info).text

    # 明细-首行省份
    def ctarget_detail_info_province(self):
        sleep(1)
        return self.find_element(*self.ctarget_detail_province_info).text

    # 明细-首行城市
    def ctarget_detail_info_city(self):
        sleep(1)
        return self.find_element(*self.ctarget_detail_city_info).text

    # 明细-首行门店
    def ctarget_detail_info_shop(self):
        sleep(1)
        return self.find_element(*self.ctarget_detail_shop_info).text

    # 汇总-首行地区
    def ctarget_summary_info_region(self):
        sleep(1)
        return self.find_element(*self.ctarget_summary_region_info).text

    # 汇总-首行目标
    def ctarget_summary_info_goal(self):
        sleep(1)
        return self.find_element(*self.ctarget_summary_goal_info).text

    # 查询按钮
    def ctarget_search_button(self):
        sleep(1)
        self.find_element(*self.ctarget_search_button_loc).click()
        sleep(10)

    #访问目标查询
    def surf_ctarget(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get('http://bossdev.epoque.cn/admin/scan-target/analy-country')
        self.open()

    #上一页
    def ctarget_lastpage(self):
        sleep(1)
        self.find_element(*self.ctarget_lastpage_loc).click()

    #下一页
    def ctarget_nextpage(self):
        sleep(1)
        self.find_element(*self.ctarget_nextpage_loc).click()

    #导出
    def ctarget_export(self):
        def ctarget_cleanDir(rootdir):
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
        ctarget_cleanDir(rootdir)
        sleep(3)
        self.find_element(*self.ctarget_export_button_loc).click()
        sleep(3)
        if os.listdir(rootdir):
            return True

    def target_switch_detail(self):
        sleep(1)
        self.find_element(*self.ctarget_switch_detail).click()

    def target_switch_summary(self):
        sleep(1)
        self.find_element(*self.ctarget_switch_summary).click()

    def ctarget_search_area(self,area):
        sleep(1)
        self.find_element(*self.ctarget_search_area_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[2]/div/div[%s]' % area).click()

    def ctarget_search_province(self,area,province):
        sleep(1)
        self.find_element(*self.ctarget_search_area_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.ctarget_search_province_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[2]/div/div[2]/div/div[%s]' % province).click()

    def ctarget_search_city(self,area,province,city):
        sleep(1)
        self.find_element(*self.ctarget_search_area_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.ctarget_search_province_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[2]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        self.find_element(*self.ctarget_search_city_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[3]/div/div[2]/div/div[%s]' % city).click()

    def ctarget_search_shop(self,shop):
        sleep(1)
        self.find_element(*self.ctarget_search_shop_loc).send_keys(shop)

    def ctarget_search_id(self,id):
        sleep(1)
        self.find_element(*self.ctarget_search_id_loc).send_keys(id)

    def ctarget_search_code(self,code):
        sleep(1)
        self.find_element(*self.ctarget_search_code_loc).send_keys(code)

    #时间搜索
    def ctarget_search_date(self, start_date, end_date):
        sleep(1)
        self.find_element(*self.ctarget_search_date_start_loc).clear()
        sleep(1)
        self.find_element(*self.ctarget_search_date_start_loc).send_keys(start_date)
        sleep(1)
        self.find_element(*self.ctarget_search_date_end_loc).clear()
        sleep(1)
        self.find_element(*self.ctarget_search_date_end_loc).send_keys(end_date)










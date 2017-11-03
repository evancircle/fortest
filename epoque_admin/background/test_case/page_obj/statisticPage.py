# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page
import shutil

class statistic(Page):

    url = "/admin/wx"

    statistic_search_contrastdate_start_loc = (By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/div/form/div/div/div[1]/input')#对比开始日期
    statistic_search_contrastdate_end_loc = (By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/div/form/div/div/div[2]/input')#对比结束日期
    statistic_search_checkdate_start_loc = (By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/div/form/div/div/div[3]/input')#查询开始时间
    statistic_search_checkdate_end_loc = (By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/div/form/div/div/div[4]/input')#查询结束时间
    statistic_type_loc = (By.XPATH,'//*[@id="wxFrom"]/div/div/div[5]/div/div[1]/input')#渠道类型
    statistic_search_button_loc = (By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/div/form/div/div/div[7]/div[1]')#查询按钮
    statistic_export_button_loc = (By.XPATH, '//*[@id="wrap"]/div[1]/div[1]/div/form/div/div/div[7]/div[2]')#导出按钮
    statistic_contrastdate_info = (By.XPATH, '//*[@id="wrap"]/div[1]/div[2]/div/div[2]/div/div/table/thead/tr/th[2]')#对比日期
    statistic_check_info = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[3]')#查询日期总计
    statistic_contrast_info = (By.XPATH,'//*[@id="wrap"]/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[4]')#对比日期总计

    #对比日期
    def statistic_search_contrastdate(self,start_date,end_date):
        sleep(1)
        self.find_element(*self.statistic_search_contrastdate_start_loc).clear()
        sleep(1)
        self.find_element(*self.statistic_search_contrastdate_start_loc).send_keys(start_date)
        sleep(1)
        self.find_element(*self.statistic_search_contrastdate_end_loc).clear()
        sleep(1)
        self.find_element(*self.statistic_search_contrastdate_end_loc).send_keys(end_date)


    #查询日期
    def statistic_search_checkdate(self,start_date,end_date):
        sleep(1)
        self.find_element(*self.statistic_search_checkdate_start_loc).clear()
        sleep(1)
        self.find_element(*self.statistic_search_checkdate_start_loc).send_keys(start_date)
        sleep(1)
        self.find_element(*self.statistic_search_checkdate_end_loc).clear()
        sleep(1)
        self.find_element(*self.statistic_search_checkdate_end_loc).send_keys(end_date)

    #对比日期
    def statistic_info_contrastdate(self):
        sleep(1)
        return self.find_element(*self.statistic_contrastdate_info).text

    #首行对比日期总计
    def statistic_info_contrast(self):
        sleep(1)
        return self.find_element(*self.statistic_contrast_info).text

    #首行查询日期总计
    def statistic_info_check(self):
        sleep(1)
        return self.find_element(*self.statistic_check_info).text

    #渠道类型
    def statistic_search_type(self,type):
        sleep(1)
        self.find_element(*self.statistic_type_loc).click()
        sleep(1)
        statistics = self.driver.find_element_by_name('search_user_source')
        sleep(1)
        statistics.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[1]/div/form/div/div/div[5]/div/div[2]/div/div[%s]' % type).click()
        sleep(1)

    #查询按钮
    def statistic_search_button(self):
        sleep(1)
        self.find_element(*self.statistic_search_button_loc).click()

    #访问公众号统计查询
    def surf_statistic(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get("http://bossdev.epoque.cn/admin/wx")
        self.open()

    #使页面失去焦点
    def statistic_lostfocus(self):
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[1]/div/ol').click()

    #导出文件
    def statistic_export(self):
        def statistic_cleanDir(rootdir):
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
        statistic_cleanDir(rootdir)
        sleep(3)
        self.find_element(*self.statistic_export_button_loc).click()
        sleep(3)
        if os.listdir(rootdir):
            return True










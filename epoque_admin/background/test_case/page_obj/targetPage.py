# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class target(Page):

    url = "/admin/scan-target"

    target_search_area_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[1]/div/div[1]/div')#所在地区
    target_search_province_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[2]/div/div[1]/div')#所在省份
    target_search_city_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[3]/div/div[1]/div')#所在城市
    target_shop_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[4]/input')#所在门店
    target_date_from_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[5]/input')#开始日期
    target_date_to_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[6]/input')#结束日期
    target_search_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[8]/div[1]')#查询按钮
    target_add_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[8]/div[2]')#新增目标
    target_date_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[2]')#日期
    target_goal_range_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]')#目标范围
    target_goal_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[5]')#目标合计
    target_shop_sum_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]')#门店数量
    target_region_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]')#地区
    target_province_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[5]')#省份
    target_city_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[6]')#城市
    target_shop_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[7]')#门店
    terget_id_info = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr/td[1]')#id
    target_goal_detail_info = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr/td[10]')#目标合计-明细
    target_switch_detail_loc = (By.XPATH, '//*[@id="myTabs"]/li[2]/a')
    target_switch_summary_loc = (By.XPATH, '//*[@id="myTabs"]/li[1]/a')

    #首行id
    def target_info_id(self):
        sleep(1)
        return self.find_element(*self.terget_id_info).text

    #首行时间
    def target_info_date(self):
        sleep(1)
        return self.find_element(*self.target_date_info).text

    #首行目标
    def target_info_goal(self):
        sleep(1)
        return self.find_element(*self.target_goal_info).text

    #首行目标范围
    def target_info_goal_range(self):
        sleep(1)
        return self.find_element(*self.target_goal_range_info).text

    #首行门店数量
    def target_info_rate(self):
        sleep(1)
        return self.find_element(*self.target_shop_sum_info).text

    #首行地区
    def target_info_region(self):
        sleep(1)
        return self.find_element(*self.target_region_info).text

    #首行省份
    def target_info_province(self):
        sleep(1)
        return self.find_element(*self.target_province_info).text

    #首行城市
    def target_info_city(self):
        sleep(1)
        return self.find_element(*self.target_city_info).text

    #首行门店
    def target_info_shop(self):
        sleep(1)
        return self.find_element(*self.target_shop_info).text

    #查询按钮
    def target_search_button(self):
        sleep(1)
        self.find_element(*self.target_search_button_loc).click()
        sleep(10)

    #新增目标
    def target_add(self,goal_range,start_date,end_date,weekday,weekend,text,select):
        sleep(1)
        self.find_element(*self.target_add_button_loc).click()
        sleep(1)
        if goal_range == 'country':
            self.driver.find_element_by_xpath('//*[@id="country_start_time"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_start_time"]').send_keys(start_date)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_end_time"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_end_time"]').send_keys(end_date)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/div/ol').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_select_name"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_all"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_submit"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_set_weekday"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_set_weekday"]').send_keys(weekday)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_set_weekend"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_set_weekend"]').send_keys(weekend)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_set_btn"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_remark"]').send_keys(text)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="save-btn"]').click()
        elif goal_range == 'region':
            self.driver.find_element_by_xpath('//*[@id="country_start_time"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_start_time"]').send_keys(start_date)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_end_time"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_end_time"]').send_keys(end_date)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/div/ol').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_select_name"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_select_wrapper"]/li[%s]/label/input'%select).click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_submit"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_set_weekday"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_set_weekday"]').send_keys(weekday)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_set_weekend"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_set_weekend"]').send_keys(weekend)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_set_btn"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_remark"]').send_keys(text)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="save-btn"]').click()
        elif goal_range == 'city':
            self.driver.find_element_by_xpath('//*[@id="myTabs"]/li[2]/a').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_start_time"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_start_time"]').send_keys(start_date)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_end_time"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_end_time"]').send_keys(end_date)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/div/ol').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="city_select_name"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="city_select_wrapper"]/li[%s]/label/input'%select).click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="city_submit"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_set_weekday"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_set_weekday"]').send_keys(weekday)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_set_weekend"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_set_weekend"]').send_keys(weekend)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_set_btn"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_remark"]').send_keys(text)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="save-btn"]').click()
        elif goal_range == 'shop':
            self.driver.find_element_by_xpath('//*[@id="myTabs"]/li[2]/a').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_start_time"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_start_time"]').send_keys(start_date)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_end_time"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_end_time"]').send_keys(end_date)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/div/ol').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="city_select_name"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="city_select_wrapper"]/li[%s]/label/input'%select).click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="city_submit"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="shop_select_name"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="shop_select_wrapper"]/li[%s]/label/input'%select).click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="shop_submit"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_set_weekday"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_set_weekday"]').send_keys(weekday)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_set_weekend"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_set_weekend"]').send_keys(weekend)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_set_btn"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_remark"]').send_keys(text)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="save-btn"]').click()

    #删除目标
    def target_delete(self,targer_id):
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="%s"]'%targer_id).click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button').click()

    #编辑目标
    def target_edit(self,weekday,weekend,text):
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr/td[8]/a').click()
        sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="myTabs"]/li[1]/a').text == u"全国" and self.driver.find_element_by_xpath('//*[@id="myTabs"]/li[2]/a').get_attribute('style') == 'display: none;':
            self.driver.find_element_by_xpath('//*[@id="country_set_weekday"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_set_weekday"]').send_keys(weekday)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_set_weekend"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_set_weekend"]').send_keys(weekend)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_set_btn"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="country_remark"]').clear()
            self.driver.find_element_by_xpath('//*[@id="country_remark"]').send_keys(text)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="save-btn"]').click()
        elif self.driver.find_element_by_xpath('//*[@id="myTabs"]/li[2]/a').text == u"地区" and self.driver.find_element_by_xpath('//*[@id="myTabs"]/li[1]/a').get_attribute('style') == 'display: none;':
            self.driver.find_element_by_xpath('//*[@id="region_set_weekday"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_set_weekday"]').send_keys(weekday)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_set_weekend"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_set_weekend"]').send_keys(weekend)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_set_btn"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="region_remark"]').clear()
            self.driver.find_element_by_xpath('//*[@id="region_remark"]').send_keys(text)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="save-btn"]').click()


    #按日期搜索
    def target_search_date(self, start_date, end_date):
        sleep(1)
        self.find_element(*self.target_date_from_loc).clear()
        sleep(1)
        self.find_element(*self.target_date_from_loc).send_keys(start_date)
        sleep(1)
        self.find_element(*self.target_date_to_loc).clear()
        sleep(1)
        self.find_element(*self.target_date_to_loc).send_keys(end_date)

    #按地区搜索
    def target_search_area(self,area):
        sleep(1)
        self.find_element(*self.target_search_area_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[1]/div/div[2]/div/div[%s]'%area).click()

    #按省份搜索
    def target_search_province(self,area,province):
        sleep(1)
        self.find_element(*self.target_search_area_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.target_search_province_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[2]/div/div[2]/div/div[%s]' % province).click()

    #按城市搜索
    def target_search_city(self,area,province,city):
        sleep(1)
        self.find_element(*self.target_search_area_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.target_search_province_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[2]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        self.find_element(*self.target_search_city_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[3]/div/div[2]/div/div[%s]' % city).click()

    #按门店搜索
    def target_search_shop(self,shop):
        sleep(1)
        self.find_element(*self.target_shop_loc).send_keys(shop)

    #按目标范围搜索
    def target_search_goal_range(self,range):
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[7]/div/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[7]/div/div[2]/div/div[%s]'%range).click()

    #访问统计分析
    def surf_target(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get('http://bossdev.epoque.cn/admin/scan-target')
        self.open()
        sleep(10)

    #使页面失去焦点
    def target_lostfocus(self):
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/div/ol').click()

    def target_switch_detail(self):
        sleep(1)
        self.find_element(*self.target_switch_detail_loc).click()

    def target_switch_summary(self):
        sleep(1)
        self.find_element(*self.target_switch_summary_loc).click()











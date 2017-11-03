# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class fault(Page):

    url = "/admin/fault"

    fault_search_id_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[1]/input')#设备编号
    fault_search_shop_name_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[2]/input')#门店名称
    fault_search_shop_code_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[3]/input')#门店代码
    fault_search_startdate_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[5]/input')#开始时间
    fault_search_enddate_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[6]/input')#结束时间
    fault_export_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[7]/div[3]')#导出按钮
    fault_add_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[7]/div[2]')#新增记录
    fault_search_button_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[7]/div[1]')#查询按钮
    fault_edit_button_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[13]/div/a[1]')#查看/编辑按钮
    fault_edit_add_starttime_loc = (By.XPATH,'//*[@id="formDetail"]/div[4]/div/input')#统计开始日期
    fault_edit_add_endtime_loc = (By.XPATH,'//*[@id="formDetail"]/div[5]/div/input')#统计结束日期
    fault_edit_add_record_loc = (By.XPATH, '//*[@id="formDetail"]/div[6]/div/textarea')#故障说明
    fault_add_edit_save_button_loc = (By.XPATH,'//*[@id="save-btn"]')
    fault_info_faultid = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[1]')#首行故障编号
    fault_info_id = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[5]')#首行设备ID
    fault_info_code = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[6]')#首行门店代码
    fault_info_name = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[7]')#首行门店名称
    fault_info_startdate = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[8]')#首行开始日期
    fault_info_enddate = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[9]')#首行结束日期
    fault_info_fault = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[11]')#首行故障说明
    fault_search_area_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[4]/div[1]/div/div[1]/div')#所在地区
    fault_search_province_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[4]/div[2]/div/div[1]/div')#所在省份
    fault_search_city_loc = (By.XPATH, '//*[@id="epoque-search"]/div/div/div[4]/div[3]/div/div[1]/div')#所在城市
    fault_info_area = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[2]')#首行地区信息
    fault_info_province = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]')#首行省份信息
    fault_info_city = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]')#首行城市信息

    #设备编号搜索
    def fault_search_id(self,id):
        sleep(1)
        self.find_element(*self.fault_search_id_loc).clear()
        sleep(1)
        self.find_element(*self.fault_search_id_loc).send_keys(id)
    def search_id_success_mgt(self):
        sleep(1)
        return self.find_element(*self.fault_info_id).text

    #门店名称搜索
    def fault_search_shop_name(self,name):
        sleep(1)
        self.find_element(*self.fault_search_shop_name_loc).clear()
        sleep(1)
        self.find_element(*self.fault_search_shop_name_loc).send_keys(name)
    def search_shop_name_success_mgt(self):
        sleep(1)
        return self.find_element(*self.fault_info_name).text

    #门店代码搜索
    def fault_search_shop_code(self,code):
        sleep(1)
        self.find_element(*self.fault_search_shop_code_loc).clear()
        sleep(1)
        self.find_element(*self.fault_search_shop_code_loc).send_keys(code)
    def search_shop_code_success_mgt(self):
        sleep(1)
        return self.find_element(*self.fault_info_code).text

    #开始日期搜索
    def fault_search_startdate(self,sdate):
        sleep(1)
        self.find_element(*self.fault_search_startdate_loc).clear()
        sleep(1)
        self.find_element(*self.fault_search_startdate_loc).send_keys(sdate)
    def search_startdate_success_mgt(self):
        sleep(1)
        return self.find_element(*self.fault_info_startdate).text

    #结束日期搜索
    def fault_search_enddate(self,edate):
        sleep(1)
        self.find_element(*self.fault_search_enddate_loc).clear()
        sleep(1)
        self.find_element(*self.fault_search_enddate_loc).send_keys(edate)
    def search_enddate_success_mgt(self):
        sleep(1)
        return self.find_element(*self.fault_info_enddate).text

    #查询按钮
    def fault_search_button(self):
        sleep(1)
        self.find_element(*self.fault_search_button_loc).click()

    #访问扫描仪档案
    def surf_fault(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get("http://bossdev.epoque.cn/admin/fault")
        self.open()

    #首行设备编号信息
    def fault_id_info(self):
        sleep(1)
        return self.find_element(*self.fault_info_id).text

    #首行门店名称信息
    def fault_shop_name_info(self):
        sleep(1)
        return self.find_element(*self.fault_info_name).text

    #首行门店代码信息
    def fault_code_info(self):
        sleep(1)
        return self.find_element(*self.fault_info_code).text

    #首行开始时间信息
    def fault_startdate_info(self):
        sleep(1)
        return self.find_element(*self.fault_info_startdate).text

    #首行结束时间信息
    def fault_enddate_info(self):
        sleep(1)
        return self.find_element(*self.fault_info_enddate).text

    #首行故障说明信息
    def fault_fault_info(self):
        sleep(1)
        return self.find_element(*self.fault_info_fault).text

    #首行故障编号信息
    def fault_faultid_info(self):
        sleep(1)
        return self.find_element(*self.fault_info_faultid).text

    #新增扫描仪
    def fault_add(self,id,code,name,startdate,enddate,record):
        sleep(1)
        self.find_element(*self.fault_add_button_loc).click()#点击新增按钮
        sleep(1)
        js1 = 'document.getElementsByName("scanner_id")[0].removeAttribute("readonly");'
        self.driver.execute_script(js1)  # 使扫描仪编辑框可写
        self.driver.find_element_by_xpath('//*[@id="formDetail"]/div[1]/div/div/input').send_keys(id)
        # 门店代码选择
        js2 = 'document.getElementsByName("shop_code")[0].removeAttribute("readonly");'
        self.driver.execute_script(js2)  # 使门店代码编辑框可写
        self.driver.find_element_by_xpath('//*[@id="formDetail"]/div[2]/div/input').send_keys(code)
        # 门店名称选择
        js3 = 'document.getElementsByName("shop_name")[0].removeAttribute("readonly");'
        self.driver.execute_script(js3)  # 使门店名称编辑框可写
        self.driver.find_element_by_xpath('//*[@id="formDetail"]/div[3]/div/input').send_keys(name)
        sleep(1)
        self.find_element(*self.fault_edit_add_starttime_loc).send_keys(startdate)#输入开始时间
        sleep(1)
        self.find_element(*self.fault_edit_add_endtime_loc).send_keys(enddate)#输入结束时间
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[1]/div/ol').click()
        sleep(1)
        self.find_element(*self.fault_edit_add_record_loc).send_keys(record)#输入故障说明时间
        sleep(1)
        self.find_element(*self.fault_add_edit_save_button_loc).click()#点击保存
        sleep(2)
        self.driver.get("http://bossdev.epoque.cn/admin/fault")

    #查看/编辑扫描仪
    def fault_edit(self,id,code,name,startdate,enddate,record):
        sleep(1)
        self.find_element(*self.fault_edit_button_loc).click()#点击编辑按钮
        sleep(1)
        js1 = 'document.getElementsByName("scanner_id")[0].removeAttribute("readonly");'
        self.driver.execute_script(js1)  # 使扫描仪编辑框可写
        self.driver.find_element_by_xpath('//*[@id="formDetail"]/div[1]/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="formDetail"]/div[1]/div/div/input').send_keys(id)
        # 门店代码选择
        js2 = 'document.getElementsByName("shop_code")[0].removeAttribute("readonly");'
        self.driver.execute_script(js2)  # 使门店代码编辑框可写
        self.driver.find_element_by_xpath('//*[@id="formDetail"]/div[2]/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="formDetail"]/div[2]/div/input').send_keys(code)
        # 门店名称选择
        js3 = 'document.getElementsByName("shop_name")[0].removeAttribute("readonly");'
        self.driver.execute_script(js3)  # 使门店名称编辑框可写
        self.driver.find_element_by_xpath('//*[@id="formDetail"]/div[3]/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="formDetail"]/div[3]/div/input').send_keys(name)
        sleep(1)
        self.find_element(*self.fault_edit_add_starttime_loc).clear()
        self.find_element(*self.fault_edit_add_starttime_loc).send_keys(startdate)#修改开始时间
        self.find_element(*self.fault_edit_add_endtime_loc).clear()
        self.find_element(*self.fault_edit_add_endtime_loc).send_keys(enddate)#修改结束时间
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[1]/div/ol').click()
        sleep(1)
        self.find_element(*self.fault_edit_add_record_loc).clear()
        self.find_element(*self.fault_edit_add_record_loc).send_keys(record)#修改故障说明时间
        self.find_element(*self.fault_add_edit_save_button_loc).click() #点击保存
        sleep(2)
        self.driver.get("http://bossdev.epoque.cn/admin/fault")

    #删除扫描仪
    def fault_delete(self):
        sleep(1)
        self.driver.find_element_by_class_name('del').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button').click()

    #地区搜索
    def fault_search_area(self, area):
        sleep(1)
        self.find_element(*self.fault_search_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[4]/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
    def search_area_success_mgt(self):
        sleep(1)
        return self.find_element(*self.fault_info_area).text

    #省份搜索
    def fault_search_province(self, area, province):
        sleep(1)
        self.find_element(*self.fault_search_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[4]/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.fault_search_province_loc).click()
        sleep(1)
        provinces = self.driver.find_element_by_name('provinceid')
        sleep(1)
        provinces.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[4]/div[2]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
    def search_province_success_mgt(self):
        sleep(1)
        return self.find_element(*self.fault_info_province).text

    #城市搜索
    def fault_search_city(self, area, province, city):
        sleep(1)
        self.find_element(*self.fault_search_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[4]/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.fault_search_province_loc).click()
        sleep(1)
        provinces = self.driver.find_element_by_name('provinceid')
        sleep(1)
        provinces.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[4]/div[2]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        self.find_element(*self.fault_search_city_loc).click()
        sleep(1)
        citys = self.driver.find_element_by_name('cityid')
        sleep(1)
        citys.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[4]/div[3]/div/div[2]/div/div[%s]' % city).click()
        sleep(1)
    def search_city_success_mgt(self):
        sleep(1)
        return self.find_element(*self.fault_info_city).text

    #导出文件
    def fault_export(self):
        def fault_cleanDir(rootdir):
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
        fault_cleanDir(rootdir)
        sleep(3)
        self.find_element(*self.fault_export_button_loc).click()
        sleep(3)
        if os.listdir(rootdir):
            return True

    def fault_lostfocus(self):
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/div/ol').click()


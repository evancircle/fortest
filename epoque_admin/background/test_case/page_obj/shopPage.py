# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class shop(Page):

    url = "/admin/shop"

    shop_search_code_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[1]/input')#门店代码
    shop_search_name_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[2]/input')#门店名称
    shop_search_brand_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[3]/div/div/div[1]/input')#品牌
    shop_search_type_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[4]/div/div/div[1]/input')#门店类型
    shop_search_area_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[5]/div/div/div[1]/div')#所在地区
    shop_search_province_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[6]/div/div/div[1]/div')#所在省份
    shop_search_city_loc= (By.XPATH,'//*[@id="epoque-search"]/div/div/div[7]/div/div/div[1]/div')#所在城市
    shop_search_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[8]/div[1]')#查询按钮
    shop_add_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[8]/div[2]')#新建门店档案按钮
    shop_export_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[8]/div[3]')#导出按钮
    shop_edit_button_loc = (By.XPATH,'html/body/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[11]/div/a')#查看/编辑按钮
    shop_open_stop_button_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[11]/div/button')#启用/停用按钮
    shop_open_stop_comfirm_loc = (By.XPATH,"/html/body/div[3]/div/div/div[2]/button[2]")#启用/停用确定按钮
    shop_open_stop_ok_loc = (By.XPATH,"/html/body/div[3]/div/div/div[2]/button")#启用/停用ok按钮
    shop_lastpage_loc = (By.LINK_TEXT,u'上一頁')#上一页按钮
    shop_nextpage_loc = (By.LINK_TEXT,u'下一頁')#下一页按钮
    shop_add_edit_brand_loc = (By.XPATH,'//*[@id="shop"]/div[1]/div/div/div[1]/input')#新增/编辑品牌选项下拉按钮
    shop_add_edit_area_loc = (By.XPATH,'//*[@id="shop"]/div[2]/div/div/div[1]/div')#新增/编辑所在地区下拉按钮
    shop_add_edit_province_loc = (By.XPATH,'//*[@id="shop"]/div[3]/div/div/div[1]/div')#新增/编辑所在省份下拉按钮
    shop_add_edit_city_loc = (By.XPATH,'//*[@id="shop"]/div[4]/div/div/div[1]/div')#新增/编辑所在城市下拉按钮
    shop_add_edit_code_loc = (By.XPATH,'//*[@id="shop"]/div[5]/div/input')#新增/编辑门店代码
    shop_add_edit_name_loc = (By.XPATH,'//*[@id="shop"]/div[6]/div/input')#新增/编辑门店名称下来按钮
    shop_add_edit_type_loc = (By.XPATH,'//*[@id="shop"]/div[7]/div/div/div[1]/input')#新增/编辑门店类型下拉按钮
    shop_add_edit_address_loc = (By.XPATH,'//*[@id="shop"]/div[8]/div/input')#新增/编辑地址
    shop_add_edit_wechataddress_loc = (By.XPATH,'//*[@id="shop"]/div[9]/div/input')#新增/编辑微信展示地址
    shop_add_edit_mall_loc = (By.XPATH,'//*[@id="shop"]/div[10]/div/input')#新增/编辑所在商场
    shop_add_edit_status_loc = (By.XPATH,'//*[@id="shop"]/div[11]/div/div/div[1]/div')#新增/编辑状态下拉按钮
    shop_info_brand = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[1]')#首行门店品牌信息
    shop_info_area = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[2]')#首行门店所在地区信息
    shop_info_province = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[3]')#首行门店所在省份信息
    shop_info_city = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[4]')#首行门店所在城市信息
    shop_info_name = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[5]')#首行门店名称信息
    shop_info_code = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[6]')#首行门店代码信息
    shop_info_type = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[7]')#首行门店类型信息
    shop_info_address = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[8]')#首行门店地址信息
    shop_info_wechataddress = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[9]')#首行门店微信地址信息
    shop_info_status = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[10]')#首行门店状态信息
    shop_add_edit_save_button_loc = (By.XPATH, '//*[@id="save-btn"]')#新增编辑门店保存按钮
    shop_add_edit_ok_button_loc = (By.XPATH, '/html/body/div[3]/div/div/div[2]/button')#新增编辑门店ok按钮
    shop_delete_comfirm_loc = (By.XPATH,'/html/body/div[3]/div/div/div[2]/button[2]')#删除确认按钮
    shop_delete_ok_loc = (By.XPATH,'/html/body/div[3]/div/div/div[2]/button')#删除ok按钮

    #门店代码搜索
    def shop_search_code(self,code):
        sleep(1)
        self.find_element(*self.shop_search_code_loc).clear()
        sleep(1)
        self.find_element(*self.shop_search_code_loc).send_keys(code)
        sleep(1)
    def search_code_success(self):
        sleep(1)
        return self.find_element(*self.shop_info_code).text

    #门店名称搜索
    def shop_search_name(self,name):
        sleep(1)
        self.find_element(*self.shop_search_name_loc).clear()
        sleep(1)
        self.find_element(*self.shop_search_name_loc).send_keys(name)
        sleep(1)
    def search_name_success(self):
        sleep(1)
        return self.find_element(*self.shop_info_name).text

    #门店品牌搜索
    def shop_search_brand(self,brand):
        sleep(1)
        self.find_element(*self.shop_search_brand_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('brand')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[3]/div/div/div[2]/div/div[%s]' % brand).click()
        sleep(1)
    def search_brand_success(self):
        sleep(1)
        return self.find_element(*self.shop_info_brand).text

    #门店类型搜索
    def shop_search_type(self,type):
        sleep(1)
        self.find_element(*self.shop_search_type_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('shop_type')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[4]/div/div/div[2]/div/div[%s]' % type).click()
        sleep(1)
    def search_type_success(self):
        sleep(1)
        return self.find_element(*self.shop_info_type).text

    #门店地区搜索
    def shop_search_area(self,area):
        sleep(1)
        self.find_element(*self.shop_search_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[5]/div/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
    def search_area_success(self):
        sleep(1)
        return self.find_element(*self.shop_info_area).text

    #门店省份搜索
    def shop_search_province(self,area,province):
        sleep(1)
        self.find_element(*self.shop_search_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[5]/div/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.shop_search_province_loc).click()
        sleep(1)
        provinces = self.driver.find_element_by_name('provinceid')
        sleep(1)
        provinces.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[6]/div/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
    def search_province_success(self):
        sleep(1)
        return self.find_element(*self.shop_info_province).text

    #门店城市搜索
    def shop_search_city(self,area,province,city):
        sleep(1)
        self.find_element(*self.shop_search_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[5]/div/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.shop_search_province_loc).click()
        sleep(1)
        provinces = self.driver.find_element_by_name('provinceid')
        sleep(1)
        provinces.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[6]/div/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        self.find_element(*self.shop_search_city_loc).click()
        sleep(1)
        citys = self.driver.find_element_by_name('cityid')
        sleep(1)
        citys.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[7]/div/div/div[2]/div/div[%s]' % city).click()
        sleep(1)
    def search_city_success(self):
        sleep(1)
        return self.find_element(*self.shop_info_city).text

    #下一页
    def shop_nextpage(self):
        sleep(1)
        self.find_element(*self.shop_nextpage_loc).click()

    #上一页
    def shop_lastpage(self):
        sleep(1)
        self.find_element(*self.shop_lastpage_loc).click()

    #查询按钮
    def shop_search_button(self):
        sleep(1)
        self.find_element(*self.shop_search_button_loc).click()

    #启用/停用按钮
    def shop_open_stop_button(self):
        sleep(1)
        self.find_element(*self.shop_open_stop_button_loc).click()
        sleep(1)
        self.find_element(*self.shop_open_stop_comfirm_loc).click()
        sleep(1)
        self.find_element(*self.shop_open_stop_ok_loc).click()

    # 访问门店档案
    def surf_shop(self, username='admin', password='0000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get('http://bossdev.epoque.cn/admin/shop')
        self.open()

    #首行门店品牌信息
    def shop_brand_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_brand).text

    #首行门店所在地区信息
    def shop_area_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_area).text

    #首行门店所在省份信息
    def shop_province_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_province).text

    #首行门店所在城市信息
    def shop_city_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_city).text

    #首行门店名称信息
    def shop_name_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_name).text

    #首行门店代码信息
    def shop_code_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_code).text

    #首行门店类型信息
    def shop_type_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_type).text

    #首行门店地址信息
    def shop_address_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_address).text

    #首行门店微信地址信息
    def shop_wechataddress_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_wechataddress).text

    #首行门店状态信息
    def shop_status_info(self):
        sleep(1)
        return self.find_element(*self.shop_info_status).text

    #新增门店
    def shop_add(self,brand,area,province,city,code,name,type,address,wechataddress,mall,status):
        sleep(1)
        self.find_element(*self.shop_add_button_loc).click()#点击新增按钮
        #品牌选择
        self.find_element(*self.shop_add_edit_brand_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('brand')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="shop"]/div[1]/div/div/div[2]/div/div[%s]' % brand).click()
        sleep(1)
        #地区选择
        self.find_element(*self.shop_add_edit_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="shop"]/div[2]/div/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        #省份选择
        self.find_element(*self.shop_add_edit_province_loc).click()
        sleep(1)
        provinces = self.driver.find_element_by_name('provinceid')
        sleep(1)
        provinces.find_element_by_xpath('//*[@id="shop"]/div[3]/div/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        #城市选择
        self.find_element(*self.shop_add_edit_city_loc).click()
        sleep(1)
        citys = self.driver.find_element_by_name('cityid')
        sleep(1)
        citys.find_element_by_xpath('//*[@id="shop"]/div[4]/div/div/div[2]/div/div[%s]' % city).click()
        sleep(1)
        #状态选择
        self.find_element(*self.shop_add_edit_status_loc).click()
        sleep(1)
        statuss = self.driver.find_element_by_name('status')
        sleep(1)
        statuss.find_element_by_xpath('//*[@id="shop"]/div[11]/div/div/div[2]/div/div[%s]' % status).click()
        sleep(1)
        #类型选择
        self.find_element(*self.shop_add_edit_type_loc).click()
        sleep(1)
        types = self.driver.find_element_by_name('shop_type')
        sleep(1)
        types.find_element_by_xpath('//*[@id="shop"]/div[7]/div/div/div[2]/div/div[%s]' % type).click()
        sleep(1)
        #-----------------------------------------------------------------------
        self.find_element(*self.shop_add_edit_code_loc).send_keys(code)#输入代码
        self.find_element(*self.shop_add_edit_name_loc).send_keys(name)#输入名称
        self.find_element(*self.shop_add_edit_address_loc).send_keys(address)#输入地址
        self.find_element(*self.shop_add_edit_wechataddress_loc).send_keys(wechataddress)#输入微信地址
        self.find_element(*self.shop_add_edit_mall_loc).send_keys(mall)#输入所在商场
        self.find_element(*self.shop_add_edit_save_button_loc).click()#点击保存
        self.find_element(*self.shop_add_edit_ok_button_loc).click()#点击ok


    #查看/编辑门店
    def shop_edit(self,brand,area,province,city,name,type,address,wechataddress,mall,status):
        sleep(1)
        self.find_element(*self.shop_edit_button_loc).click()#点击编辑按钮
        sleep(1)
        #品牌修改
        self.find_element(*self.shop_add_edit_brand_loc).click()
        sleep(1)
        self.find_element(*self.shop_add_edit_brand_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('brand')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="shop"]/div[1]/div/div/div[2]/div/div[%s]' % brand).click()
        sleep(1)
        # 地区选择
        self.find_element(*self.shop_add_edit_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="shop"]/div[2]/div/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        # 省份选择
        self.find_element(*self.shop_add_edit_province_loc).click()
        sleep(1)
        provinces = self.driver.find_element_by_name('provinceid')
        sleep(1)
        provinces.find_element_by_xpath('//*[@id="shop"]/div[3]/div/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        # 城市选择
        self.find_element(*self.shop_add_edit_city_loc).click()
        sleep(1)
        citys = self.driver.find_element_by_name('cityid')
        sleep(1)
        citys.find_element_by_xpath('//*[@id="shop"]/div[4]/div/div/div[2]/div/div[%s]' % city).click()
        sleep(1)
        # 状态选择
        self.find_element(*self.shop_add_edit_status_loc).click()
        sleep(1)
        statuss = self.driver.find_element_by_name('status')
        sleep(1)
        statuss.find_element_by_xpath('//*[@id="shop"]/div[11]/div/div/div[2]/div/div[%s]' % status).click()
        sleep(1)
        # 类型选择
        self.find_element(*self.shop_add_edit_type_loc).click()
        sleep(1)
        types = self.driver.find_element_by_name('shop_type')
        sleep(1)
        types.find_element_by_xpath('//*[@id="shop"]/div[7]/div/div/div[2]/div/div[%s]' % type).click()
        sleep(1)
        #-----------------------------------------------------------------------
        self.find_element(*self.shop_add_edit_name_loc).clear()#名称编辑框清空
        self.find_element(*self.shop_add_edit_name_loc).send_keys(name)#修改名称
        self.find_element(*self.shop_add_edit_address_loc).clear()#地址编辑框清空
        self.find_element(*self.shop_add_edit_address_loc).send_keys(address)#修改地址
        self.find_element(*self.shop_add_edit_wechataddress_loc).clear()#微信地址编辑框清空
        self.find_element(*self.shop_add_edit_wechataddress_loc).send_keys(wechataddress)#修改微信地址
        self.find_element(*self.shop_add_edit_mall_loc).clear()#所在商场编辑框清空
        self.find_element(*self.shop_add_edit_mall_loc).send_keys(mall)#修改所在商场
        self.find_element(*self.shop_add_edit_save_button_loc).click()#点击保存
        self.find_element(*self.shop_add_edit_ok_button_loc).click()#点击ok

    #删除门店
    def shop_delete(self):
        sleep(1)
        self.driver.find_element_by_class_name('delete-btn').click()
        sleep(1)
        self.find_element(*self.shop_delete_comfirm_loc).click()
        sleep(1)
        self.find_element(*self.shop_delete_ok_loc).click()
        sleep(1)

    #导出文件
    def shop_export(self):
        def shop_cleanDir(rootdir):
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
        shop_cleanDir(rootdir)
        sleep(3)
        self.find_element(*self.shop_export_button_loc).click()
        sleep(3)
        if os.listdir(rootdir):
            return True
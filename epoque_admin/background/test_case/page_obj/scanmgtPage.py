# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class scanmgt(Page):

    url = "/admin/scanner-bind"

    scanmgt_search_id_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[1]/div[1]/input')#设备编号
    scanmgt_search_shop_name_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[1]/div[2]/input')#门店名称
    scanmgt_search_shop_code_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[1]/div[3]/input')#门店代码
    scanmgt_search_brand_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[1]/input')#品牌
    scanmgt_search_area_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[3]/div[1]/div/div[1]/div')#所在地区
    scanmgt_search_province_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[3]/div[2]/div/div[1]/div')#所在省份
    scanmgt_search_city_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[3]/div[3]/div/div[1]/div')#所在城市
    scanmgt_search_type_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[2]/div[2]/div/div[1]/input')#门店类型
    scanmgt_search_status_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[2]/div[3]/div/div[1]/input')#设备状态
    scanmgt_search_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[3]/div[4]/div[1]')#查询按钮
    scanmgt_add_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[3]/div[4]/div[2]')#新建扫描仪档案按钮
    scanmgt_export_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div[3]/div[4]/div[3]')#导出按钮
    scanmgt_edit_button_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[14]/div/a')
    scanmgt_delete_comfirm_loc = (By.XPATH,'/html/body/div[3]/div/div/div[2]/button[2]')#删除确认按钮
    scanmgt_delete_ok_loc = (By.XPATH,'/html/body/div[3]/div/div/div[2]/button')#删除ok按钮
    scanmgt_lastpage_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[3]/div/ol/li[1]/a')#上一页
    scanmgt_nextpage_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[3]/div/ol/li[8]/a')#下一页
    scanmgt_add_edit_id_loc = (By.XPATH,"//*[@id='search-scanner-btn']")#新增扫描仪编号按钮
    scanmgt_add_edit_id_select_loc = (By.XPATH,'//*[@id="scannerBind"]/div[1]/div/div/input')#新增扫描仪编号选择按钮
    scanmgt_add_edit_status_loc = (By.XPATH,'//*[@id="scannerBind"]/div[2]/div/select')#新增/编辑扫描仪状态按钮
    scanmgt_add_edit_mac_loc = (By.XPATH,'//*[@id="scannerBind"]/div[3]/div/input')#新增/编辑扫描仪MAC地址
    scanmgt_add_edit_code_loc = (By.XPATH,'//*[@id="scannerBind"]/div[4]/div/div/input')#新增/编辑门店代码按钮
    scanmgt_add_edit_code_select_loc = (By.XPATH,'//*[@id="scannerBind"]/div[5]/div/input')#新增/编辑门店名称
    scanmgt_add_edit_staff_loc = (By.XPATH,'//*[@id="scannerBind"]/div[6]/div/input')#新增/编辑管理员
    scanmgt_add_edit_email_loc = (By.XPATH,'//*[@id="scannerBind"]/div[7]/div/input')#新增/编辑邮箱地址
    scanmgt_add_edit_phone_loc = (By.XPATH,'//*[@id="scannerBind"]/div[8]/div/input')#新增/编辑联系电话
    scanmgt_add_edit_time_loc = (By.XPATH,'//*[@id="scannerBind"]/div[9]/div/input')#设备到店日期
    scanmgt_add_edit_save_button_loc = (By.XPATH, '//*[@id="save-btn"]')#新增编辑扫描仪保存按钮
    scanmgt_add_edit_ok_button_loc = (By.XPATH, "/html/body/div[3]/div/div/div[2]/button")#新增编辑扫描仪ok按钮
    scanmgt_add_edit_switch_button_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/ul/li[2]/a')#切换到门店记录按钮
    scanmgt_edit_editshop_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[9]/div/button[1]')#修改门店信息
    scanmgt_edit_addbindshop_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[2]/td/button[1]')#新增绑定门店
    scanmgt_edit_starttime_loc = (By.NAME,"from_date")#统计开始日期
    scanmgt_edit_endtime_loc = (By.NAME,"to_date")#统计结束日期
    scanmgt_info_model = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[1]')#首行设备型号信息
    scanmgt_info_id = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[2]')#首行设备编号信息
    scanmgt_info_area = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[3]')#首行地区信息
    scanmgt_info_province = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[4]')#首行省份信息
    scanmgt_info_city = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[5]')#首行城市信息
    scanmgt_info_brand = (By.XPATH, '//*[@id="wrap"]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[6]')#首行品牌信息
    scanmgt_info_name = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[7]")#首行门店名称信息
    scanmgt_info_code = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[8]")#首行门店代码信息
    scanmgt_info_type = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[9]")#首行门店类型信息
    scanmgt_info_staff = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[10]")#首行维护员信息
    scanmgt_info_phone = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[11]")#首行联系电话信息
    scanmgt_info_status = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[12]")#首行设备状态信息
    scanmgt_info_address = (By.XPATH, "//*[@id='wrap']/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[13]")#首行详细地址信息

    #设备编号搜索
    def scanmgt_search_id(self,id):
        sleep(1)
        self.find_element(*self.scanmgt_search_id_loc).clear()
        sleep(1)
        self.find_element(*self.scanmgt_search_id_loc).send_keys(id)
    def search_id_success_mgt(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_id).text

    #门店名称搜索
    def scanmgt_search_shop_name(self,model):
        sleep(1)
        self.find_element(*self.scanmgt_search_shop_name_loc).clear()
        sleep(1)
        self.find_element(*self.scanmgt_search_shop_name_loc).send_keys(model)
    def search_shop_name_success_mgt(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_name).text

    #门店代码搜索
    def scanmgt_search_shop_code(self,shop_code):
        sleep(1)
        self.find_element(*self.scanmgt_search_shop_code_loc).clear()
        sleep(1)
        self.find_element(*self.scanmgt_search_shop_code_loc).send_keys(shop_code)
    def search_shop_code_success_mgt(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_code).text

    #品牌搜索
    def scanmgt_search_brand(self,brand):
        sleep(1)
        self.find_element(*self.scanmgt_search_brand_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('brand')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[1]/div/div[2]/div/div[%s]'%brand).click()
        sleep(1)
    def search_brand_success_mgt(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_brand).text

    #地区搜索
    def scanmgt_search_area(self, area):
        sleep(1)
        self.find_element(*self.scanmgt_search_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="epoque-search"]/div/div[3]/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
    def search_area_success_mgt(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_area).text

    #省份搜索
    def scanmgt_search_province(self, area, province):
        sleep(1)
        self.find_element(*self.scanmgt_search_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="epoque-search"]/div/div[3]/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.scanmgt_search_province_loc).click()
        sleep(1)
        provinces = self.driver.find_element_by_name('provinceid')
        sleep(1)
        provinces.find_element_by_xpath('//*[@id="epoque-search"]/div/div[3]/div[2]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
    def search_province_success_mgt(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_province).text

    #城市搜索
    def scanmgt_search_city(self, area, province, city):
        sleep(1)
        self.find_element(*self.scanmgt_search_area_loc).click()
        sleep(1)
        areas = self.driver.find_element_by_name('regionid')
        sleep(1)
        areas.find_element_by_xpath('//*[@id="epoque-search"]/div/div[3]/div[1]/div/div[2]/div/div[%s]' % area).click()
        sleep(1)
        self.find_element(*self.scanmgt_search_province_loc).click()
        sleep(1)
        provinces = self.driver.find_element_by_name('provinceid')
        sleep(1)
        provinces.find_element_by_xpath('//*[@id="epoque-search"]/div/div[3]/div[2]/div/div[2]/div/div[%s]' % province).click()
        sleep(1)
        self.find_element(*self.scanmgt_search_city_loc).click()
        sleep(1)
        citys = self.driver.find_element_by_name('cityid')
        sleep(1)
        citys.find_element_by_xpath('//*[@id="epoque-search"]/div/div[3]/div[3]/div/div[2]/div/div[%s]' % city).click()
        sleep(1)
    def search_city_success_mgt(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_city).text

    # 门店类型搜索
    def scanmgt_search_type(self, type):
        sleep(1)
        self.find_element(*self.scanmgt_search_type_loc).click()
        sleep(1)
        statuss = self.driver.find_element_by_name('shop_type')
        sleep(1)
        statuss.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[2]/div/div[2]/div/div[%s]' % type).click()
        sleep(1)
    def search_type_success_mgt(self):
        return self.find_element(*self.scanmgt_info_type).text

    #状态搜索
    def scanmgt_search_status(self,status):
        sleep(1)
        self.find_element(*self.scanmgt_search_status_loc).click()
        sleep(1)
        statuss = self.driver.find_element_by_name('status')
        sleep(1)
        statuss.find_element_by_xpath('//*[@id="epoque-search"]/div/div[2]/div[3]/div/div[2]/div/div[%s]'% status).click()
        sleep(1)
    def search_status_success_mgt(self):
        return self.find_element(*self.scanmgt_info_status).text

    #下一页
    def scanmgt_nextpage(self):
        sleep(1)
        self.find_element(*self.scanmgt_nextpage_loc).click()

    #上一页
    def scanmgt_lastpage(self):
        sleep(1)
        self.find_element(*self.scanmgt_lastpage_loc).click()

    #查询按钮
    def scanmgt_search_button(self):
        sleep(1)
        self.find_element(*self.scanmgt_search_button_loc).click()

    #访问扫描仪档案
    def surf_scanmgt(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get('http://bossdev.epoque.cn/admin/scanner-bind')
        self.open()

    #首行品牌信息
    def scanmgt_brand_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_brand).text

    #首行设备编号信息
    def scanmgt_id_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_id).text

    #首行设备型号信息
    def scanmgt_model_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_model).text

    #首行门店名称信息
    def scanmgt_shop_name_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_name).text

    #首行地区信息
    def scanmgt_area_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_area).text

    #首行省份信息
    def scanmgt_province_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_province).text

    #首行城市信息
    def scanmgt_city_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_city).text

    #首行类型信息
    def scanmgt_type_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_type).text

    #首行门店代码信息
    def scanmgt_code_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_code).text

    #首行管理员信息
    def scanmgt_staff_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_staff).text

    #首行联系方式信息
    def scanmgt_phone_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_phone).text

    #首行详细地址信息
    def scanmgt_address_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_address).text

    #首行设备状态信息
    def scanmgt_status_info(self):
        sleep(1)
        return self.find_element(*self.scanmgt_info_status).text

    #新增扫描仪
    def scanmgt_add(self,id,code,name,email,mac,staff,phone,time,status):
        sleep(1)
        self.find_element(*self.scanmgt_add_button_loc).click()#点击新增按钮
        sleep(1)
        #扫描仪编号选择
        js1 = 'document.getElementsByName("scanner_id")[0].removeAttribute("readonly");'
        self.driver.execute_script(js1)#使扫描仪编辑框可写
        self.driver.find_element_by_xpath('//*[@id="scannerBind"]/div[1]/div/div/input').send_keys(id)
        #门店代码选择
        js2 = 'document.getElementsByName("shop_code")[0].removeAttribute("readonly");'
        self.driver.execute_script(js2)#使门店代码编辑框可写
        self.driver.find_element_by_xpath('//*[@id="scannerBind"]/div[4]/div/div/input').send_keys(code)
        #门店名称选择
        js3 = 'document.getElementsByName("shop_name")[0].removeAttribute("readonly");'
        self.driver.execute_script(js3)#使门店名称编辑框可写
        self.driver.find_element_by_xpath('//*[@id="scannerBind"]/div[5]/div/input').send_keys(name)
        #状态选择
        Select(self.driver.find_element_by_name('status')).select_by_value(status)
        #-----------------------------------------------------------------------
        self.find_element(*self.scanmgt_add_edit_mac_loc).send_keys(mac)#输入mac地址
        self.find_element(*self.scanmgt_add_edit_staff_loc).send_keys(staff)#输入管理员
        self.find_element(*self.scanmgt_add_edit_phone_loc).send_keys(phone)#输入phone
        self.find_element(*self.scanmgt_add_edit_email_loc).send_keys(email)#输入email
        self.find_element(*self.scanmgt_add_edit_time_loc).send_keys(time)#输入设备到店时间
        self.find_element(*self.scanmgt_add_edit_save_button_loc).click()#点击保存
        self.find_element(*self.scanmgt_add_edit_ok_button_loc).click()#点击ok

    #查看/编辑扫描仪
    def scanmgt_edit(self,code,name,email,mac,staff,phone,time,status,add_starttime,add_endtime,edit_starttime,edit_endtime,history_code_edit,history_code_add,history_name_add,history_name_edit):
        sleep(1)
        self.find_element(*self.scanmgt_edit_button_loc).click()#点击编辑按钮
        sleep(1)
        self.find_element(*self.scanmgt_add_edit_switch_button_loc).click()#切换至门店记录
        sleep(1)
        self.find_element(*self.scanmgt_edit_editshop_loc).click()#点击门店记录的修改按钮
        sleep(1)
        js3 = 'document.getElementsByName("shop_code")[0].removeAttribute("readonly");'
        self.driver.execute_script(js3)  # 使门店记录的编号可写
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/input').clear()#清空门店编号
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/input').send_keys(history_code_edit)#输入门店编号
        sleep(1)
        js4 = 'document.getElementsByName("shop_name")[0].removeAttribute("readonly");'
        self.driver.execute_script(js4)  # 使门店记录的名称可写
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/input').clear()#清空门店名称
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/input').send_keys(history_name_edit)#输入门店名称
        sleep(1)
        self.find_element(*self.scanmgt_edit_starttime_loc).clear()#清空门店记录的开始时间
        self.find_element(*self.scanmgt_edit_starttime_loc).send_keys(edit_starttime)#修改开始时间
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/ul').click()#使页面失去焦点
        sleep(1)
        self.find_element(*self.scanmgt_edit_endtime_loc).clear()#清空门店记录的结束时间
        self.find_element(*self.scanmgt_edit_endtime_loc).send_keys(edit_endtime)#修改结束时间
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/ul').click()
        sleep(1)
        check = self.driver.find_element_by_name('status')
        check.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[6]/select/option[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[9]/div/button[1]').click()#点击确认
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button').click()#点击ok
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/ul/li[1]/a').click()#切换至扫描仪详情
        sleep(1)
        #门店代码修改
        js1 = 'document.getElementsByName("shop_code")[0].removeAttribute("readonly");'
        self.driver.execute_script(js1)
        self.driver.find_element_by_xpath('//*[@id="scannerBind"]/div[4]/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="scannerBind"]/div[4]/div/div/input').send_keys(code)
        sleep(1)
        #门店名称选择
        js2 = 'document.getElementsByName("shop_name")[0].removeAttribute("readonly");'
        self.driver.execute_script(js2)
        self.driver.find_element_by_xpath('//*[@id="scannerBind"]/div[5]/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="scannerBind"]/div[5]/div/input').send_keys(name)
        sleep(1)
        #状态修改
        Select(self.driver.find_element_by_name('status')).select_by_value(status)
        # -----------------------------------------------------------------------
        sleep(1)
        self.find_element(*self.scanmgt_add_edit_mac_loc).clear()#清空mac地址
        self.find_element(*self.scanmgt_add_edit_mac_loc).send_keys(mac)#修改mac地址
        sleep(1)
        self.find_element(*self.scanmgt_add_edit_staff_loc).clear()#清空管理员
        self.find_element(*self.scanmgt_add_edit_staff_loc).send_keys(staff)#修改管理员
        sleep(1)
        self.find_element(*self.scanmgt_add_edit_phone_loc).clear()#清空phone
        self.find_element(*self.scanmgt_add_edit_phone_loc).send_keys(phone)#修改phone
        sleep(1)
        self.find_element(*self.scanmgt_add_edit_email_loc).clear()#清空email
        self.find_element(*self.scanmgt_add_edit_email_loc).send_keys(email)#修改email
        sleep(1)
        self.find_element(*self.scanmgt_add_edit_time_loc).clear()#清空设备到店时间
        self.find_element(*self.scanmgt_add_edit_time_loc).send_keys(time)#修改设备到店时间
        sleep(1)
        self.find_element(*self.scanmgt_add_edit_save_button_loc).click()
        sleep(1)
        self.find_element(*self.scanmgt_add_edit_ok_button_loc).click()
        sleep(1)
        self.driver.get('http://bossdev.epoque.cn/admin/scanner-bind')
        sleep(1)
        self.find_element(*self.scanmgt_edit_button_loc).click()#再次点击编辑按钮
        sleep(1)
        self.find_element(*self.scanmgt_add_edit_switch_button_loc).click()#切换至门店记录
        sleep(1)
        self.find_element(*self.scanmgt_edit_addbindshop_loc).click()#点击门店记录的新增按钮
        sleep(1)
        js5 = 'document.getElementsByName("shop_code")[0].removeAttribute("readonly");'
        self.driver.execute_script(js5)#使门店记录的编号可写
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[2]/div/input').send_keys(history_code_add)#输入门店编号
        sleep(1)
        js6 = 'document.getElementsByName("shop_name")[0].removeAttribute("readonly");'
        self.driver.execute_script(js6)#使门店记录的名称可写
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/input').send_keys(history_name_add)#输入门店名称
        sleep(1)
        self.find_element(*self.scanmgt_edit_starttime_loc).clear()#清空门店记录的开始时间
        self.find_element(*self.scanmgt_edit_starttime_loc).send_keys(add_starttime)#输入开始时间
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/ul').click()
        sleep(1)
        self.find_element(*self.scanmgt_edit_endtime_loc).clear()#清空门店记录的结束时间
        self.find_element(*self.scanmgt_edit_endtime_loc).send_keys(add_endtime)#输入结束时间
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/ul').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[9]/div/button[1]').click()#点击保存
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button').click()#点击ok
        sleep(1)
        self.driver.get('http://bossdev.epoque.cn/admin/scanner-bind')

    #删除扫描仪
    def scanmgt_delete(self):
        sleep(1)
        self.driver.find_element_by_class_name('delete-btn').click()
        sleep(1)
        self.find_element(*self.scanmgt_delete_comfirm_loc).click()
        sleep(1)
        self.find_element(*self.scanmgt_delete_ok_loc).click()

    #导出文件
    def scanmgt_export(self):
        def scanmgt_cleanDir(rootdir):
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
        scanmgt_cleanDir(rootdir)
        sleep(3)
        self.find_element(*self.scanmgt_export_button_loc).click()
        sleep(3)
        if os.listdir(rootdir):
            return True
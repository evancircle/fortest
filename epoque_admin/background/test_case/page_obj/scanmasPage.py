# -*- coding: utf-8 -*-
import os
import urllib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base import Page

class scanmas(Page):

    url = "/admin/scanner"

    scanmas_search_id_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[1]/input')#扫描仪编号
    scanmas_search_model_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[2]/input')#扫描仪型号
    scanmas_search_model_name_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[3]/input')#型号名称
    scanmas_search_brand_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[4]/div/div/div[1]/input')#扫描仪品牌
    scanmas_search_status_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[5]/div/div/div[1]/input')#扫描仪状态
    scanmas_search_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[6]/div[1]')#查询按钮
    scanmas_add_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[6]/div[2]')#新建扫描仪档案按钮
    scanmas_export_button_loc = (By.XPATH,'//*[@id="epoque-search"]/div/div/div[6]/div[3]')#导出按钮
    scanmas_edit_button_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[6]/div/a[1]')#查看/编辑按钮
    scanmas_open_stop_button_loc = (By.XPATH,'html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[6]/div/button')#启用/停用按钮
    scanmas_open_stop_comfirm_loc = (By.XPATH,'/html/body/div[3]/div/div/div[2]/button[2]')#启用/停用确定按钮
    scanmas_open_stop_ok_loc = (By.XPATH,'/html/body/div[3]/div/div/div[2]/button')#启用/停用ok按钮
    scanmas_delete_comfirm_loc = (By.XPATH,"/html/body/div[3]/div/div/div[2]/button[2]")#删除确认按钮
    scanmas_delete_ok_loc = (By.XPATH,"/html/body/div[3]/div/div/div[2]/button")#删除ok按钮
    scanmas_lastpage_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[1]/a')#上一页
    scanmas_nextpage_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[3]/div/ol/li[8]/a')#下一页
    scanmas_add_edit_model_loc = (By.XPATH,'//*[@id="scanner"]/div[2]/div/input')#新增/编辑扫描仪型号
    scanmas_add_edit_model_name_loc = (By.XPATH,'//*[@id="scanner"]/div[3]/div/input')#新增/编辑型号名称
    scanmas_add_edit_id_loc = (By.XPATH,'//*[@id="scanner"]/div[4]/div/input')#新增/编辑扫描仪编号
    scanmas_add_edit_remark_loc = (By.XPATH,'//*[@id="scanner"]/div[5]/div/textarea')#新增/编辑备注
    scanmas_add_edit_status_loc = (By.XPATH,'//*[@id="scanner"]/div[6]/div/div/div[1]/div')#新增/编辑状态下拉按钮
    scanmas_info_brand = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[1]')#首行扫描仪品牌信息
    scanmas_info_model = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[2]')#首行扫描仪型号信息
    scanmas_info_model_name = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]')#首行型号名称信息
    scanmas_info_id = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]')#首行扫描仪编号信息
    scanmas_info_status = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[5]')#首行扫描仪状态信息
    scanmas_add_edit_save_button_loc = (By.XPATH, "//*[@id='save-btn']")#新增编辑扫描仪保存按钮
    scanmas_add_edit_ok_button_loc = (By.XPATH, "/html/body/div[3]/div/div/div[2]/button")#新增编辑扫描仪ok按钮

    #扫描仪编号搜索
    def scanmas_search_id(self,id):
        sleep(1)
        self.find_element(*self.scanmas_search_id_loc).clear()
        sleep(1)
        self.find_element(*self.scanmas_search_id_loc).send_keys(id)
    def search_id_success_mas(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_id).text

    #扫描仪型号搜索
    def scanmas_search_model(self,model):
        sleep(1)
        self.find_element(*self.scanmas_search_model_loc).clear()
        sleep(1)
        self.find_element(*self.scanmas_search_model_loc).send_keys(model)
    def search_model_success_mas(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_model).text

    #型号名称搜索
    def scanmas_search_model_name(self,model_name):
        sleep(1)
        self.find_element(*self.scanmas_search_model_name_loc).clear()
        sleep(1)
        self.find_element(*self.scanmas_search_model_name_loc).send_keys(model_name)
    def search_model_name_success_mas(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_model_name).text

    #扫描仪品牌搜索
    def scanmas_search_brand(self):
        sleep(1)
        self.find_element(*self.scanmas_search_brand_loc).click()
        sleep(1)
        brands = self.driver.find_element_by_name('brand')
        sleep(1)
        brands.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[4]/div/div/div[2]/div/div').click()
        sleep(1)
    def search_brand_success_mas(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_brand).text

    #扫描仪状态搜索
    def scanmas_search_status(self,status):
        sleep(1)
        self.find_element(*self.scanmas_search_status_loc).click()
        sleep(1)
        statuss = self.driver.find_element_by_name('status')
        sleep(1)
        statuss.find_element_by_xpath('//*[@id="epoque-search"]/div/div/div[5]/div/div/div[2]/div/div[%s]'% status).click()
        sleep(1)
    def search_status_success_mas(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_status).text

    #下一页
    def scanmas_nextpage(self):
        sleep(1)
        self.find_element(*self.scanmas_nextpage_loc).click()

    #上一页
    def scanmas_lastpage(self):
        sleep(1)
        self.find_element(*self.scanmas_lastpage_loc).click()

    #查询按钮
    def scanmas_search_button(self):
        sleep(1)
        self.find_element(*self.scanmas_search_button_loc).click()

    #启用/停用按钮
    def scanmas_open_stop_button(self):
        sleep(1)
        self.find_element(*self.scanmas_open_stop_button_loc).click()
        sleep(1)
        self.find_element(*self.scanmas_open_stop_comfirm_loc).click()
        sleep(1)
        self.find_element(*self.scanmas_open_stop_ok_loc).click()

    # 访问扫描仪档案
    def surf_scanmas(self, username='admin', password='000000'):
        self.driver.get("http://bossdev.epoque.cn/login")
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)
        innerText =  self.driver.find_element_by_id("code_box").get_attribute('innerText')
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys(innerText)
        sleep(5)
        self.driver.find_element_by_id('login_submit').click()
        self.driver.get("http://bossdev.epoque.cn/admin/scanner")
        self.open()

    #首行扫描仪品牌信息
    def scanmas_brand_info(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_brand).text

    #首行扫描仪编号信息
    def scanmas_id_info(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_id).text

    #首行扫描仪型号信息
    def scanmas_model_info(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_model).text

    #首行扫描仪型号名称信息
    def scanmas_model_name_info(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_model_name).text

    #首行扫描仪状态信息
    def scanmas_status_info(self):
        sleep(1)
        return self.find_element(*self.scanmas_info_status).text

    #新增扫描仪
    def scanmas_add(self,id,model,model_name,remark,status):
        sleep(1)
        self.find_element(*self.scanmas_add_button_loc).click()#点击新增按钮
        sleep(1)
        #状态选择
        self.find_element(*self.scanmas_add_edit_status_loc).click()
        sleep(1)
        statuss = self.driver.find_element_by_name('status')
        sleep(1)
        statuss.find_element_by_xpath('//*[@id="scanner"]/div[6]/div/div/div[2]/div/div[%s]' % status).click()
        sleep(1)
        #-----------------------------------------------------------------------
        self.find_element(*self.scanmas_add_edit_id_loc).send_keys(id)#输入编号
        self.find_element(*self.scanmas_add_edit_model_name_loc).send_keys(model_name)#输入型号名称
        self.find_element(*self.scanmas_add_edit_model_loc).send_keys(model)#输入型号
        self.find_element(*self.scanmas_add_edit_remark_loc).send_keys(remark)#输入备注
        self.find_element(*self.scanmas_add_edit_save_button_loc).click()#点击保存
        self.find_element(*self.scanmas_add_edit_ok_button_loc).click()#点击ok


    #查看/编辑扫描仪
    def scanmas_edit(self,model,model_name,remark,status):
        sleep(1)
        self.find_element(*self.scanmas_edit_button_loc).click()#点击编辑按钮
        sleep(1)
        # 状态修改
        self.find_element(*self.scanmas_add_edit_status_loc).click()
        sleep(1)
        statuss = self.driver.find_element_by_name('status')
        sleep(1)
        statuss.find_element_by_xpath('//*[@id="scanner"]/div[6]/div/div/div[2]/div/div[%s]' % status).click()
        sleep(1)
        # -----------------------------------------------------------------------
        self.find_element(*self.scanmas_add_edit_model_name_loc).clear()
        self.find_element(*self.scanmas_add_edit_model_name_loc).send_keys(model_name)#修改型号名称
        self.find_element(*self.scanmas_add_edit_model_loc).clear()
        self.find_element(*self.scanmas_add_edit_model_loc).send_keys(model)#修改型号
        self.find_element(*self.scanmas_add_edit_remark_loc).clear()
        self.find_element(*self.scanmas_add_edit_remark_loc).send_keys(remark)#修改备注
        self.find_element(*self.scanmas_add_edit_save_button_loc).click()#点击保存
        self.find_element(*self.scanmas_add_edit_ok_button_loc).click()#点击ok

    #删除扫描仪
    def scanmas_delete(self):
        sleep(1)
        self.driver.find_element_by_class_name('delete-btn').click()
        sleep(1)
        self.find_element(*self.scanmas_delete_comfirm_loc).click()
        sleep(1)
        self.find_element(*self.scanmas_delete_ok_loc).click()
        sleep(2)

    #导出文件
    def scanmas_export(self):
        def scanmas_cleanDir(rootdir):
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
        scanmas_cleanDir(rootdir)
        sleep(3)
        self.find_element(*self.scanmas_export_button_loc).click()
        sleep(3)
        if os.listdir(rootdir):
            return True
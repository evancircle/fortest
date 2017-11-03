# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
import os
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.targetPage import target
from selenium.webdriver.common.by import By


class targetTest(myunit.MyTest):
    """目标配置测试"""

    def target_login_verify(self, username="admin", password="000000"):
        target(self.driver).surf_target(username, password)

    def test_1_target_add(self):
        """新增全国目标"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_add(goal_range='country',start_date='2017-09-01',end_date='2017-09-02',weekday='1',weekend='1',text=u'这是全国备注',select='1')
        po.target_search_date(start_date='2017-09-01',end_date='2017-09-02')
        po.target_search_goal_range(range=1)
        po.target_search_button()
        self.assertEqual(po.target_info_goal_range(),u'全国')
        self.assertEqual(po.target_info_goal(),'1094')
        self.assertEqual(po.target_info_date(),u'2017-09-01 至 2017-09-02')
        function.insert_img(self.driver, "country_target_add_successs.jpg")


    def test_2_target_add(self):
        """新增地区目标"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_add(goal_range='region', start_date='2017-09-03', end_date='2017-09-04', weekday='1', weekend='1',
                      text=u'这是地区备注', select='2')
        po.target_search_date(start_date='2017-09-03', end_date='2017-09-04')
        po.target_search_goal_range(range=2)
        po.target_search_button()
        self.assertEqual(po.target_info_goal_range(), u'地区')
        self.assertEqual(po.target_info_goal(), '322')
        self.assertEqual(po.target_info_date(), u'2017-09-03 至 2017-09-04')
        function.insert_img(self.driver, "region_target_add_successs.jpg")

    def test_3_target_add(self):
        """新增城市目标"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_add(goal_range='city', start_date='2017-09-08', end_date='2017-09-09', weekday='1', weekend='1',
                      text=u'这是城市备注', select='3')
        po.target_search_date(start_date='2017-09-08', end_date='2017-09-09')
        po.target_search_goal_range(range=3)
        po.target_search_button()
        self.assertEqual(po.target_info_goal_range(), u'城市')
        self.assertEqual(po.target_info_goal(), '24')
        self.assertEqual(po.target_info_date(), u'2017-09-08 至 2017-09-09')
        function.insert_img(self.driver, "city_target_add_successs.jpg")

    def test_4_target_add(self):
        """新增门店目标"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_add(goal_range='shop', start_date='2017-09-10', end_date='2017-09-11', weekday='1', weekend='1',
                      text=u'这是门店备注', select='4')
        po.target_search_date(start_date='2017-09-10', end_date='2017-09-11')
        po.target_search_goal_range(range=4)
        po.target_search_button()
        self.assertEqual(po.target_info_goal_range(), u'门店')
        self.assertEqual(po.target_info_goal(), '2')
        self.assertEqual(po.target_info_date(), u'2017-09-10 至 2017-09-11')
        function.insert_img(self.driver, "shop_target_add_successs.jpg")

    def test_5_target_edit(self):
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_search_date(start_date='2017-09-01', end_date='2017-09-02')
        po.target_search_goal_range(range=1)
        po.target_search_button()
        po.target_edit(weekday=2,weekend=2,text=u'这是修改后的备注')
        po.target_search_date(start_date='2017-09-01', end_date='2017-09-02')
        po.target_search_goal_range(range=1)
        po.target_search_button()
        self.assertEqual(po.target_info_goal(), '2188')
        function.insert_img(self.driver, "country_target_edit_successs.jpg")
        po.target_search_date(start_date='2017-09-08', end_date='2017-09-09')
        po.target_search_goal_range(range=3)
        po.target_search_button()
        po.target_edit(weekday=2, weekend=2, text=u'这是修改后的备注')
        po.target_search_date(start_date='2017-09-08', end_date='2017-09-09')
        po.target_search_goal_range(range=3)
        po.target_search_button()
        self.assertEqual(po.target_info_goal(), '48')
        function.insert_img(self.driver, "city_target_edit_successs.jpg")

    def test_6_target_delete(self):
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_search_date(start_date='2017-09-01', end_date='2017-09-02')
        po.target_search_goal_range(range=1)
        po.target_search_button()
        country_id = po.target_info_id()
        po.target_delete(targer_id=country_id)
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/div/table/tbody').find_elements(By.TAG_NAME, "tr")
        for i in table:
            p1 = (i.text).split(" ")
            for j in p1:
                self.assertNotEqual(j, country_id)
        function.insert_img(self.driver, "country_target_delete_successs.jpg")
        po.target_search_date(start_date='2017-09-03', end_date='2017-09-04')
        po.target_search_goal_range(range=2)
        po.target_search_button()
        region_id = po.target_info_id()
        po.target_delete(targer_id=region_id)
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/div/table/tbody').find_elements(By.TAG_NAME, "tr")
        for i in table:
            p2 = (i.text).split(" ")
            for j in p2:
                self.assertNotEqual(j, region_id)
        function.insert_img(self.driver, "region_target_delete_successs.jpg")
        po.target_search_date(start_date='2017-09-08', end_date='2017-09-09')
        po.target_search_goal_range(range=3)
        po.target_search_button()
        city_id = po.target_info_id()
        po.target_delete(targer_id=city_id)
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/div/table/tbody').find_elements(By.TAG_NAME, "tr")
        for i in table:
            p3 = (i.text).split(" ")
            for j in p3:
                self.assertNotEqual(j, city_id)
        function.insert_img(self.driver, "city_target_delete_successs.jpg")
        po.target_search_date(start_date='2017-09-10', end_date='2017-09-11')
        po.target_search_goal_range(range=4)
        po.target_search_button()
        shop_id = po.target_info_id()
        po.target_delete(targer_id=shop_id)
        table = self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div/div/div/div/table/tbody').find_elements(By.TAG_NAME, "tr")
        for i in table:
            p4 = (i.text).split(" ")
            for j in p4:
                self.assertNotEqual(j, shop_id)
        function.insert_img(self.driver, "shop_target_delete_successs.jpg")

    def test_target_search_area(self):
        """地区搜索"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_switch_detail()
        po.target_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.target_search_area(area=3)
        po.target_search_button()
        self.assertEqual(po.target_info_region(), u'华中')
        function.insert_img(self.driver, "target_search_area_successs.jpg")

    def test_target_search_province(self):
        """省份搜索"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_switch_detail()
        po.target_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.target_search_province(area=4,province=4)
        po.target_search_button()
        self.assertEqual(po.target_info_province(), u'河北省')
        function.insert_img(self.driver, "target_search_province_successs.jpg")

    def test_target_search_city(self):
        """城市搜索"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_switch_detail()
        po.target_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.target_search_city(area=4,province=6,city=2)
        po.target_search_button()
        self.assertEqual(po.target_info_city(), u'北京市')
        function.insert_img(self.driver, "target_search_city_successs.jpg")

    def test_target_search_shop(self):
        """门店搜索"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_switch_detail()
        po.target_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.target_search_shop(shop=u'石家庄北国奥特莱斯MAP')
        po.target_search_button()
        self.assertEqual(po.target_info_shop(), u'石家庄北国奥特莱斯MAP')
        function.insert_img(self.driver, "target_search_shop_successs.jpg")

    def test_target_search_date(self):
        """日期搜索"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_switch_detail()
        po.target_search_date(start_date='2017-10-01', end_date='2017-10-02')
        po.target_search_button()
        self.assertEqual(po.target_info_date(), u'2017-10-01 至 2017-10-02')
        function.insert_img(self.driver, "target_search_date_successs.jpg")

    def test_target_search_range(self):
        """目标范围搜索"""
        self.target_login_verify()
        sleep(2)
        po = target(self.driver)
        po.target_switch_detail()
        po.target_search_date(start_date='2017-10-01', end_date='2017-10-31')
        po.target_search_goal_range(range=3)
        po.target_search_button()
        self.assertEqual(po.target_info_goal_range(), u'城市')
        function.insert_img(self.driver, "target_search_range_successs.jpg")

if __name__ == "__main__":
    unittest.main()


# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import Remote

def browser():
    #分布式测试
    '''host = '192.168.3.146:4444'
    dc = {'browserName':'firefox'}
    driver = Remote(command_executor='http://' + host +'/wd/hub',
                    desired_capabilities=dc)'''
    #driver = webdriver.Firefox()#使用firefox进行测试
    driver = webdriver.Chrome(r"C:\Users\lenovo\Documents\Selenium\epoque_admin\background\driver\chromedriver.exe")#使用chrome进行测试
    driver.maximize_window()
    return driver

if __name__ == '__main__':
    driver = browser()
    driver.get("http://bossdev.epoque.cn/login")
    driver.quit()
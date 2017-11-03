from selenium import webdriver
import os

def insert_img(driver,file_name):
    # type: (object, object) -> object
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)

if __name__ ==  '__main__':
    driver = webdriver.Chrome(r"C:\Users\lenovo\Documents\Selenium\epoque_admin\background\driver\chromedriver.exe")
    driver.get("http://bossdev.epoque.cn/login")
    insert_img(driver,'epoque.jpg')
    driver.quit()
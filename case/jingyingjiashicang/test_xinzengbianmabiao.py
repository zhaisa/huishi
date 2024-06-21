import os
import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from case.touzi.getfiles import getfiles
from case.touzi.test_houpingjia_getproject import houpingjia_getproject


def add():
    executable_path = "C:\Program Files\Mozilla Firefox\geckodriver.exe"
    wd = webdriver.Firefox(executable_path=executable_path)
    # wd = webdriver.Firefox()
    wd.maximize_window()
    wd.implicitly_wait(30)
    wd.get('http://10.22.33.45:8769/hub/login/cockpit')
    wd.find_element(By.XPATH,'//section/section/main/div/div/div/div/form/div[2]/div/div/input').send_keys("admin")
    wd.find_element(By.XPATH,'//section/section/main/div/div/div/div/form/div[3]/div/div/input').send_keys("admin123")
    wd.find_element(By.XPATH,'//section/section/main/div/div/div/div/form/div[4]/button').click()
    time.sleep(2)
    wd.find_element(By.XPATH,'//section/header/div/div[1]/div[2]/ul/div/li[4]').click()
    time.sleep(2)
    wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[8]').click()
    time.sleep(2)
    for i in range(20):
        wd.find_element(By.XPATH,'//section/main/section/main/div[2]/div[1]/form/div[2]/button[2]/span').click()
        time.sleep(1)
        strtime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        wd.find_element(By.XPATH, '//div/div[2]/div/form/div[1]/div/div/input').clear()
        wd.find_element(By.XPATH,'//div/div[2]/div/form/div[1]/div/div/input').send_keys(f"数据名称_{strtime}")
        wd.find_element(By.XPATH, '//div/div[2]/div/form/div[2]/div/div/input').clear()
        wd.find_element(By.XPATH,'//div/div[2]/div/form/div[2]/div/div/input').send_keys(strtime)
        # wd.find_element(By.XPATH,'//div/div[2]/div/form/div[3]/div/div/div[1]/span/span/i').click()
        # wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,3)}]').pop().click()
        wd.find_element(By.XPATH,'//div/div[3]/span/button[2]/span').click()
        time.sleep(2)
    wd.quit()


if __name__ == '__main__':

    add()




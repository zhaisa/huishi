import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
def test_login():
    wd=webdriver.Chrome()
    wd.maximize_window()
    wd.get('http://10.22.33.101:32752/ind_net_fvue/index')
    time.sleep(1)
    try:
        loginelement=wd.find_element(By.XPATH,'//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/span')
    except NoSuchElementException:
        print('没有登录这个元素')
    loginelement.click()
    handles=wd.window_handles
    wd.switch_to.window(handles[1])
    print(wd.current_url)
    wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[2]/div/div[1]/input').send_keys('admin')
    wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[3]/div/div[1]/input').send_keys('Indnet123&')
    wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[4]/button').click()
    time.sleep(1)

if __name__ == '__main__':
    pytest.main(['--alluredir', './result', '-W', 'ignore:Module already imported:pytest.PytestWarning','test_login.py'])
    os.system("allure generate ./result/ -o /gyhlw/output/report/ --clean")
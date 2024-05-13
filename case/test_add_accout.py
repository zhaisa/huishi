import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def add_account(phone,num):
    wd = webdriver.Firefox()
    wd.maximize_window()
    wd.implicitly_wait(30)
    wd.get('http://18.0.144.248:8091/')

    wd.find_element(By.XPATH,'//form/div[1]/div/div/div[1]/div/input').send_keys("admin")
    wd.find_element(By.XPATH,'//form/div[2]/div/div/div[1]/div/input').send_keys("Jdl1234!")
    input1=input()
    wd.find_element(By.XPATH,'//form/div[3]/div/div/input').send_keys(input1)

    time.sleep(1)
    wd.find_element(By.XPATH,'//section/div/div[1]/div/ul/li[1]/div').click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/div/div[1]/div/ul/li[1]/ul/li[1]/div').click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/div/div[1]/div/ul/li[1]/ul/li[1]/ul/li[1]').click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//div/div[1]/div[2]/button[2]/span').click()
    time.sleep(0.5)

    wd.switch_to.frame("1694051364000.5132")
    wd.find_element(By.XPATH,'//div/div[1]/div[5]/div[2]/form/div[1]/div[1]/div/div/div/input').send_keys(f"wendang-{num}")
    wd.find_element(By.XPATH,'//div/div[1]/div[5]/div[2]/form/div[1]/div[2]/div/div/div/input').send_keys(f"文档管理员{num}")
    wd.find_element(By.XPATH,'//div/div[1]/div[5]/div[2]/form/div[2]/div[1]/div/div/div/input').send_keys("qweasd123!@#")
    wd.find_element(By.XPATH,'//div/div[1]/div[5]/div[2]/form/div[2]/div[2]/div/div/div/input').send_keys("qweasd123!@#")
    wd.find_element(By.XPATH,'//div[1]/div[1]/div[5]/div[2]/form/div[3]/div[1]/div/div/span/span').click()
    wd.find_elements(By.XPATH,'//ul[1]/li').pop().click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//ul[2]/li[1]').click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//*[@id="menu-6480-2-1"]').click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//*[@id="menu-6480-3-2"]').click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//div[1]/div[1]/div[5]/div[2]/form/div[3]/div[2]/div/div/div/input').send_keys(phone)
    wd.find_element(By.XPATH,'//div[1]/div[1]/div[5]/div[2]/form/div[4]/div[1]/div/div/div/div[1]/span/span/i').click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//div[3]/div[1]/div[1]/ul/li[1]/span').click()
    
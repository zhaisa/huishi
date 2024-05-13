import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_xietongchuangxin(sytle):
    wd = webdriver.Firefox()
    wd.maximize_window()
    wd.implicitly_wait(30)
    wd.get('http://10.22.33.153:31376/gdzbgtt/industryPolicy')

    wd.find_element(By.XPATH, '//section/div/div[1]/div/ul/li[5]').click()
    handles = wd.window_handles
    wd.switch_to.window(handles[1])
    wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[2]/div/div/input').send_keys("GJGDJT009")
    wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[3]/div/div/input').send_keys("welcome@2024")
    time.sleep(2)
    wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[4]/button').click()

    wd.find_element(By.XPATH, '//section/main/section/aside/div/div[2]/ul/li[6]/div').click()
    wd.find_element(By.XPATH, '//section/main/section/aside/div/div[2]/ul/li[6]/ul/li[1]/div').click()
    wd.find_element(By.XPATH, '//section/main/section/aside/div/div[2]/ul/li[6]/ul/li[1]/ul/li[3]').click()
    for i in range(20):
        wd.find_element(By.XPATH,'//section/main/section/main/div[2]/div/div/div[1]/form/div[2]/button[3]/i').click()
        wd.find_element(By.XPATH,'//form/div[2]/div[1]/div/div/div/input').send_keys("2022")
        wd.find_element(By.XPATH,'//form/div[2]/div[2]/div/div/div[1]/div/span/span/i').click()
        if sytle==1:

            wd.find_elements(By.XPATH,'//ul/li[1]').pop().click()
            wd.find_element(By.XPATH,'//form/div[3]/div[1]/div/div/div/input').send_keys(f"国家先进轨道交通装备创新中心-{i}")
            wd.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/input').send_keys(random.randint(1,100))
            wd.find_element(By.XPATH,'//form/div[3]/div[3]/div/div/div/textarea').send_keys("1.课题立项XX2.专利XX项3.科研成果转化XX……")
            wd.find_element(By.XPATH,'//form/div[4]/div[1]/div/div/div/input').send_keys("中车股份")
            wd.find_element(By.XPATH,'//form/div[4]/div[2]/div/div/div/input').send_keys("大连交通")
            wd.find_element(By.XPATH,'//form/div[5]/div[1]/div/div/div/textarea').send_keys("test_备注")
            wd.find_element(By.XPATH,'//div/div[3]/span/button[2]').click()
            time.sleep(1)
        elif sytle==2:

            wd.find_elements(By.XPATH, '//ul/li[2]').pop().click()
            #成果名称
            wd.find_element(By.XPATH,'//form/div[3]/div[1]/div/div/div[1]/input').send_keys(f"test_成果名称_{i}")
            wd.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/input').send_keys("test_完成单位")
            wd.find_element(By.XPATH,'//form/div[3]/div[3]/div/div/div/input').send_keys("test_评价形式")
            wd.find_element(By.XPATH,'//form/div[4]/div[1]/div/div/div/input').send_keys("test_评价水平")
            wd.find_element(By.XPATH,'//form/div[4]/div[2]/div/div/div/input').send_keys("test_成果体现形式")
            wd.find_element(By.XPATH,'//form/div[5]/div[1]/div/div/div/textarea').send_keys("test_备注")
            wd.find_element(By.XPATH, '//div/div[3]/span/button[2]').click()
            time.sleep(1)
        elif sytle==3:

            wd.find_elements(By.XPATH, '//ul/li[3]').pop().click()
            wd.find_element(By.XPATH,'//form/div[3]/div[1]/div/div/div[1]/input').send_keys(f"test_服务行业企业项目_{i}")
            wd.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/input').send_keys("test_项目")
            wd.find_element(By.XPATH,'//form/div[4]/div[1]/div/div/div/textarea').send_keys("1.课题立项XX2.专利XX项3.科研成果转化XX……")
            wd.find_element(By.XPATH,'//form/div[4]/div[2]/div/div/div/input').send_keys("中车集团")
            wd.find_element(By.XPATH,'//form/div[5]/div[1]/div/div/div/input').send_keys("test_服务企业")
            wd.find_element(By.XPATH,'//form/div[5]/div[2]/div/div/div/input').send_keys("test_备注")
            wd.find_element(By.XPATH, '//div/div[3]/span/button[2]').click()
            time.sleep(1)
    wd.quit()
if __name__ == '__main__':

    test_xietongchuangxin(sytle=2)





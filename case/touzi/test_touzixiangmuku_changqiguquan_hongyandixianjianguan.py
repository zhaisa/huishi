
import os
import random
import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def shenbao():
    wd = webdriver.Firefox()
    wd.maximize_window()
    wd.implicitly_wait(30)
    wd.get('http://10.22.33.44:8769/mvue/login/tzgl')
    #wd.get('http://10.209.2.244:8769/mvue/login/tzgl')
    time.sleep(2)
    wd.find_element(By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div[2]/form/div[2]/div/div[1]/input').send_keys(
        "admin")
    wd.find_element(By.XPATH, '//input[@type="password"]').send_keys('1234567')
    wd.find_element(By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div[2]/form/div[4]/div/button[1]').click()
    time.sleep(5)
    # 点击组织架构
    e1 = wd.find_element(By.XPATH, '//*[@id="app"]/section/section/div/aside/div[2]/div/div[5]//div[1]')

    e2 = e1.get_attribute("aria-controls")
    print(e2)
    e1.click()
    time.sleep(2)
    str1 = '//*[@id='
    str2 = ']/div/ul/li[2]/span'
    jsxpath = str1 + '"' + e2 + '"' + str2
    print(jsxpath)
    wd.find_element(By.XPATH, jsxpath).click()
    time.sleep(2)
    wd.find_element(By.XPATH,
                    '//*[@id="pane-userListManager"]/section/section/main/main/div[1]/div/div[1]/div[1]/div/input').send_keys(
        "李晓霞")
    time.sleep(1)
    wd.find_element(By.XPATH,
                    '//*[@id="pane-userListManager"]/section/section/main/main/div[1]/div/div[1]/div[1]/div/div/button').click()
    time.sleep(1)
    # 点击下拉按钮自动生成了一个id，通过aria_controls获取到
    webele1 = wd.find_element(By.XPATH, '//table/tbody/tr/td[9]/div/div/div/button[2]')
    webele1.click()
    webele2 = webele1.get_attribute("aria-controls")
    time.sleep(1)
    xpastr1 = '//*[@id='
    xpastr2 = ']/li[3]'
    jsxpath1 = xpastr1 + '"' + webele2 + '"' + xpastr2
    wd.find_element(By.XPATH, jsxpath1).click()  # 跳转前端登录
    time.sleep(2)
    handles = wd.window_handles
    wd.switch_to.window(handles[1])
    time.sleep(1)
    #跳转到前端后，需要选择所在公司
    wd.find_element(By.XPATH,
                    '//*[@id="app"]/section/main/div/div[3]/div/div[2]/form/div/div/div/div/input').click()

    wd.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span').click()

    wd.find_element(By.XPATH, '//*[@id="app"]/section/main/div/div[3]/div/div[3]/span/button/span').click()  # 点击确定
    # //*[@id="app"]/section/main/div/div[2]/div/div[3]/span/button
    time.sleep(2)
    # 选择投资项目库
    wd.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div/ul/li[5]').click()
    if wd.find_element(By.XPATH, '//section/header/div/div/div[1]/div[1]/h3').get_attribute("title") == "李晓霞":
        # WebDriverWait(wd, 20, 0.5).until(ec.element_to_be_clickable(
        #     (wd.find_element(By.XPATH, '//section/main/section/aside/div/div/ul/li[2]/ul/li[3]'))))
        time.sleep(5)
        wd.find_element(By.XPATH, '//section/main/section/aside/div/div/ul/li[3]/div').click()
        time.sleep(0.5)
        wd.find_element(By.XPATH, '//section/main/section/aside/div/div/ul/li[3]/ul/li[3]').click()
        time.sleep(0.5)
    else:
        time.sleep(4)
    # time.sleep(4)
        wd.find_element(By.XPATH,'//section/main/section/aside/div/div/ul/li[2]/div').click()
        time.sleep(0.5)
        wd.find_element(By.XPATH,'//section/main/section/aside/div/div/ul/li[2]/ul/li[3]').click()
        time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[1]/div/div/button[1]/span').click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/span/span/i').click()
    wd.find_elements(By.XPATH,'//ul/li[1]').pop().click()

    #经营情况
    wd.find_element(By.XPATH,"//section/main/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div[1]/div/div/div/input").send_keys("1000")
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div[2]/div/div/div/input').send_keys("800")
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div[3]/div/div/div[1]/input').send_keys("500")
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[1]/div/div/div/input').send_keys("800")
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[2]/div/div/div/input').send_keys("300")
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[3]/div/div/div/input').send_keys("500")
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/input').send_keys("232")
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[2]/div[2]/div[3]/div[3]/div/div/div/input').send_keys("45")
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[2]/div[2]/div[4]/div[1]/div/div/div/input').send_keys("120")
    time.sleep(0.5)
    #红线底线

    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[3]/div[2]/div[1]/div[1]/div/div/div/div/div[1]/span/span/i').click()
    wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,2)}]').pop().click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div[1]/span/span/i').click()
    wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 2)}]').pop().click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[3]/div[2]/div[1]/div[3]/div/div/div/div/div[1]/span/span/i').click()
    wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 2)}]').pop().click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[3]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/span/span/i').click()
    wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 2)}]').pop().click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,
                    '//section/main/section/main/div/div[2]/form/div[3]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/span/span/i').click()
    wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 2)}]').pop().click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,
                    '//section/main/section/main/div/div[2]/form/div[3]/div[2]/div[2]/div[3]/div/div/div/div/div[1]/span/span/i').click()
    wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 2)}]').pop().click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[3]/div[2]/div[3]/div[1]/div/div/div/div/div[1]/span/span/i').click()
    wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 2)}]').pop().click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div[3]/div[2]/div[3]/div[2]/div/div/div/div/div[1]/span/span/i').click()
    wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 2)}]').pop().click()
    time.sleep(0.5)
    wd.find_element(By.XPATH,'//section/main/section/main/div/div[1]/div/button[1]').click()
    time.sleep(2)
    wd.quit()

if __name__ == '__main__':
    for i in range(5):
        shenbao()
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_add_kaifachanjiaoziyuan(year,style,projectname):
    wd = webdriver.Firefox()
    wd.maximize_window()
    wd.implicitly_wait(30)
    wd.get('http://10.22.33.153:31376/gdzbgtt/industryPolicy')

    wd.find_element(By.XPATH,'//section/div/div[1]/div/ul/li[5]').click()
    handles=wd.window_handles
    wd.switch_to.window(handles[1])
    wd.find_element(By.XPATH,'//section/section/main/div/div/div/div/form/div[2]/div/div/input').send_keys("GJGDJT009")
    wd.find_element(By.XPATH,'//section/section/main/div/div/div/div/form/div[3]/div/div/input').send_keys("welcome@2024")
    time.sleep(1)
    wd.find_element(By.XPATH,'//section/section/main/div/div/div/div/form/div[4]/button').click()

    wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[6]/div').click()
    wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[6]/ul/li[1]/div').click()
    wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]').click()
    for i in range(20):
        wd.find_element(By.XPATH,'//section/main/section/main/div[2]/div/div/div[1]/form/div[2]/button[3]').click()


        wd.find_element(By.XPATH,'//form/div[1]/div[1]/div/div/div/input').send_keys(year)
        wd.find_element(By.XPATH,'//form/div[1]/div[2]/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH,f'//ul/li[{style}]').pop().click()
        wd.find_element(By.XPATH,'//form/div[2]/div[1]/div/div/div/input').send_keys(projectname)
        wd.find_element(By.XPATH,'//form/div[2]/div[2]/div/div/div/textarea').send_keys("1.颗粒化专业教学资源建设2.标准化课程、"
                                                                                        "专创融合课程、社会培训课程建设3.虚拟仿真"
                                                                                        "资源建设建设4.典型实训项目建设")
        wd.find_element(By.XPATH,'//form/div[2]/div[3]/div/div/div/input').send_keys("国家级专业教学资源库")
        wd.find_element(By.XPATH,'//form/div[3]/div[1]/div/div/div/input').send_keys("中车股份")
        wd.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/input').send_keys("大连交通大学")
        wd.find_element(By.XPATH,'//form/div[3]/div[3]/div/div/div/input').send_keys("2023-11")

        wd.find_element(By.XPATH,'//div/div[3]/span/button[2]').click()
        time.sleep(1)
    time.sleep(2)
    wd.quit()


if __name__ == '__main__':
    for i in range(1):
        strtime = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        projectname = f"《铁道机车运用与维护专业教学资源库_{strtime}》"
        test_add_kaifachanjiaoziyuan(year="2022",style="4",projectname=projectname)
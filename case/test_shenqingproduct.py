import os
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from public.reda_data import reda_pytestdata

yamlfile = os.path.basename(__file__).replace('py', 'yaml')  # 获取当前目运行文件
class Test_ShenQingProduct:
    @pytest.mark.parametrize("username",reda_pytestdata(yamlfile, 'test_shenqingproduct'))
    def test_shenqingproduct(self,username):
        wd = webdriver.Chrome()
        wd.maximize_window()
        wd.get('http://18.0.142.184:8769/ind_net_fvue/index')
        #time.sleep(3)
        wd.implicitly_wait(30)
        try:
            loginelement = wd.find_element(By.XPATH, '//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/div/span')
            # //*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/div/span
        except NoSuchElementException:
            print('没有登录这个元素')
        loginelement.click()
        wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[2]/div/div/input').send_keys(username)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[3]/div/div[1]/input').send_keys('Indnet123&')
        wd.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/form/div[4]/button').click()
        time.sleep(3)
        wd.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div[1]/img').click()
        time.sleep(2)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/div/div[6]/ul[1]/li[1]/div[1]/h6').click()
        time.sleep(1)
        handles=wd.window_handles
        wd.switch_to.window(handles[1])
        print(wd.current_url)
        time.sleep(2)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/div/div/div[2]/div/div/button[1]').click()
        time.sleep(2)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/div/div/div[6]/div/div[2]/div/div/div[1]/span/span/i').click()
        time.sleep(1)
        #选择项目
        wd.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/div/div/div[6]/div/div[3]/span/button[2]/span').click()
        time.sleep(3)
        handles = wd.window_handles
        wd.switch_to.window(handles[2])
        print(wd.current_url)
        time.sleep(5)

        iframes=wd.find_elements(By.TAG_NAME,'iframe')
        for iframe in iframes:
            print(iframe)
        wd.switch_to.frame(iframes[1])
        time.sleep(1)

        wd.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div/div[2]/div[1]/div/form/div[2]').click()

        time.sleep(1)
        myneed=wd.find_elements(By.XPATH,'//ul/li[1]').pop()
        myneed.click()
        wd.find_element(By.XPATH,'//*[@id="userName"]').send_keys("test_zhai")
        wd.find_element(By.XPATH,'//*[@id="userPwd"]').send_keys("mrzhai123!@#")
        time.sleep(1)
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div/div[2]/div[1]/div/form/div[5]').click()
        mycpu=wd.find_elements(By.XPATH,'//ul/li[1]').pop()
        mycpu.click()
        time.sleep(1)
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div/div[2]/div[1]/div/form/div[6]').click()
        mymem=wd.find_elements(By.XPATH,'//ul/li[1]').pop()
        mymem.click()
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div/div[2]/div[1]/div/form/div[7]/div[2]/div/span/div/div[2]/div/div[2]/input').send_keys("40")
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div/div[2]/div[1]/div/form/div[8]/div[2]/div/span/div/div[2]/div/div[2]/input').send_keys("20")
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div/div[2]/div[1]/div/form/div[9]').click()
        wd.find_elements(By.XPATH,'//ul/li[1]').pop().click()
        time.sleep(1)
        wd.find_element(By.XPATH,'//*[@id="instanceName"]').send_keys("test_schema12")
        wd.find_element(By.XPATH,'//*[@id="businessDesc"]').send_keys("test_add")
        time.sleep(2)
        #尺子分段，用js
        button=wd.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div/div[2]/div[1]/div/form/div[12]/div[2]/div/span/div/div[2]/div[5]/span[2]')
        ac=ActionChains(wd)
        ac.move_to_element(button).click().perform()
        time.sleep(1)

        wd.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div/div[2]/div[2]/div/div[2]/button').click()
        time.sleep(2)
        wd.find_element(By.XPATH,'//*[@id="additional.orderLinkNote"]').send_keys("add_add")
        # time.sleep(2)
        # wd.find_element(By.XPATH,'//div[@class="ant-slider-mark"]/span[2]').click()
        time.sleep(2)
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section/main/div[2]/div/div[2]/button[2]').click()
        time.sleep(2)
        wd.close()
        wd.quit()

    @pytest.mark.skip(reason="就是不想执行")
    def test_shenpi(self):
        wd = webdriver.Chrome()
        wd.maximize_window()
        wd.get('http://18.0.142.184:8769/ind_net_fvue/index')
        # time.sleep(3)
        wd.implicitly_wait(30)
        try:
            loginelement = wd.find_element(By.XPATH, '//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/div/span')
            # //*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/div/span
        except NoSuchElementException:
            print('没有登录这个元素')
        loginelement.click()
        wd.find_element(By.XPATH,
                        '//*[@id="app"]/section/section/main/div/div/div/div/form/div[2]/div/div/input').send_keys(
            '013700270075')
        wd.find_element(By.XPATH,
                        '//*[@id="app"]/section/section/main/div/div/div/div/form/div[3]/div/div[1]/input').send_keys(
            'Indnet123&')
        wd.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/form/div[4]/button').click()
        time.sleep(3)
        try:
            wd.find_element(By.XPATH,'//*[@id="app"]/section/main/div/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[6]/div/button').click()
        except NoSuchElementException:
            wd.close()
        time.sleep(1)
        handles=wd.window_handles
        wd.switch_to.window(handles[1])
        time.sleep(2)
        iframes = wd.find_elements(By.TAG_NAME, 'iframe')
        time.sleep(2)
        for iframe in iframes:
            print(iframe)
        wd.switch_to.frame(iframes[1])
        time.sleep(2)
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section/main/div[4]/div/form/div[3]/div/div/span/button').click()
        time.sleep(2)


        wd.close()
        wd.quit()

if __name__ == '__main__':

    pytest.main(['--alluredir', './result', '-W', 'ignore:Module already imported:pytest.PytestWarning','test_shenqingproduct.py'])
    os.system("allure generate ./result/ -o /gyhlw/output/report/ --clean")
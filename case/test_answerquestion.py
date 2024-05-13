import os
import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import pyautogui as pygui

from public.reda_data import reda_pytestdata

yamlfile = os.path.basename(__file__).replace('py', 'yaml')  # 获取当前目运行文件
class Test_Answerquestion:
    @pytest.mark.parametrize("content",reda_pytestdata(yamlfile, 'test_answerquestion'))
    def test_answerquestion(self,content):

        wd=webdriver.Chrome()
        wd.maximize_window()
        wd.get('http://10.22.33.101:32752/ind_net_fvue/index')
        time.sleep(1)
        try:
            loginelement=wd.find_element(By.XPATH,'//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/div/span')
            #//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/div/span
        except NoSuchElementException:
            print('没有登录这个元素')
        loginelement.click()
        # handles=wd.window_handles
        # wd.switch_to.window(handles[1])
        # print(wd.current_url)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[2]/div/div[1]/input').send_keys('450000000395')
        wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[3]/div/div[1]/input').send_keys('Indnet123&')
        wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[4]/button').click()
        time.sleep(2)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/header/div/div[1]/div[1]/img').click()
        time.sleep(2)
        e1=wd.find_element(By.XPATH,'//*[@id="app"]/section/div/div[1]/div/ul/div[1]/li[6]/span/span')
        e1.click()
        time.sleep(2)

        wd.find_element(By.XPATH,'//div[@class="nav"]/div[2]/div[4]').click()#自己写的相对路径，点击问题反馈
        wd.find_element(By.CLASS_NAME,'submit').click()
        time.sleep(3)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/div/form/div[1]/div/div/label[1]/span[1]/span').click()
        wd.find_element(By.XPATH,'//*[@id="app"]/section/div/form/div[2]/div/div/input').send_keys("如何正确安装MYSQL")
        e1=wd.find_element(By.XPATH,'//*[@id="app"]/section/div/form/div[3]/div/div/div[1]/input')
        e1.click()
        time.sleep(3)
        e3=wd.find_element(By.XPATH,'//div[@role="menu"][1]')
        e3.click()
        e2 = e3.get_attribute('id')
        print(e2)
        str1 = '//*[@id='
        str2 = ']/div/ul/li[1]'
        jsxpath = str1 + '"' + e2 + '"' + str2
        print(jsxpath)
        wd.find_element(By.XPATH,jsxpath).click()
        time.sleep(2)
        e4=wd.find_element(By.XPATH,'//div[@role="menu"][2]')
        e4.click()
        e5=e4.get_attribute('id')
        jsxpath2=str1 + '"' + e5 + '"' + str2
        print(jsxpath2)
        wd.find_element(By.XPATH,jsxpath2).click()
        time.sleep(2)
        iframe_id=wd.find_element(By.CLASS_NAME,'tox-edit-area__iframe').get_attribute('id')

        wd.switch_to.frame(iframe_id)
        wd.find_element(By.XPATH,'//*[@id="tinymce"]/p').send_keys(content)
        wd.switch_to.default_content()
        time.sleep(1)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/div/form/div[5]/div/div/div[1]/button/span').click()
        file_dir1 = 'D:\pic'  # 真的是历史上一大坑，/不行，非得\才行！
        mypic = 'f91b08a14f964875b5b19cb252554f04.png'
        file_dir = os.path.join(file_dir1, mypic)
        time.sleep(2)
        pygui.write(file_dir)
        time.sleep(3)
        pygui.press('enter', presses=2)
        time.sleep(5)
        wd.find_element(By.XPATH,'//*[@id="app"]/section/div/div/button[1]/span').click()



        wd.close()
        wd.quit()

if __name__ == '__main__':
    pytest.main(['--alluredir', './result', '-W', 'ignore:Module already imported:pytest.PytestWarning', 'test_answerquestion.py'])
    os.system("allure generate ./result/ -o /gyhlw/output/report/ --clean")

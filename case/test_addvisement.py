import os
import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import pyautogui as pygui
'''
测试登录后新增广告
'''
def test_add():
    wd = webdriver.Chrome()
    wd.maximize_window()
    wd.get('http://10.22.33.101:32752/ind_net_fvue/index')
    time.sleep(1)
    try:
        loginelement = wd.find_element(By.XPATH, '//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/div/span')#//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/div/span
    except NoSuchElementException:
        print('没有登录这个元素')
    loginelement.click()
    handles = wd.window_handles
    wd.switch_to.window(handles[1])
    print(wd.current_url)
    wd.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/form/div[2]/div/div[1]/input').send_keys(
        'admin')
    wd.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/form/div[3]/div/div[1]/input').send_keys(
        'Indnet123&')
    wd.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/form/div[4]/button').click()
    wd.implicitly_wait(30)

    e1=wd.find_element(By.XPATH,'//*[@id="app"]/section/header/div/div[1]/div[2]/ul/div[2]/div/span')
    e1.click()

    e2 = e1.get_attribute("aria-controls")
    time.sleep(5)
    # mouse_obj = ActionChains(wd)
    # mouse_obj.move_to_element(e1).click()
    # mouse_obj.key_down(Keys.PAGE_DOWN).click().perform()

    str1='//*[@id='
    str2=']/li[1]'
    jsxpath=str1+'"'+e2+'"'+str2
    print(jsxpath)
    wd.find_element(By.XPATH,jsxpath).click()
    time.sleep(1)
    print(wd.current_url)
    wd.refresh()
    time.sleep(3)

    wd.find_element(By.XPATH,'//*[@id="app"]/section/main/section/aside/div/div[2]/ul/li[3]/div').click()
    time.sleep(2)
    wd.find_element(By.XPATH,'//*[@id="app"]/section/main/section/aside/div/div[2]/ul/li[3]/ul/li').click()
    time.sleep(2)
    wd.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/div/div/form/button[3]').click()
    time.sleep(2)
    #动态获取新增弹出框
    str3='//*[@id='
    str4=']/div/div[1]/div[1]/div/div/div[1]/input'
    e4=wd.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/form/div/div/div[1]')
    e3=e4.get_attribute("aria-controls")
    jsxpath1=str3+'"'+e3+'"'+str4
    print('第二个动态jxpath:%s' %(jsxpath1))
    time.sleep(1)

    random_str =random.randint(9999,99999)

    ad_name="test_"+str(random_str)
    wd.find_element(By.XPATH,jsxpath1).send_keys(ad_name)#输入广告名称
    str5=']/div/div[1]/div[2]/div/div/div/div/input'
    jsxpath2=str3+'"'+e3+'"'+str5
    wd.find_element(By.XPATH,jsxpath2).click()
    time.sleep(2)
    wd.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]/span').click()#选择主广告
    str6=']/div/div[2]/div[1]/div/div/div/input'
    jsxpath2=str3+'"'+e3+'"'+str6
    wd.find_element(By.XPATH,jsxpath2).send_keys(str(random_str))#显示顺序
    str7=']/div/div[2]/div[2]/div/div/div/div/input'
    jsxpath3=str3+'"'+e3+'"'+str7
    wd.find_element(By.XPATH,jsxpath3).click()
    wd.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()#上传类型选择图片
    str8=']/div/div[3]/div/div/div/div/div/button/span'
    jsxpath4=str3+'"'+e3+'"'+str8
    wd.find_element(By.XPATH,jsxpath4).click()#等待上传出现
    time.sleep(2)
    file_dir1='D:\pic'#真的是历史上一大坑，/不行，非得\才行！
    mypic='f91b08a14f964875b5b19cb252554f04.png'
    file_dir=os.path.join(file_dir1,mypic)
    pygui.write(file_dir)
    time.sleep(2)
    pygui.press('enter',presses=2)
    time.sleep(1)
    str9=']/div/div[4]/div/div/div/div/input'
    jsxpath5=jsxpath3=str3+'"'+e3+'"'+str9
    wd.find_element(By.XPATH,jsxpath5).send_keys("https://www.baidu.com")
    wd.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/span/button[2]/span').click()
    time.sleep(2)
    wd.quit()
if __name__ == '__main__':
    # for i in range(2):
    #     pytest.main(
    #         ['--alluredir', './result', '-W', 'ignore:Module already imported:pytest.PytestWarning', 'test_addvisement.py'])、
    #     os.system("allure generate ./result/ -o /gyhlw/output/report/ --clean")
    test_add()
import time

from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_zuhu():
    wd= webdriver.Chrome()
    wd.maximize_window()
    wd.get('http://10.22.33.101:32752/ind_net_fvue/index')
    time.sleep(1)
    try:
        loginelement = wd.find_element(By.XPATH, '//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/span')
    except NoSuchElementException:
        print('没有登录这个元素')
    loginelement.click()
    handles = wd.window_handles
    wd.switch_to.window(handles[1])
    print(wd.current_url)
    wd.find_element(By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/form/div[2]/div/div[1]/input').send_keys(
        'admin')
    wd.find_element(By.XPATH,
                    '//*[@id="app"]/section/section/main/div/div/div/div/form/div[3]/div/div[1]/input').send_keys(
        'Indnet123&')
    wd.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/form/div[4]/button').click()
    time.sleep(3)   #到此登录成功

    #shift+tab批量取消缩进，tab缩进
    e1 =wd.find_element(By.XPATH, '//ul/div[2]/div/span')  #/html/body/div/section/header/div/div[1]/div[2]/ul/div[2]/div/span   点击门户管理
    e2 = e1.get_attribute("aria-controls")
    e1.click()
    time.sleep(5)
    str1 = '//*[@id='
    str2 = ']/li[1]'#1为业务中心2为系统管理3为日志管理
    jsxpath = str1 + '"' + e2 + '"' + str2
    print(jsxpath)
    wd.find_element(By.XPATH, jsxpath).click()
    time.sleep(2)
    print(wd.current_url)
    wd.refresh()
    time.sleep(3)





    wd.close()
    wd.quit()
if __name__ == '__main__':
    test_add_zuhu()
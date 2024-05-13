import time

from selenium import webdriver
from selenium.webdriver.common.by import By
'''测试点击文档跳转'''

def test_document():
    wd = webdriver.Chrome()
    wd.maximize_window()
    wd.get('http://10.22.33.101:32752/ind_net_fvue/index')
    time.sleep(1)
    wd.find_element(By.XPATH,'//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[2]/span').click()
    handles = wd.window_handles
    wd.switch_to.window(handles[1])
    print(wd.current_url)


    wd.quit()
if __name__ == '__main__':

        test_document()
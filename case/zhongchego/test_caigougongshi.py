import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
def test_caigougongshi():
    wd=webdriver.Firefox()
    wd.get("https://test.crrcgo.cc/#/homePage")
    wd.implicitly_wait(30)
    wd.find_element(By.CLASS_NAME,'loginBtn').click()

    time.sleep(2)
    wd.find_element(By.XPATH,'//div/div/div[2]/div[2]/span[2]').click()
    wd.find_element(By.XPATH,'//form[2]/div[1]/input').send_keys("18701473018")
    a=input('请输入验证码:')
    wd.find_element(By.XPATH,'//*[@id="imgCode"]').send_keys(a)
    wd.find_element(By.XPATH,'//div/div/div[2]/div[2]/form[2]/div[4]/div/button').click()
    b=input('请输入短信验证码：')
    wd.find_element(By.XPATH,'//div/div/div[2]/div[2]/form[2]/div[4]/div/input').send_keys(b)
    wd.find_element(By.XPATH,'//div/div/div[2]/div[2]/form[2]/input[4]').click()
    time.sleep(2)
    wd.find_element(By.XPATH,'//div[1]/div/div[1]/div[1]/div[3]/div[2]/div[4]/div/div[1]').click()
    time.sleep(1)
    handles=wd.window_handles
    wd.switch_to(handles[1])
    time.sleep(3)
    wd.find_element(By.XPATH,'//div[2]/div/div[1]/div[1]/div[1]/div[1]/div/i').click()
    wd.find_element(By.XPATH,'//div[2]/div/div[8]/div/div/div[1]/div/div/div[3]/div[3]/div[3]/div[1]/div[1]').click()
    time.sleep(2)
    wd.find_element(By.XPATH,'//div[2]/div/div[1]/div[1]/div[2]/div[1]/ol/li[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/i').click()
    time.sleep(0.5)
    wd.find_elements(By.XPATH,'//ul/li[@class="ovSUTpDn"]')[2].click()
    time.sleep(2)
    wd.find_element()

















if __name__ == '__main__':
    test_caigougongshi()
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def shujudaoru(laiyuanleixing,jici):
    executable_path = "C:\Program Files\Mozilla Firefox\geckodriver.exe"
    wd = webdriver.Firefox(executable_path=executable_path)
    # wd = webdriver.Firefox()
    wd.maximize_window()
    wd.implicitly_wait(30)
    wd.get('http://10.22.33.45:8769/hub/login/cockpit')
    wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[2]/div/div/input').send_keys("caiwu")
    wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[3]/div/div/input').send_keys("123abc")



    a = input("请输入验证码:")
    wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[4]/div/div/input').send_keys(a)

    wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[5]/button').click()
    # print(wd.page_source)
    #如果出现异常，递归
    def yanzhengma(str):

        if str in wd.page_source:
            time.sleep(3)
            wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[4]/div/div/input').clear()
            a=input("请再次输入验证码:")
            wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[4]/div/div/input').send_keys(a)
            wd.find_element(By.XPATH, '//section/section/main/div/div/div/div/form/div[5]/button').click()
            time.sleep(1)
            yanzhengma(str)
        else:
            pass
    yanzhengma("验证码错误")
    time.sleep(2)
    wd.find_element(By.XPATH, '//section/main/section/aside/div/div[2]/ul/li[2]/div').click()
    time.sleep(1)
    wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[2]/ul/li/ul/li[1]').click()
    time.sleep(1)


    for i in range(jici):
        # 点击导入
        wd.find_element(By.XPATH, '//section/main/section/main/div[2]/div/div[1]/form/div[2]/button[3]/span').click()
        time.sleep(1)
        wd.find_element(By.XPATH, '//div/div[2]/form/div[1]/div/div/div[1]/span/span/i').click()
        if laiyuanleixing=="2023年快报":
            file_dir1 = 'D:\国信会视工作文档\需求\数据导入\数据表样 - 副本'  # 真的是历史上一大坑，/不行，非得\才行！
            mypic = '2023快报导出表样.xls'
            file_dir = os.path.join(file_dir1, mypic)
            wd.find_elements(By.XPATH,'//ul/li[1]').pop().click()
            wd.find_element(By.XPATH,'//div/div[2]/form/div[2]/div/div/input').send_keys(f'2023-0{random.randint(1,12)}')
            time.sleep(1)
            wd.find_element(By.XPATH,'//div/div[1]/span[contains(text(),"导入报表")]').click()
            time.sleep(1)
            wd.find_element(By.XPATH,'//div/div[2]/form/div[3]/div/div/div[1]/input').send_keys(file_dir)
            time.sleep(1)
            wd.find_element(By.XPATH,'//span/button[2]/span[contains(text(),"确 定")]').click()
            time.sleep(1)
            wd.find_elements(By.XPATH,'//button[2]/span[contains(text(),"确定")]').pop().click()
            time.sleep(1)
        elif laiyuanleixing=="2023年月报":
            file_dir1 = 'D:\国信会视工作文档\需求\数据导入\数据表样 - 副本'  # 真的是历史上一大坑，/不行，非得\才行！
            mypic = '2023月报导出表样.xls'
            file_dir = os.path.join(file_dir1, mypic)
            wd.find_elements(By.XPATH, '//ul/li[2]').pop().click()
            wd.find_element(By.XPATH, '//div/div[2]/form/div[2]/div/div/input').send_keys(f'2023-0{random.randint(1,5)}')
            wd.find_element(By.XPATH, '//div/div[1]/span[contains(text(),"导入报表")]').click()
            time.sleep(1)
            wd.find_element(By.XPATH, '//div/div[2]/form/div[3]/div/div/div[1]/input').send_keys(file_dir)
            time.sleep(1)
            wd.find_element(By.XPATH, '//span/button[2]/span[contains(text(),"确 定")]').click()
            time.sleep(2)
            wd.find_elements(By.XPATH, '//button[2]/span[contains(text(),"确定")]').pop().click()
            time.sleep(1)
        elif laiyuanleixing=="2023年半年决算":
            file_dir1 = 'D:\国信会视工作文档\需求\数据导入\数据表样 - 副本'  # 真的是历史上一大坑，/不行，非得\才行！
            mypic = '2023年半年报表样.xlsx'
            file_dir = os.path.join(file_dir1, mypic)
            wd.find_elements(By.XPATH, '//ul/li[3]').pop().click()
            wd.find_element(By.XPATH, '//div/div[2]/form/div[2]/div/div/input').send_keys(f'2023-06')
            wd.find_element(By.XPATH, '//div/div[1]/span[contains(text(),"导入报表")]').click()
            time.sleep(1)
            wd.find_element(By.XPATH, '//div/div[2]/form/div[3]/div/div/div[1]/input').send_keys(file_dir)
            time.sleep(1)
            wd.find_element(By.XPATH, '//span/button[2]/span[contains(text(),"确 定")]').click()
            time.sleep(2)
            wd.find_elements(By.XPATH, '//button[2]/span[contains(text(),"确定")]').pop().click()
            time.sleep(1)
        elif laiyuanleixing=="2023年年报":
            wd.find_elements(By.XPATH, '//ul/li[4]').pop().click()
            file_dir1 = 'D:\国信会视工作文档\需求\数据导入\数据表样 - 副本'  # 真的是历史上一大坑，/不行，非得\才行！
            mypic = '2023年年报表样.xlsx'
            file_dir = os.path.join(file_dir1, mypic)
            wd.find_element(By.XPATH, '//div/div[2]/form/div[2]/div/div/input').send_keys(f'2023-12')
            wd.find_element(By.XPATH, '//div/div[1]/span[contains(text(),"导入报表")]').click()
            time.sleep(1)
            wd.find_element(By.XPATH, '//div/div[2]/form/div[3]/div/div/div[1]/input').send_keys(file_dir)
            time.sleep(1)
            wd.find_element(By.XPATH, '//span/button[2]/span[contains(text(),"确 定")]').click()
            time.sleep(2)
            wd.find_elements(By.XPATH, '//button[2]/span[contains(text(),"确定")]').pop().click()
            time.sleep(1)
        elif laiyuanleixing == "2024年快报":
            file_dir1 = 'D:\国信会视工作文档\需求\数据导入\数据表样 - 副本'  # 真的是历史上一大坑，/不行，非得\才行！
            mypic = '2024快报导出表样.xls'
            file_dir = os.path.join(file_dir1, mypic)
            wd.find_elements(By.XPATH, '//ul/li[1]').pop().click()
            wd.find_element(By.XPATH, '//div/div[2]/form/div[2]/div/div/input').send_keys(
                f'2024-0{random.randint(1, 9)}')
            time.sleep(1)
            wd.find_element(By.XPATH, '//div/div[1]/span[contains(text(),"导入报表")]').click()
            time.sleep(1)
            wd.find_element(By.XPATH, '//div/div[2]/form/div[3]/div/div/div[1]/input').send_keys(file_dir)
            time.sleep(1)
            wd.find_element(By.XPATH, '//span/button[2]/span[contains(text(),"确 定")]').click()
            time.sleep(1)
            wd.find_elements(By.XPATH, '//button[2]/span[contains(text(),"确定")]').pop().click()
            time.sleep(1)
        elif laiyuanleixing == "2024年月报":
            file_dir1 = 'D:\国信会视工作文档\需求\数据导入\数据表样 - 副本'  # 真的是历史上一大坑，/不行，非得\才行！
            mypic = '2024月报导出表样.xls'
            file_dir = os.path.join(file_dir1, mypic)
            wd.find_elements(By.XPATH, '//ul/li[2]').pop().click()
            wd.find_element(By.XPATH, '//div/div[2]/form/div[2]/div/div/input').send_keys(
                f'2024-0{random.randint(1, 5)}')
            wd.find_element(By.XPATH, '//div/div[1]/span[contains(text(),"导入报表")]').click()
            time.sleep(1)
            wd.find_element(By.XPATH, '//div/div[2]/form/div[3]/div/div/div[1]/input').send_keys(file_dir)
            time.sleep(1)
            wd.find_element(By.XPATH, '//span/button[2]/span[contains(text(),"确 定")]').click()
            time.sleep(2)
            wd.find_elements(By.XPATH, '//button[2]/span[contains(text(),"确定")]').pop().click()
            time.sleep(1)
    wd.quit()
if __name__ == '__main__':
    shujudaoru("2024年月报",5)
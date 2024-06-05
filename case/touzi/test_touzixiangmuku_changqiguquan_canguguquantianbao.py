import os
import random
import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
def test_canguguquan():
        exe_path="C:\\Program Files\Mozilla Firefox\geckodriver"
        wd = webdriver.Firefox(executable_path=exe_path)
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
            "高腾")
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
                        '//section/main/div/div[2]/div/div[2]/form/div/div/div/div[1]/span/span/i').click()

        wd.find_elements(By.XPATH, '//ul/li[1]/span').pop().click()

        wd.find_element(By.XPATH, '//section/main/div/div[2]/div/div[3]/span/button/span').click()  # 点击确定
        # //*[@id="app"]/section/main/div/div[2]/div/div[3]/span/button
        time.sleep(2)
        # 选择投资项目库
        wd.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div/ul/li[6]').click()
        time.sleep(4)
        if wd.find_element(By.XPATH,'//section/header/div/div/div[1]/div[1]/h3').get_attribute("title")=="李晓霞":
                wd.find_element(By.XPATH,'//section/main/section/aside/div/div/ul/li[4]/div').click()
                time.sleep(0.5)
                wd.find_element(By.XPATH, '//section/main/section/aside/div/div/ul/li[4]/ul/li[1]').click()
        else:
                wd.find_element(By.XPATH, '//section/main/section/aside/div/div/ul/li[3]/div').click()
                time.sleep(0.5)
                wd.find_element(By.XPATH,'//section/main/section/aside/div/div/ul/li[3]/ul/li[1]').click()

        time.sleep(0.5)
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[1]/div[1]/div/div/button[1]/span').click()
        time.sleep(0.5)
        #填报内容
        #wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[1]/div[1]/div/div/div/input').send_keys(f"20{random.randint(0,2)}{random.randint(1,4)}")
        wd.find_element(By.XPATH, '//section/main/section/main/div/div[2]/form/div/div/div[1]/div[1]/div/div/div/input').send_keys("2020")
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[1]/div[2]/div/div/div/div/div/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 4)}]').pop().click()
        #wd.find_elements(By.XPATH, f'//ul/li[2]').pop().click()
        jidu=wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[1]/div[2]/div/div/div/div/div/input').get_attribute("value")
        print(f"选择季度为：{jidu}")
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[1]/div[3]/div/div/div/div/span/span/i').click()
        time.sleep(1)
        aa=wd.find_elements(By.XPATH,'//div[@class="el-scrollbar"]/div/ul').pop().find_elements(By.XPATH,'//li/span')
        newlist=[]
        for zz in aa :
                if zz.text!="":
                        print(zz.text)
                        newlist.append(zz.text)

        print(f"获取到下拉列表的长度为:{len(newlist)}")
        wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,len(newlist))}]').pop().click()

        proj=wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[1]/div[3]/div/div/div/div/input').get_attribute("value")
        print(f"选择项目名称为:{proj}")
        time.sleep(1)
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[2]/div[1]/div/div/div[1]/div/div/span/span/i').click()
        wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,2)}]').pop().click()

        time.sleep(1)
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[2]/div[2]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()
        time.sleep(1)
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[2]/div[3]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()
        #投资主体派出董监事及重要岗位人员数量
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[3]/div[1]/div/div/div[1]/input').send_keys(random.randint(1,99))
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[3]/div[2]/div/div/div[1]/input').send_keys(random.randint(1,99))
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[3]/div[3]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[4]/div[1]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()

        #分类整治方式
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[4]/div[2]/div/div/div/div/div/span/span/i').click()
        wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,4)}]').pop().click()
        #调试，制定特定的值
        #wd.find_elements(By.XPATH, f'//ul/li[4]').pop().click()
        time.sleep(3)
        # bb=wd.find_elements(By.XPATH,'//div[@class="el-scrollbar"]/div/ul').pop().find_elements(By.XPATH,'//li/span')
        #
        # for cc in bb:
        #         print(cc.text)



        dd=wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[4]/div[2]/div/div/div/div/div/input').get_attribute("value")
        print(dd)
        if dd=="继续持有":
                wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[4]/div[3]/div/div/div/textarea').send_keys("test_整治目标")
                wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[5]/div[1]/div/div/div/textarea').send_keys("test_整治措施")
                wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[8]/div[1]/div/div/div/textarea').send_keys("test_工作进展")

        elif dd=="限期整改":
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[4]/div[3]/div/div/div/textarea').send_keys(
                        "test_整治目标")
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[5]/div[1]/div/div/div/textarea').send_keys(
                        "test_整治措施")
                wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[6]/div[1]/div/div/div/input').send_keys(f"202{random.randint(0,4)}-0{random.randint(1,9)}")
                wd.find_element(By.XPATH,
                        '//section/main/section/main/div/div[2]/form/div/div/div[8]/div[1]/div/div/div/textarea').send_keys(
                "test_工作进展")

        elif dd == "清理退出":
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[4]/div[3]/div/div/div/textarea').send_keys(
                        "test_整治目标")
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[5]/div[1]/div/div/div/textarea').send_keys(
                        "test_整治措施")
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[6]/div[1]/div/div/div/input').send_keys(
                        f"202{random.randint(0, 4)}-0{random.randint(1, 9)}")
                wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[6]/div[2]/div/div/div/div/div[1]/span/span/i').click()
                # wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,2)}]').pop().click()
                wd.find_elements(By.XPATH, f'//ul/li[1]').pop().click()
                time.sleep(1)
                ee=wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[6]/div[2]/div/div/div/div/div/input').get_attribute("value")
                print(f"是否退出全部股权为：{ee}")
                if ee=="是":
                        time.sleep(2)
                        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[6]/div[3]/div/div/div/div/div[1]/span/span/i').click()
                        wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,2)}]').pop().click()
                        time.sleep(1)
                        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[7]/div[1]/div/div/div/input').send_keys(random.randint(2000,3000))
                        wd.find_element(By.XPATH,'//section/main/section/main/div/div[2]/form/div/div/div[7]/div[2]/div/div/div/input').send_keys(f"20{random.randint(1,2)}{random.randint(1,4)}-0{random.randint(1,9)}-{random.randint(11,31)}")

                else:
                        wd.find_element(By.XPATH,
                                        '//section/main/section/main/div/div[2]/form/div/div/div[7]/div[2]/div/div/div/input').send_keys(
                                f"20{random.randint(1, 2)}{random.randint(1, 4)}-0{random.randint(1, 9)}-{random.randint(11, 31)}")

                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[8]/div[1]/div/div/div/textarea').send_keys(
                        "test_工作进展")


        elif dd == "有序退出":
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[4]/div[3]/div/div/div/textarea').send_keys(
                        "test_整治目标")
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[5]/div[1]/div/div/div/textarea').send_keys(
                        "test_整治措施")
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[6]/div[1]/div/div/div/input').send_keys(
                        f"202{random.randint(0, 4)}-0{random.randint(1, 9)}")
                time.sleep(1)
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[6]/div[2]/div/div/div/div/div[1]/span/span/i').click()
                # wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 2)}]').pop().click()
                wd.find_elements(By.XPATH, f'//ul/li[1]').pop().click()
                time.sleep(1)
                ee = wd.find_element(By.XPATH,
                                     '//section/main/section/main/div/div[2]/form/div/div/div[6]/div[2]/div/div/div/div/div/input').get_attribute("value")
                if ee == "是":
                        wd.find_element(By.XPATH,
                                        '//section/main/section/main/div/div[2]/form/div/div/div[6]/div[3]/div/div/div/div/div[1]/span/span/i').click()
                        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 2)}]').pop().click()
                        time.sleep(2)
                        wd.find_element(By.XPATH,
                                        '//section/main/section/main/div/div[2]/form/div/div/div[7]/div[1]/div/div/div/input').send_keys(random.randint(2000,3000))
                        wd.find_element(By.XPATH,
                                        '//section/main/section/main/div/div[2]/form/div/div/div[7]/div[2]/div/div/div/input').send_keys(
                                f"20{random.randint(1, 2)}{random.randint(1, 4)}-0{random.randint(1, 9)}-{random.randint(11, 31)}")

                else:
                        wd.find_element(By.XPATH,
                                        '//section/main/section/main/div/div[2]/form/div/div/div[7]/div[2]/div/div/div/input').send_keys(
                                f"20{random.randint(0, 2)}{random.randint(1, 4)}-0{random.randint(1, 9)}-{random.randint(11, 31)}")

                wd.find_element(By.XPATH,
                                '//section/main/section/main/div/div[2]/form/div/div/div[8]/div[1]/div/div/div/textarea').send_keys(
                        "test_工作进展")


        time.sleep(1)
        wd.find_element(By.XPATH, '//section/main/section/main/div/div/div/button[1]/span').click()
        time.sleep(3)
        wd.quit()


if __name__ == '__main__':
        for i in range(1):
                test_canguguquan()




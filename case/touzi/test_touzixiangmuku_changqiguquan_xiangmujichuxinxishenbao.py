import os
import random
import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
def test_jichuxinxi(company,times,main_touzi):
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
        # wd.find_element(By.XPATH,
        #                 '//section/main/div/div[2]/div/div[2]/form/div/div/div/div[1]/span/span/i').click()
        #
        # wd.find_elements(By.XPATH, '//ul/li[1]/span').pop().click()
        #
        # wd.find_element(By.XPATH, '//section/main/div/div[2]/div/div[3]/span/button/span').click()  # 点击确定
        # # //*[@id="app"]/section/main/div/div[2]/div/div[3]/span/button
        # time.sleep(2)
        # 选择投资项目库
        wd.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div/ul/li[6]').click()
        time.sleep(4)
        if wd.find_element(By.XPATH,'//section/header/div/div/div[1]/div[1]/h3').get_attribute("title")=="李晓霞":
                wd.find_element(By.XPATH,'//section/main/section/aside/div/div/ul/li[3]/div').click()
                time.sleep(0.5)
                wd.find_element(By.XPATH, '//section/main/section/aside/div/div/ul/li[3]/ul/li[1]').click()
        else:
                wd.find_element(By.XPATH, '//section/main/section/aside/div/div/ul/li[2]/div').click()
                time.sleep(0.5)
                wd.find_element(By.XPATH,'//section/main/section/aside/div/div/ul/li[2]/ul/li[1]').click()

        time.sleep(0.5)
        wd.find_element(By.XPATH,'//section/main/section/main/div/div[1]/div[1]/div/div/button[1]/span').click()
        time.sleep(0.5)
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[1]/div/div/div/input').send_keys(company)
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[2]/div/div/div/input').send_keys(f"{company}_company")
        #wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[3]/div/div/div/input').send_keys(times)
        #wd.find_element(By.XPATH,'//table[1]/tbody/tr[5]/td[6]/div/span').click()
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[3]/div/div/div/input').send_keys(main_touzi)
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[4]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,2)}]').pop().click()


        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[5]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,7)}]').pop().click()
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[6]/div/div/div/div/div/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,5)}]').pop().click()
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[7]/div/div/div/div/div/span/span/i').click()
        wd.find_elements(By.XPATH, '//ul/li[1]').pop().click()
        wd.find_element(By.XPATH,
                        '//section/main/section/main/div/form/div[1]/div[2]/div/div[8]/div/div/div/input').send_keys(
                times)
        wd.find_element(By.XPATH,
                        '//section/main/section/main/div/form/div[1]/div[2]/div/div[9]/div/div/div/input').send_keys(
                "test_可研文号")
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[10]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()
        time.sleep(1)
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[11]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,20)}]').pop().click()
        wd.find_element(By.XPATH,
                        '//section/main/section/main/div/form/div[1]/div[2]/div/div[12]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()
        wd.find_element(By.XPATH,
                        '//section/main/section/main/div/form/div[1]/div[2]/div/div[13]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,3)}]').pop().click()
        wd.find_element(By.XPATH,
                        '//section/main/section/main/div/form/div[1]/div[2]/div/div[14]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,3)}]').pop().click()
        #我方投资总额
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[15]/div/div/div[1]/input').send_keys("12000")
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[16]/div/div/div[1]/input').send_keys("64.55")
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[17]/div/div/div/textarea').send_keys("大连公司，大同公司，株机公司")
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[19]/div/div/div/textarea').send_keys("12.11,12.22,12.12")
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[20]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[21]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()
        wd.find_element(By.XPATH,
                        '//section/main/section/main/div/form/div[1]/div[2]/div/div[22]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[23]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,2)}]').pop().click()
        '''______________________________________________'''
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/span/span/i').click()
        wd.find_elements(By.XPATH,'//ul/li[2]').pop().click()
        if wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[4]/div/div/div/div/div/input').get_attribute("value") == "境内":
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[2]/div/div/div/input').send_keys(times)
        else:
                pass
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[3]/div/div/div/input').send_keys(times)
        wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[4]/div/div/div/input').send_keys(times)
        wd.find_element(By.XPATH,
                        '//section/main/section/main/div/form/div[2]/div[2]/div/div[5]/div/div/div/div/div/span/span/i').click()
        wd.find_elements(By.XPATH, '//ul/li[5]').pop().click()
        wd.find_element(By.XPATH, '//section/main/section/main/div/form/div[2]/div[2]/div/div[6]/div/div/div/input').send_keys("1000")
        wd.find_element(By.XPATH,
                        '//section/main/section/main/div/form/div[2]/div[2]/div/div[7]/div/div/div/div/div/span/span/i').click()
        if wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[4]/div/div/div/div/div/input').get_attribute("value")=="境内":
                wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1,3)}]').pop().click()
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[9]/div/div/div/div/div[1]/span/span/i').click()
                wd.find_elements(By.XPATH, f'//ul/li[{random.randint(1, 33)}]').pop().click()
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[10]/div/div/div/div/div/span/span/i').click()
                time.sleep(1)
                wd.find_elements(By.XPATH,'//ul/li[1]').pop().click()
                name = wd.find_element(By.XPATH, '//section/header/div/div/div[1]/div[1]/h3').get_attribute("title")
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[11]/div/div/div[1]/input').send_keys(name)
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[12]/div/div/div[1]/input').send_keys("1980000000")

                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[13]/div/div/div/textarea').send_keys("测试经营范围测试经营范围测试经营范围测试"
                                                                                                                                          "经营范围测试经营范围测试经营范围测试经营范围测试经"
                                                                                                                                          "营范围测试经营范围测试经营范围测试经营范围测试经营范围测"
                                                                                                                                          "试经营范围测试经营范围测试经营范围")
        else:
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[7]/div/div/div/div/div[1]/span/span/i').click()
                wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,3)}]').pop().click()
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[8]/div/div/div/div/div[1]/span/span/i').click()
                wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,70)}]').pop().click()
                value1=wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[8]/div/div/div/div/div/input').get_attribute("value")
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[9]/div/div/div/input').send_keys(value1)
                name=wd.find_element(By.XPATH,'//section/header/div/div/div[1]/div[1]/h3').get_attribute("title")
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[10]/div/div/div/input').send_keys(name)
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[11]/div/div/div/input').send_keys("18900000001")
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[2]/div[2]/div/div[12]/div/div/div[1]/textarea').send_keys("test_经营范围")


        #境外相关信息
        if wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[1]/div[2]/div/div[4]/div/div/div/div/div/input').get_attribute("value")=="境外":
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[3]/div[2]/div/div[1]/div/div/div/input').send_keys(times)
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[3]/div[2]/div/div[2]/div/div/div/input').send_keys(times)
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[3]/div[2]/div/div[3]/div/div/div/input').send_keys(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))

                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[3]/div[2]/div/div[4]/div/div/div/input').send_keys(times)

                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[3]/div[2]/div/div[5]/div/div/div/input').send_keys(times)
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[3]/div[2]/div/div[6]/div/div/div/div/div[1]/span/span/i').click()
                wd.find_elements(By.XPATH,f'//ul/li[{random.randint(1,3)}]').pop().click()
                wd.find_element(By.XPATH,'//section/main/section/main/div/form/div[3]/div[2]/div/div[7]/div/div/div/input').send_keys("12345.99")

        else:
                pass
        time.sleep(1)
        wd.find_element(By.XPATH, '//section/main/section/main/div/div/div/button[1]/span').click()
        time.sleep(3)
        wd.quit()


if __name__ == '__main__':
    # strtime = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # projectname = "测试立项备案test_" + strtime

    list3=["株机公司","大连公司","大同公司","戚墅堰公司","长客股份公司","四方股份公司","唐山公司","浦镇公司","四方车辆公司","齐车集团","长江集团","株洲所","永济电机公司","株洲电机公司",]
    list2=["唐山公司","浦镇公司","四方车辆公司","齐车集团","长江集团","株洲所","永济电机公司","株洲电机公司",]
    list=["齐车新能源机械公司-9",]
    for company in list:
            for i in range(3):
                    times="2024-02"
                    #main_touzi=f"中车投资{random.randint(3,1000)}-{i+1}"
                    main_touzi=f"中国中车投资集团-{i+1}"
                    test_jichuxinxi(company,times,main_touzi)
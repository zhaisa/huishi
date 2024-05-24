import random
import time

#import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
def test_add_kaifachanjiaoziyuan(year,bigstyle,style,count):
    exe_path = "C:\\Program Files\Mozilla Firefox\geckodriver"
    wd = webdriver.Firefox(executable_path=exe_path)
    wd.maximize_window()

    wd.get('http://10.22.33.153:31376/gdzbgtt/industryPolicy')
    wd.implicitly_wait(180)
    wd.find_element(By.XPATH,'//section/div/div[1]/div/ul/li[5]').click()
    handles=wd.window_handles
    wd.switch_to.window(handles[1])
    # wd.implicitly_wait(180)
    time.sleep(3)
    wd.find_element(By.XPATH,'//section/section/main/div/div/div/div/form/div[2]/div/div/input').send_keys("GJGDJT001")
    wd.find_element(By.XPATH,'//section/section/main/div/div/div/div/form/div[3]/div/div/input').send_keys("welcome@2024")
    time.sleep(1)
    wd.find_element(By.XPATH,'//section/section/main/div/div/div/div/form/div[4]/button').click()

    wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[6]/div').click()
    wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[6]/ul/li[1]/div').click()
    wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]').click()
    if bigstyle=="需求":
        wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[6]/ul/li/ul/li[1]/ul/li/ul/li[1]/ul/li/div').click()
        if style=="开发产教资源":
            #开发产教资源
            wd.find_element(By.XPATH,'//section/main/section/aside/div/div[2]/ul/li[6]/ul/li/ul/li[1]/ul/li/ul/li[1]/ul/li/ul/li[1]').click()
            #wd.find_element(By.XPATH,'//section/main/section/main/div[2]/div/div/div/div[1]/form/div[2]/button[3]/span').click()
            time.sleep(2)
            for i in range(count):
                wd.find_element(By.XPATH,'//section/main/section/main/div[2]/div/div/div/div[1]/form/div[2]/button[3]/span').click()
                # wd.find_element(By.XPATH,'//section/main/section/main/div[2]/div/div/div[1]/form/div[2]/button[3]').click()
                time.sleep(1)

                wd.find_element(By.XPATH,'//form/div[1]/div[1]/div/div/div/input').send_keys(year)
                time.sleep(1)
                wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()
                time.sleep(1)
                # wd.find_element(By.XPATH,'//form/div[1]/div[2]/div/div/div/div[1]/span/span/i').click()
                # wd.find_elements(By.XPATH,f'//ul/li[{style}]').pop().click()
                #获取所有类型，选择一个类型填报
                wd.find_element(By.XPATH,'//form/div[1]/div[2]/div/div/div/div/span/span/i').click()
                aa = wd.find_elements(By.XPATH, '//div[@class="el-scrollbar"]/div/ul').pop().find_elements(By.XPATH,'//li/span')
                newlist = []
                for zz in aa:
                    if zz.text != "":
                        print(zz.text)
                        newlist.append(zz.text)

                print(f"获取到下拉列表的长度为:{len(newlist)}")
                if i<len(newlist):
                    wd.find_elements(By.XPATH, f'//ul/li[{i+1}]').pop().click()
                elif i==len(newlist):
                    wd.find_elements(By.XPATH, f'//ul/li[{i}]').pop().click()
                elif i>len(newlist) and i<len(newlist)**2:
                    wd.find_elements(By.XPATH,f'//ul/li[{i//len(newlist)}]')
                else:
                    pass
                proj = wd.find_element(By.XPATH,'//form/div[1]/div[2]/div/div/div/div/input').get_attribute("value")
                print(f"选择项目类型为:{proj}")
                wd.find_element(By.XPATH,'//form/div[2]/div[1]/div/div/div/input').send_keys(f"{proj}_{i}")
                wd.find_element(By.XPATH,'//form/div[2]/div[2]/div/div/div/textarea').send_keys("1.颗粒化专业教学资源建设2.标准化课程、"
                                                                                                "专创融合课程、社会培训课程建设3.虚拟仿真"
                                                                                                "资源建设建设4.典型实训项目建设")

                wd.find_element(By.XPATH,'//form/div[2]/div[3]/div/div/div[1]/textarea').send_keys("test_工作成果")

                #wd.find_element(By.XPATH,'//form/div[3]/div[1]/div/div/div/div[1]/input').send_keys("西南交通大学")
                # wd.find_elements(By.XPATH,'//ul/li[2]').pop().click()
                # mouse_click=ActionChains(wd)
                # mouse_click.move_to_element()
                wd.find_element(By.XPATH,'//form/div[3]/div[1]/div/div/div/div[2]/span/span/i').click()
                wd.find_elements(By.XPATH,'//ul/li[2]').pop().click()

                time.sleep(0.5)
                wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()
                #协同单位
                # wd.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/div[1]/input').send_keys("中车长春轨道客车股份有限公司")
                # wd.find_elements(By.XPATH,'//ul/li[45]').pop().click()
                wd.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/div[2]/span/span/i').click()
                wd.find_elements(By.XPATH, '//ul/li[45]').pop().click()
                time.sleep(0.5)
                wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()

                wd.find_element(By.XPATH,'//form/div[3]/div[3]/div/div/div/input').send_keys(f"2024-0{random.randint(1,9)}")
                time.sleep(0.5)
                wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()
                time.sleep(1)
                wd.find_element(By.XPATH,'//div/div[3]/span/button[2]').click()
                time.sleep(3)
        elif style=="师生研修实践":
            wd.find_element(By.XPATH,
                            '//section/main/section/aside/div/div[2]/ul/li[6]/ul/li/ul/li[1]/ul/li/ul/li[1]/ul/li/ul/li[2]').click()
            time.sleep(2)
            for i in range(count):
                wd.find_element(By.XPATH,'//section/main/section/main/div[2]/div/div/div/div[1]/form/div[2]/button[3]').click()
                time.sleep(1)
                wd.find_element(By.XPATH, '//form/div[1]/div[1]/div/div/div/input').send_keys(year)
                time.sleep(1)
                wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()
                time.sleep(1)
                # 获取所有类型，选择一个类型填报
                wd.find_element(By.XPATH, '//form/div[1]/div[2]/div/div/div/div/span/span/i').click()
                aa = wd.find_elements(By.XPATH, '//div[@class="el-scrollbar"]/div/ul').pop().find_elements(By.XPATH,
                                                                                                           '//li/span')
                newlist = []
                for zz in aa:
                    if zz.text != "":
                        print(zz.text)
                        newlist.append(zz.text)

                print(f"获取到下拉列表的长度为:{len(newlist)}")
                if i < len(newlist):
                    wd.find_elements(By.XPATH, f'//ul/li[{i + 1}]').pop().click()
                elif i == len(newlist):
                    wd.find_elements(By.XPATH, f'//ul/li[{i}]').pop().click()
                elif i > len(newlist) and i < len(newlist) ** 2:
                    wd.find_elements(By.XPATH, f'//ul/li[{i // len(newlist)}]')
                else:
                    pass
                proj = wd.find_element(By.XPATH, '//form/div[1]/div[2]/div/div/div/div/input').get_attribute("value")
                print(f"选择项目类型为:{proj}")
                wd.find_element(By.XPATH,'//form/div[2]/div[1]/div/div/div[1]/input').send_keys("西南交通大学")

                wd.find_element(By.XPATH,'//form/div[2]/div[2]/div/div/div/textarea').send_keys("test_实训专业/技能说明")
                wd.find_element(By.XPATH,'//form/div[3]/div[1]/div/div/div/input').send_keys(random.randint(1,99))
                wd.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/div[2]/span/span/i').click()
                time.sleep(1)
                wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()
                wd.find_element(By.XPATH,'//form/div[4]/div[1]/div/div/div/textarea').send_keys("test_相关说明")
                wd.find_element(By.XPATH,'//form/div[5]/div/div/div/div/textarea').send_keys("test_备注")
                wd.find_element(By.XPATH,'//div/div[3]/span/button[2]/span').click()
                time.sleep(2)

        elif style=="创新中心与项目实施":
            wd.find_element(By.XPATH,
                            '//section/main/section/aside/div/div[2]/ul/li[6]/ul/li/ul/li[1]/ul/li/ul/li[1]/ul/li/ul/li[3]').click()
            time.sleep(2)
            for i in range(count):
                wd.find_element(By.XPATH,
                                '//section/main/section/main/div[2]/div/div/div/div[1]/form/div[2]/button[3]').click()
                time.sleep(1)
                wd.find_elements(By.XPATH, '//form/div[1]/div[1]/div/div/div/input').pop().send_keys(year)
                time.sleep(1)
                wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()
                time.sleep(1)
                # 获取所有类型，选择一个类型填报
                wd.find_element(By.XPATH, '//form/div[1]/div[2]/div/div/div/div/span/span/i').click()
                aa = wd.find_elements(By.XPATH, '//div[@class="el-scrollbar"]/div/ul').pop().find_elements(By.XPATH,
                                                                                                           '//li/span')
                newlist = []
                for zz in aa:
                    if zz.text != "":
                        print(zz.text)
                        newlist.append(zz.text)

                print(f"获取到下拉列表的长度为:{len(newlist)}")
                if i < len(newlist):
                    wd.find_elements(By.XPATH, f'//ul/li[{i + 1}]').pop().click()
                elif i == len(newlist):
                    wd.find_elements(By.XPATH, f'//ul/li[{i}]').pop().click()
                elif i > len(newlist) and i < len(newlist) ** 2:
                    wd.find_elements(By.XPATH, f'//ul/li[{i // len(newlist)}]')
                else:
                    pass
                proj = wd.find_element(By.XPATH, '//form/div[1]/div[2]/div/div/div/div/input').get_attribute("value")
                print(f"选择项目类型为:{proj}")
                if proj=="共同体企业单位参与配合的项目":
                    wd.find_element(By.XPATH, '//form/div[2]/div[1]/div/div/div/div[1]/input').send_keys("西南交通大学")

                    wd.find_element(By.XPATH, '//form/div[2]/div[2]/div/div/div/div[1]/textarea').send_keys("test_项目简介")
                    # wd.find_element(By.XPATH, '//form/div[3]/div[1]/div/div/div/input').send_keys(random.randint(1, 99))
                    # wd.find_element(By.XPATH, '//form/div[3]/div[2]/div/div/div/div[2]/span/span/i').click()
                    # time.sleep(1)
                    # wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()
                    wd.find_element(By.XPATH, '//form/div[2]/div[3]/div/div/div/div[1]/textarea').send_keys("test_需求说明")
                    wd.find_element(By.XPATH, '//form/div[3]/div[1]/div/div/div/input').send_keys("刘立国")
                    wd.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/input').send_keys("010-8888888")
                    wd.find_elements(By.XPATH, '//div/div[3]/span/button[2]/span').pop().click()
                    time.sleep(2)
                else:
                    wd.find_element(By.XPATH,'//form/div[2]/div[1]/div/div/div[1]/input').send_keys("西南技术创新中心")
                    wd.find_element(By.XPATH,'//form/div[2]/div[2]/div/div/div/input').send_keys("10000")
                    wd.find_element(By.XPATH,'//form/div[2]/div[3]/div/div/div/textarea').send_keys("test_工作成果")
                    wd.find_element(By.XPATH,'//form/div[3]/div[1]/div/div/div/div[2]/span/span/i').click()
                    wd.find_elements(By.XPATH,'//ul/li[2]').pop().click()
                    time.sleep(1)
                    wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()
                    wd.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/div[2]/span/span/i').click()
                    wd.find_elements(By.XPATH,'//ul/li[45]').pop().click()
                    time.sleep(1)
                    wd.find_elements(By.XPATH, '//div[@class="el-dialog__header"]').pop().click()
                    time.sleep(1)
                    wd.find_element(By.XPATH,'//div/div[3]/span/button[2]').click()
                    time.sleep(2)

    elif bigstyle=="供给":
        wd.find_element(By.XPATH,
                        '//section/main/section/aside/div/div[2]/ul/li[6]/ul/li/ul/li[1]/ul/li/ul/li[2]/ul/li/div').click()
        if style=="毕业生与技术服务":
            pass
        elif style=="专业师资供给":
            pass

    elif bigstyle=="成果":

        wd.find_element(By.XPATH,
                        '//section/main/section/aside/div/div[2]/ul/li[6]/ul/li/ul/li[1]/ul/li/ul/li[3]/ul/li/div').click()
        if style=="联合人才培养成果":
            pass

        elif style=="协同创新成果":
            pass
        elif style=="支持保障措施":
            pass
        elif style=="教学资源库及精品课程":
            pass

    time.sleep(2)
    wd.quit()


if __name__ == '__main__':
    for i in range(1):
        #strtime = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        #projectname = f"《铁道机车运用与维护专业教学资源库_{strtime}》"
        test_add_kaifachanjiaoziyuan(year="2024")
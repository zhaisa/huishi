import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_add_gonggao():
    wd= webdriver.Chrome()
    wd.maximize_window()
    wd.get('http://10.22.33.101:32752/ind_net_fvue/index')
    time.sleep(1)
    wd.implicitly_wait(30)
    try:
        loginelement = wd.find_element(By.XPATH, '//*[@id="app"]/section/div/div[1]/div/ul/div[2]/li[4]/div/span')
        #//*[@id="app"]/section/section/main/div/div/div/div/form/div[4]/button
    except NoSuchElementException:
        print('没有登录这个元素')
    loginelement.click()
    # handles = wd.window_handles
    # wd.switch_to.window(handles[1])
    # print(wd.current_url)
    wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[2]/div/div/input').send_keys('admin')
    wd.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/form/div[3]/div/div[1]/input').send_keys('Indnet123&')
    wd.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/form/div[4]/button').click()#//*[@id="app"]/section/section/main/div/div/div/div/form/div[4]/button
    time.sleep(3)   #到此登录成功
    # shift+tab批量取消缩进，tab缩进
    e1 = wd.find_element(By.XPATH,'//ul/div[2]/div/span')  # /html/body/div/section/header/div/div[1]/div[2]/ul/div[2]/div/span   点击门户管理
    e2 = e1.get_attribute("aria-controls")
    e1.click()
    time.sleep(5)
    str1 = '//*[@id='
    str2 = ']/li[1]'  # 1为业务中心2为系统管理3为日志管理
    jsxpath = str1 + '"' + e2 + '"' + str2
    print(jsxpath)
    wd.find_element(By.XPATH, jsxpath).click()
    time.sleep(2)
    print(wd.current_url)
    #wd.refresh()
    time.sleep(3)
    wd.find_element(By.XPATH,'//*[@id="app"]/section/main/section/aside/div/div[2]/ul/li[2]/div').click()#点击工作台配置
    time.sleep(2)
    wd.find_element(By.XPATH,'//*[@id="app"]/section/main/section/aside/div/div[2]/ul/li[2]/ul/li[1]').click() #点击公告管理
    time.sleep(2)
    wd.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/div/div[2]/div[1]/form/div[2]/div/button[3]').click()#点击新增按钮
    time.sleep(3)
    #定位打开页面
    #使用jquery来定位该动态元素，通过chrome的consle调试定位到具体位置，.代表类，#代表id

    input_js='$(".el-input__inner")[4].value="test_ceshi_004"'
    wd.execute_script(input_js)

    time.sleep(2)
    wd.find_element(By.XPATH,'//form/div[2]/div/div/div[1]/input').click()
    time.sleep(2)
    wd.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
    time.sleep(2)
    #//*[@id="ueditor_1"]
    # input_js1='$("p.view").value="test_ceshi_004"'
    # wd.execute_script(input_js1) //*[@id="ueditor_1"]
    #wd.switch_to.frame(wd.find_element(By.XPATH,'//*[@id="ueditor_1"]'))
    #动态获取id
    # input_js1='document.getElementsByTagName("iframe")[7].getAttribute("id")'
    # id=wd.execute_script(input_js1)

    list1=wd.find_elements(By.TAG_NAME,'iframe')
    idlist=[]
    global id

    for id1 in list1:
        idstr=id1.get_attribute("id")
        idlist.append(idstr)
    for id2 in idlist:
        if len(id2)!=0:
            id=id2
    time.sleep(3)
    print(f"获取到的iframe的id为 {id}")
    wd.switch_to.frame(id)
    wd.find_element(By.XPATH,'/html/body/p').send_keys("test_ceshi_004")
    time.sleep(1)

    #wd.switch_to.active_element,没有光标的时候使用，
    #wd.switch_to.parent_frame()
    wd.switch_to.default_content()
    time.sleep(1)
    wd.get_window_position()
    time.sleep(2)

    wd.find_element(By.XPATH,'//div[@aria-label="新增"]/div[@class="el-dialog__footer"]/span/button[2]').click()



    time.sleep(2)
    wd.close()
    wd.quit()
if __name__ == '__main__':
    test_add_gonggao()

import sys
from typing import TypeVar

sys.path.append('../')
import os, time
import requests

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from public.common import ErrorExcep, logger
from config.pathconf import WIN_CHROMEDRIVER, LUINX_CHROMEDRIVER, MAC_CHROMEDRIVER
from config.pathconf import WIN_FIREFOXDRIVER, LUINX_FIREFOXDRIVER, MAC_FIREFOXDRIVER
from config.pathconf import IE_PATH
from config.pathconf import LOG_DIR
from config.setting import URL, BROWSERNAME, HUB_HOST, IS_COLONY
from config.setting import PLATFORM, IOS_CAPA, ANDROID_CAPA, APIUMHOST

DAY = time.strftime("%Y-%m-%d", time.localtime(time.time()))

T = TypeVar('T')  # 可以是任何类型。


def if_linux_firefox() -> bool:
    """
    当系统是 luinx 和火狐流量浏览器时 需要做特殊处理
    :browsername 浏览器名称
    :return:
    """
    # 如果不是集群 并且linx firfo
    if IS_COLONY == False and sys.platform.lower() == 'linux' and BROWSERNAME.lower() == 'firefox':

        return True

    else:
        return False


class AppInit:
    """
    初始化APP连接信息类
    """

    def __init__(self):
        self.appos = PLATFORM.lower()

    def decide_appos(self) -> str:  # 判断移动系统选择参数

        if self.appos == 'ios':
            return IOS_CAPA

        elif self.appos == 'android':
            return ANDROID_CAPA
        else:
            logger.error('不支持此移动系统！')
            raise ErrorExcep("不支持此移动系统!!!!")

    # def setup(self) -> T:
    #     try:
    #         from appium import webdriver
    #         decide = self.decide_appos()
    #         return webdriver.Remote("http://" + APIUMHOST + "/wd/hub", decide)
    #
    #     except Exception as e:
    #         logger.error(f'初始app失败 {e}')
    #         raise ErrorExcep("初始app失败!!!!")


class WebInit:
    """
    返回浏览器驱动
    """

    def __init__(self):
        self.browser = BROWSERNAME.lower()
        self.baseurl = URL

    def inspect_url_code(self, url: str) -> bool:
        """
        判断url 地址正常请求
        """
        try:
            rep = requests.get(url, timeout=5)  # 默认设置5秒超时
            code = rep.status_code
            if code == 200:
                return True
            else:
                return False
        except Exception as e:
            logger.error(f'请求地址异常{e}！！')

    @property
    def url(self) -> str:
        return self.baseurl

    @url.setter
    def url(self, value: str) -> str:
        self.baseurl = value

    @property
    def linux_firefox_args(self) -> T:
        """
        linux os firefox browser parameter  只能在 linux 调试
        :return:
        """
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1200x600')
        return options

    @property
    def linux_chrome_args(self) -> T:
        """
        linux os chrome browser parameter
        :return:
        """
        option = webdriver.ChromeOptions()
        option.add_argument('--no-sandbox')  # 取消沙盒模式
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        option.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
        return option

    @property
    def enable(self) -> T:
        """
        如果是 IS_COLONY 开启  启用集群 否则 启用模式
        :return:
        """
        if IS_COLONY:
            return self.setups()
        else:
            return self.setup()

    def browaer_setup_args(self, driver: T) -> T:
        """
        单机浏览器参数设置
        :param driver: driver驱动浏览器
        :return:
        """
        driver.maximize_window()
        driver.get(self.url)
        return driver

    def browaer_setups_args(self, descap: str, option=None) -> T:
        """
        集群浏览器参数设置
        :param descap:启动参数
        :param option:浏览器参数参数
        :return:
        """
        driver = webdriver.Remote(command_executor='http://' + HUB_HOST + '/wd/hub',
                                  desired_capabilities=descap, options=option)
        driver.maximize_window()
        driver.get(self.url)
        return driver

    def setup(self) -> T:
        """
        设置单机版 浏览器驱动
        :return:
        """
        # 判断当前系统
        try:
            if self.inspect_url_code(self.url):  # 如果项目地址正常
                current_sys = sys.platform.lower()
                log_path = os.path.join(LOG_DIR, f'{DAY}firefox.log')

                if current_sys == 'linux':  # linux系统

                    if self.browser == 'chrome':  # 谷歌浏览器
                        option = self.linux_chrome_args
                        driver = webdriver.Chrome(executable_path=LUINX_CHROMEDRIVER, options=option)
                        return self.browaer_setup_args(driver)

                    elif self.browser == 'firefox':  # 火狐浏览器
                        options = self.linux_firefox_args
                        driver = webdriver.Firefox(executable_path=LUINX_FIREFOXDRIVER, options=options,
                                                   service_log_path=log_path)
                        drivers = self.browaer_setup_args(driver)
                        return drivers  # 在linux下启用 火狐浏览器需要借助Display

                    else:
                        logger.error(f'linux系统不支持此浏览器: {self.browser}')
                        return False

                elif current_sys == 'darwin':  # mac 系统

                    if self.browser == 'chrome':
                        driver = webdriver.Chrome(executable_path=MAC_CHROMEDRIVER)
                        return self.browaer_setup_args(driver)

                    elif self.browser == 'firefox':
                        driver = webdriver.Firefox(executable_path=MAC_FIREFOXDRIVER, service_log_path=log_path)
                        return self.browaer_setup_args(driver)

                    elif self.browser == 'safari':
                        driver = webdriver.Safari()
                        return self.browaer_setup_args(driver)

                    else:
                        logger.error(f'mac系统不支持此浏览器: {self.browser}')
                        return False
                elif current_sys == 'win32':

                    if self.browser == 'ie':
                        logger.warning('请确保当前服务器安装IE!')
                        driver = webdriver.Ie(executable_path=IE_PATH)
                        return self.browaer_setup_args(driver)

                    if self.browser == 'chrome':
                        driver = webdriver.Chrome(executable_path=WIN_CHROMEDRIVER)
                        return self.browaer_setup_args(driver)

                    elif self.browser == 'firefox':
                        driver = webdriver.Firefox(executable_path=WIN_FIREFOXDRIVER, service_log_path=log_path)

                        return self.browaer_setup_args(driver, )

                    else:
                        logger.error(f'windos系统不支持此浏览器: {self.browser}')

                        return False
                else:
                    logger.error(f'当前{current_sys}系统不支持！')
                    return False
            else:
                logger.error('项目地址地址请求异常！！！')
                return False

        except Exception as e:
            logger.error(f'浏览器驱动启动失败 {e}')
            return False

    def setups(self) -> T:
        """
        设置集群 浏览器驱动
        :return:
        """
        current_sys = sys.platform.lower()
        try:
            if self.inspect_url_code(self.url) and self.inspect_url_code('http://' + HUB_HOST):  # 项目地址和 集群地址是不是通的
                if current_sys == 'linux':  # linux系统
                    if self.browser == 'chrome':
                        option = self.linux_chrome_args
                        descap = DesiredCapabilities.CHROME
                        return self.browaer_setups_args(descap, option=option)

                    elif self.browser == 'firefox':
                        options = self.linux_firefox_args
                        descap = DesiredCapabilities.FIREFOX
                        return self.browaer_setups_args(descap, option=options)
                    else:
                        logger.error('linux不支持此浏览器')
                        return False

                elif current_sys == 'darwin':  # mac 系统
                    if self.browser == 'safari':
                        descap = DesiredCapabilities.SAFARI
                        return self.browaer_setups_args(descap)

                    elif self.browser == 'chrome':
                        descap = DesiredCapabilities.CHROME
                        return self.browaer_setups_args(descap)

                    elif self.browser == 'firefox':
                        descap = DesiredCapabilities.FIREFOX
                        return self.browaer_setups_args(descap)

                    else:
                        logger.error('mac不支持此浏览器')
                        return False

                elif current_sys == 'win32':
                    if self.browser == 'ie':
                        descap = DesiredCapabilities.INTERNETEXPLORER
                        return self.browaer_setups_args(descap)

                    if self.browser == 'chrome':
                        descap = DesiredCapabilities.CHROME
                        return self.browaer_setups_args(descap)

                    elif self.browser == 'firefox':
                        descap = DesiredCapabilities.FIREFOX
                        return self.browaer_setups_args(descap)

                    else:
                        logger.error('windos不支持此浏览器')
                        return False

                else:
                    logger.info(f'当前{current_sys}系统不支持！')
                    return False

            else:
                logger.error('项目地址或者集群地址请求异常！！！')
                return False

        except Exception as e:
            logger.error(f'浏览器驱动启动失败 {e}')
            return False

from selenium import webdriver
import pytest
import os

driver=None
@pytest.fixture(scope='session',autouse=True)
def wd():
    global driver
    if driver is None:
        exe_path = "C:\\Program Files\Mozilla Firefox\geckodriver"
        driver = webdriver.Firefox(executable_path=exe_path)
        driver
    return driver
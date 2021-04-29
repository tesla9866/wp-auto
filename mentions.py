from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def mentionspi(driver,p):
    inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@data-tab="6"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    if(p==0):
        input_box.send_keys("This command is only applicable in groups\n"+Keys.ENTER)
        return

    peoples = p-1
    for i in range(peoples):
        temp1 = i
        input_box.send_keys('*|=>* @')
        for _ in range(i):
            input_box.send_keys(Keys.ARROW_DOWN)
        input_box.send_keys(Keys.ENTER)
        input_box.send_keys(Keys.SHIFT+Keys.ENTER)
    #input_box.send_keys('*|=>* @' + Keys.ARROW_DOWN+Keys.ENTER)
    #input_box.send_keys(Keys.SHIFT+Keys.ENTER)
    input_box.send_keys(Keys.ENTER)
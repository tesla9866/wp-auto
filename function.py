from selenium.webdriver.common.keys import Keys
import random
from time import sleep
#namz = {'GSI': 'singh', 'GR': 'raj','GM':'mishra','GSH':'shah','GAD':'advik','GAI':'aishnee'}
def catalog(driver):
    inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@data-tab="6"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    input_box.send_keys("*~~~~~~~~~~~~~~~~~~~~*")
    input_box.send_keys(Keys.SHIFT+Keys.ENTER)
    input_box.send_keys("⚙️ *mention all user->*  ```!/Mention```")
    input_box.send_keys(Keys.SHIFT+Keys.ENTER)
    input_box.send_keys("⚙️ *Gaali :)->*  ```!/gaali```")
    input_box.send_keys(Keys.SHIFT+Keys.ENTER)
    input_box.send_keys("⚙️ *Group description ->*  ```!/description```")
    input_box.send_keys(Keys.SHIFT+Keys.ENTER)
    input_box.send_keys("⚙️ *Gaali with mention ->*  ```!/gaali Surname(for adityas)```")
    input_box.send_keys(Keys.SHIFT+Keys.ENTER)
    input_box.send_keys(Keys.ENTER)

def gaali(driver):
    gaalis = ['Bhosdike', 'Madarchod','Bhen Ke laude','Macchar ki jhat','Bawli gaand','Betichod','Fuckoff']
    x = random.randrange(7)
    inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@data-tab="6"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    input_box.send_keys(gaalis[x])
    input_box.send_keys(Keys.ENTER)

def Lgaali(driver):
    gaalis = ['BC', 'MC','BKL','BSDK','FUCK OFF','Go to hell']
    x = random.randrange(5)
    return gaalis[x]

def Sgaali(driver):
    gaalis = ['Bhosdike', 'Madarchod','Bhen Ke laude','Macchar ki jhat','Bawli gaand','Betichod']
    x = random.randrange(6)
    return gaalis[x]

def addimg(driver):
    print()
    #//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[3]/button -> document 
    # //*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button -> image

def descriptionp(driver,desx):
    inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@data-tab="6"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    input_box.send_keys(desx)
    input_box.send_keys(Keys.ENTER)

def mentiongaali(driver,name):
    inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@data-tab="6"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    namz = {'GSI': '@singh', 'GR': '@raj','GM':'@mishra','GSH':'@shah','GAD':'@advik','GAI':'@aishnee'}
    input_box.send_keys(namz[name])
    input_box.send_keys(Keys.ENTER)
    input_box.send_keys(Sgaali(driver))
    input_box.send_keys(Keys.ENTER)

def mentionLgaali(driver,name):
    inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@data-tab="6"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    namz = {'LGSI': '@singh', 'LGR': '@raj','LGM':'@mishra','LGSH':'@shah','LGAD':'@advik','LGAI':'@aishnee'}
    input_box.send_keys(namz[name])
    sleep(0.2)
    input_box.send_keys(Keys.ENTER)
    input_box.send_keys(Lgaali(driver))
    input_box.send_keys(Keys.ENTER)
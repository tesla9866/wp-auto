from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from mentions import mentionspi
from cleaner import cleanup,cleanhead
from search import calling
from functioncaller import funx
#from gui import contactname

#contact = contactname()
#print(contact)
#contact = 'Get Ignited'
def mainfunx(contact):
    path = "C:/webdrivers/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get('http://web.whatsapp.com')

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "app")))
    sleep(8)
    driver.find_element_by_xpath('//*[@title="'+contact+'"]').click()
    driver.find_element_by_xpath('//*[@id="main"]/header/div[2]').click()



    # //*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[1]/div/div/div[1]/span
    no = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[1]/div/div/div[1]/span').text
    x = no.split()
    print("no. of participants-> ",x)
    if(x == []):
        x = [7]
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[2]/div[2]/div/div/div/span[2]').click()
    desx = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[2]/div[2]/div/div/div/span').text
    while(True):
        sleep(0.5)
        cleanup(driver)
        cleanhead(driver)
        sleep(0.5)
        inpt = calling(driver)
        funx(inpt,driver,x[0],desx)

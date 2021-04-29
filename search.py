from selenium import webdriver
from cleaner import cleanhead

def calling(driver):
    while(True):
        try:
            driver.find_elements_by_xpath("//*[contains(text(), '!/Mention')]")
            azz = driver.find_elements_by_xpath("//*[contains(text(), '!/Mention')]")
            if(azz != []):
                return 'M'
        except:
            print()
        try:
            driver.find_elements_by_xpath("//*[contains(text(), '!/catalog')]")
            azz1 = driver.find_elements_by_xpath("//*[contains(text(), '!/catalog')]")
            if(azz1 != []):
                return 'C'
        except:
            print()

        try:
            aer1 = driver.find_elements_by_xpath("//*[contains(text(), 'madarchod bot')]")
            if(aer1!=[]):  
                return 'Hr' 
        except:
            print()
        try:
            aer2 = driver.find_elements_by_xpath("//*[contains(text(), '!/description')]")
            if(aer2!=[]):  
                return 'D' 
        except:
            print()
        try:
            aer3 = driver.find_elements_by_xpath("//*[contains(text(), '!/sgaali singh')]")
            aer4 = driver.find_elements_by_xpath("//*[contains(text(), '!/sgaali raj')]")
            aer5 = driver.find_elements_by_xpath("//*[contains(text(), '!/sgaali mishra')]")
            aer6 = driver.find_elements_by_xpath("//*[contains(text(), '!/sgaali shah')]")
            aer7 = driver.find_elements_by_xpath("//*[contains(text(), '!/sgaali advik')]")
            aer8 = driver.find_elements_by_xpath("//*[contains(text(), '!/sgaali aishnee')]")
            if(aer3!=[]): 
                return 'GSI'
            if(aer4!=[]): 
                return 'GR'
            if(aer5!=[]): 
                return 'GM'
            if(aer6!=[]): 
                return 'GSH'
            if(aer7!=[]): 
                return 'GAD'
            if(aer8!=[]): 
                return 'GAI'
        except:
            print()

        try:
            aerp3 = driver.find_elements_by_xpath("//*[contains(text(), '!/litegaali singh')]")
            aerp4 = driver.find_elements_by_xpath("//*[contains(text(), '!/litegaali raj')]")
            aerp5 = driver.find_elements_by_xpath("//*[contains(text(), '!/litegaali mishra')]")
            aerp6 = driver.find_elements_by_xpath("//*[contains(text(), '!/litegaali shah')]")
            aerp7 = driver.find_elements_by_xpath("//*[contains(text(), '!/litegaali advik')]")
            aerp8 = driver.find_elements_by_xpath("//*[contains(text(), '!/litegaali aishnee')]")
            if(aerp3!=[]): 
                return 'LGSI'
            if(aerp4!=[]): 
                return 'LGR'
            if(aerp5!=[]): 
                return 'LGM'
            if(aerp6!=[]): 
                return 'LGSH'
            if(aerp7!=[]): 
                return 'LGAD'
            if(aerp8!=[]): 
                return 'LGAI'
        except:
            print()
        try:
            aer = driver.find_elements_by_xpath("//*[contains(text(), '!/gaali')]")
            if(aer!=[]):
                return 'G'
            """outerhtml = aer.get_attribute('innerText')
            return outerhtml"""
        except:
            print()
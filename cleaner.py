#from selenium.webdriver.common.keys import Keys

def cleanup(driver):
    for _ in range(50):
        try:
            print("YESSSSSS")
            driver.execute_script("""
            var l = document.getElementsByClassName("_3-8er selectable-text copyable-text")[0];
            l.parentNode.removeChild(l);""")
        except:
            print("cleaned")
            break
        try:
            driver.execute_script("""
            var l = document.getElementsByClassName("_2mGGI")[0];
            l.parentNode.removeChild(l);""")
        except:
            print("Cld")
        

def cleanhead(driver):
    for _ in range(10):
        try:
            driver.execute_script("""
                var l = document.getElementsByClassName("_1DB2K")[0];
                l.parentNode.removeChild(l);""")
            driver.execute_script("""
                var l = document.getElementsByClassName("_1SjZ2")[0];
                l.parentNode.removeChild(l);""")
            print("removing")
        except:
            print()
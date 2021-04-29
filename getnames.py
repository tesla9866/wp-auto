
def getname(driver):
    pnames = []
    val = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[4]/div/div[6]/div/div/div[2]/div[1]/div[1]/span/span').text
    pnames.append(val)
    driver.execute_script("""
    var l = document.getElementsByXpath("//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[4]/div/div[6]/div/div/div[2]/div[1]/div[1]/span/span")[0];
    l.parentNode.removeChild(l);""")
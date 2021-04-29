from mentions import mentionspi
import function

def funx(val,driver,p,desx):
    if(val == 'M'):
        mentionspi(driver,p)
        return
    if(val == 'C'):
        function.catalog(driver)
    if(val == '!\quote'):
        print("Gotaaaaaaaaaaaaaaaaa///")
    if(val == 'G'):
        function.gaali(driver)
    if(val == 'Hr'):
        print()
    if(val=='D'):
        function.descriptionp(driver,desx)
    if(val == 'GSI'or val =='GR' or val == 'GM' or val == 'GAD' or val=='GAI' or val =='GSH'):
        function.mentiongaali(driver,val)
    if(val == 'LGSI'or val =='LGR' or val == 'LGM' or val == 'LGAD' or val=='LGAI' or val =='LGSH'):
        function.mentionLgaali(driver,val)

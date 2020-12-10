import datetime

def takescreenshot(driver)
    dttime = str(datetime.datetime.now()).replace("-","_").replace(" ","_").replace(":","_").split(".")[0]
    print(dttime)
    driver.save_screenshot("screenshot"+dttime+".png")
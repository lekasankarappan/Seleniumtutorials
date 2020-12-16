import datetime

def takescreenshot(driver):
    dttime = str(datetime.datetime.now()).replace("-","_").replace(" ","_").replace(":","_").split(".")[0]
    print(dttime)
    driver.save_screenshot("screenshot"+dttime+".png")

def acceptAlert(driver):
    alt = driver._switch_to.alert
    print("Alert text:", alt.text)
    alt.accept()

def dismissAlert(driver):
    alt = driver._switch_to.alert
    print("Alert text:", alt.text)
    alt.dismiss()

def acceptAlertandsendkeys(driver,value):
    alt = driver._switch_to.alert
    print("Alert title:", alt.text)
    alt.send_keys(value)
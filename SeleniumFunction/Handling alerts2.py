
# this program about switch to alert(),.accept(),.dismiss()
# another test website https://the-internet.herokuapp.com/
from selenium.webdriver.common.keys import Keys
from Launch import browerlaunch as bl
from SeleniumFunction import Generic as gs
import time
bl.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
bl.driver.maximize_window()
bl.driver.find_element_by_xpath("//button[text()='Click for JS Alert']").click()
time.sleep(3)

gs.acceptAlert(bl.driver)
time.sleep(3)
bl.driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
gs.dismissAlert(bl.driver)
time.sleep(3)
bl.driver.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()
gs.acceptAlertandsendkeys(bl.driver,"Hello Guys")
time.sleep(3)
#result = bl.driver.find_element_by_id("result").text
#print(result)
bl.driver.quit()
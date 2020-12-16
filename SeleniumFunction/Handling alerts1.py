
# this program about switch to alert(),.accept()
# another test website https://the-internet.herokuapp.com/
from selenium.webdriver.common.keys import Keys
from Launch import browerlaunch as bl
from SeleniumFunction import Generic as gs
import time
bl.driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
bl.driver.maximize_window()
bl.driver.find_element_by_name("proceed").click()
time.sleep(3)
alt = bl.driver._switch_to.alert
print("Alert text:",alt.text)
alt.accept()
time.sleep(3)
bl.driver.find_element_by_name("login").send_keys("Leka")
time.sleep(3)

bl.driver.quit()
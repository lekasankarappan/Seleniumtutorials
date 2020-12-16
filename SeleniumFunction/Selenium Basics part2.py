#from selenium.webdriver import Chrome
#from webdriver_manager.chrome import ChromeDriverManager
# this program about clear(),back(),forward()
from selenium.webdriver.common.keys import Keys
from Launch import browerlaunch as bl
from SeleniumFunction import Generic as gs
import time
bl.driver.get("https://www.google.com/")
bl.driver.maximize_window()
bl.driver.find_element_by_name("q").send_keys("Selenium jobs")
time.sleep(3)
bl.driver.find_element_by_name("q").clear()
time.sleep(4)

bl.driver.find_element_by_name("q").send_keys("Selenium Jobs",Keys.ENTER)
pgtitle=bl.driver.title
time.sleep(3)
assert pgtitle == "Selenium Jobs - Google Search"
print("page title",pgtitle)

bl.driver.back()
bl.driver.find_element_by_partial_link_text("Imag").click()
bl.driver.find_element_by_name("q").send_keys("Goa",Keys.ENTER)
#driver.save_screenshot("trip.png")
gs.takescreenshot(bl.driver)
time.sleep(4)
bl.driver.back()
time.sleep(3)
bl.driver.forward()
time.sleep(3)

bl.driver.quit()
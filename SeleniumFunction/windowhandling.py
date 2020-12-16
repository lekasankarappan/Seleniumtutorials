
# this program about window_handles, switch to.window()

from selenium.webdriver.common.keys import Keys
from Launch import browerlaunch as bl
from SeleniumFunction import Generic as gs
import time
bl.driver.get("https://www.google.com/intl/en-GB/gmail/about/#")
bl.driver.maximize_window()
bl.driver.find_element_by_xpath("(//a[@title='Create an account'])[1]").click()
win = bl.driver.window_handles
pgtitle = bl.driver.title
print(pgtitle)
first = win[0]
second = win[1]

print("First window :",first)
print("second window :",second)
bl.driver.switch_to.window(second)
pgtitle=bl.driver.title
print(pgtitle)
bl.driver.find_element_by_name("firstName").send_keys("Leka")

time.sleep(3)
#result = bl.driver.find_element_by_id("result").text
#print(result)
bl.driver.quit()
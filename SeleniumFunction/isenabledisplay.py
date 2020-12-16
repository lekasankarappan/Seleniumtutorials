
# this program about is enabled(),is selected(),isdisplayed()

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
fn = bl.driver.find_element_by_name("firstName")
if  fn.is_displayed():
   print("First Name is displayed :",fn.is_displayed())
   fn.send_keys("Leka")
   print("First Name is enabled:",fn.is_enabled())
next = bl.driver.find_element_by_css_selector(".VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc")
if  next.is_enabled():
    next.click()
time.sleep(3)
cb = bl.driver.find_element_by_xpath("//*[@type='checkbox']")
if cb.is_selected()== False:
    cb.click()
cb = bl.driver.find_element_by_xpath("//*[@type='checkbox']")
print("checkbox is selected?",cb.is_selected())
#result = bl.driver.find_element_by_id("result").text
#print(result)
bl.driver.quit()
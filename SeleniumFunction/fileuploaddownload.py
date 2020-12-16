
# this program about is enabled(),is selected(),isdisplayed()

from selenium.webdriver.common.keys import Keys
from Launch import browerlaunch as bl
from SeleniumFunction import Generic as gs
import time
bl.driver.get("https://the-internet.herokuapp.com/upload")

bl.driver.find_element_by_xpath("//input[@id='file-upload']").send_keys("C:/Users/Lenovo/Desktop/PycharmProjects/Seleniumtutorials/SeleniumFunction/screenshot2020_12_16_09_17_05.png")

bl.driver.find_element_by_xpath("//input[@id='file-submit']").click()
time.sleep(3)
bl.driver.get("https://the-internet.herokuapp.com/download")
bl.driver.find_element_by_link_text("screenshot2020_12_16_09_17_05.png").click()
time.sleep(4)
bl.driver.quit()

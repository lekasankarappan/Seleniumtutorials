#-->this pgm is about maximize(),pgtitle,datetime,screenshot

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from SeleniumFunction import Generic as gs
driver=Chrome(ChromeDriverManager().install())
import time
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("SeleniumFunction Jobs",Keys.ENTER)
pgtitle=driver.title
time.sleep(3)
print("page title",pgtitle)
driver.back()
driver.find_element_by_partial_link_text("Imag").click()
driver.find_element_by_name("q").send_keys("dandeli",Keys.ENTER)
#driver.save_screenshot("trip.png")
gs.takescreenshot(driver)
time.sleep(4)
driver.quit()
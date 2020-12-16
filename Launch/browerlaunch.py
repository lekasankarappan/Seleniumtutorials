from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
driver=Chrome(ChromeDriverManager().install())
import time
#driver.get("https://www.google.com/")
time.sleep(3)
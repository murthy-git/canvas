from selenium.webdriver import Chrome
from settings import CHROME_DRIVER_PATH
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = Chrome(CHROME_DRIVER_PATH)

driver.get('http://www.htmlcanvasstudio.com')

slider = driver.find_element_by_class_name('ui-slider-handle')
action = ActionChains(driver)
action.move_to_element(slider).click_and_hold()
action.move_by_offset(10, 0)
action.release()
action.perform()
time.sleep(5)

driver.quit()



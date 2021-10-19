from locators.locators import CanvasPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class CanvasPage:
    def __init__(self, driver):
        self.driver = driver
        self.canvas = driver.find_element(*CanvasPageLocators.canvas)

    def click_line(self):
        self.driver.find_element(*CanvasPageLocators.line).click()

    def click_rectangle(self):
        self.driver.find_element(*CanvasPageLocators.rectangle).click()

    def click_eraser(self):
        self.driver.find_element(*CanvasPageLocators.eraser).click()

    def draw_line(self, start_point, end_point):
        self.click_line()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.canvas, *start_point)
        action.click()
        action.move_to_element_with_offset(self.canvas, *end_point)
        action.click()
        action.perform()

    def draw_rectangle(self, start_point, end_point):
        self.click_rectangle()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.canvas, *start_point)
        action.click()
        action.move_to_element_with_offset(self.canvas, *end_point)
        action.click()
        action.perform()

    def erase_line(self, start_point, end_point):
        self.click_eraser()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.canvas, *start_point)
        action.click_and_hold()
        action.move_to_element_with_offset(self.canvas, *end_point)
        action.release()
        action.perform()

    def erase_rectangle(self, start_point, end_point):
        self.click_eraser()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.canvas, *start_point)
        action.click_and_hold()
        action.move_to_element_with_offset(self.canvas, end_point[0], start_point[1])
        action.move_to_element_with_offset(self.canvas, *end_point)
        action.move_to_element_with_offset(self.canvas, start_point[0], end_point[1])
        action.move_to_element_with_offset(self.canvas, *start_point)
        action.release()
        action.perform()


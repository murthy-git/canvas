from locators.locators import CanvasPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class CanvasPage:
    def __init__(self, driver):
        self.driver = driver
        self.canvas = driver.find_element(*CanvasPageLocators.canvas)

    def increase_slider(self):
        """Increases the size of default pain brush and eraser, Takes no args"""
        slider = self.driver.find_element(*CanvasPageLocators.slider)
        action = ActionChains(self.driver)
        action.move_to_element(slider).click_and_hold()
        action.move_by_offset(10, 0)
        action.release()
        action.perform()

    def click_line(self):
        """Finds the line element and clicks it, Takes no args"""
        self.driver.find_element(*CanvasPageLocators.line).click()

    def click_rectangle(self):
        """Finds the rectangle element and clicks it, Takes no args"""
        self.driver.find_element(*CanvasPageLocators.rectangle).click()

    def click_eraser(self):
        """Finds the line eraser and clicks it, Takes no args"""
        self.driver.find_element(*CanvasPageLocators.eraser).click()

    def draw_line(self, start_point: tuple, end_point: tuple):
        """Takes two args, start_point and end_point which determines
        the co-ordinated of start and end points of the line respectively. Draws a line from
        start point to end point"""
        self.click_line()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.canvas, *start_point)
        action.click()
        action.move_to_element_with_offset(self.canvas, *end_point)
        action.click()
        action.perform()

    def draw_rectangle(self, start_point: tuple, end_point: tuple):
        """Takes two args, start_point and end_point which determines
                the co-ordinated of start and end points of the rectangle respectively.
                Draws a rectangle from start point to end point"""
        self.click_rectangle()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.canvas, *start_point)
        action.click()
        action.move_to_element_with_offset(self.canvas, *end_point)
        action.click()
        action.perform()

    def erase_line(self, start_point: tuple, end_point: tuple):
        """Takes two args, start_point and end_point which determines
                the co-ordinated of start and end points of the line respectively. erases the line from
                start point to end point"""
        self.increase_slider()
        self.click_eraser()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.canvas, *start_point)
        action.click_and_hold()
        action.move_to_element_with_offset(self.canvas, *end_point)
        action.release()
        action.perform()

    def erase_rectangle(self, start_point, end_point):
        """Takes two args, start_point and end_point which determines
            the co-ordinated of start and end points of the rectangle respectively.
            finds all four corners of rectangle and erases the rectangle."""
        self.increase_slider()
        self.click_eraser()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.canvas, *start_point)
        action.click_and_hold()
        action.move_to_element_with_offset(self.canvas, end_point[0], start_point[1])
        action.move_to_element_with_offset(self.canvas, *end_point)
        action.move_to_element_with_offset(self.canvas, start_point[0], end_point[1])
        action.move_to_element_with_offset(self.canvas, start_point[0], start_point[1]-5)
        action.release()
        action.perform()


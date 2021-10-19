from selenium.webdriver import Chrome
from settings import CHROME_DRIVER_PATH
from actions import CanvasPageActions
from consts import *


def perform_task():
    cp.draw_line(HORIZONTAL_LINE_START, HORIZONTAL_LINE_END)
    cp.draw_line(VERTICAL_LINE_START, VERTICAL_LINE_END)
    cp.draw_rectangle(RECTANGLE_START, RECTANGLE_END)
    cp.erase_line(HORIZONTAL_LINE_START, HORIZONTAL_LINE_END)
    cp.erase_line(VERTICAL_LINE_START, VERTICAL_LINE_END)
    cp.erase_rectangle(RECTANGLE_START, RECTANGLE_END)


if __name__ == '__main__':
    driver = Chrome(CHROME_DRIVER_PATH)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.get(URL)
    driver.fullscreen_window()
    cp = CanvasPageActions(driver)
    perform_task()












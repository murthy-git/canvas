from selenium.webdriver import Chrome
from settings import CHROME_DRIVER_PATH
from pages.canvaspage import CanvasPage
from utils.consts import Constants


def perform_task():
    cp.draw_line(Constants.HORIZONTAL_LINE_START, Constants.HORIZONTAL_LINE_END)
    cp.draw_line(Constants.VERTICAL_LINE_START, Constants.VERTICAL_LINE_END)
    cp.draw_rectangle(Constants.RECTANGLE_START, Constants.RECTANGLE_END)
    cp.erase_line(Constants.HORIZONTAL_LINE_START, Constants.HORIZONTAL_LINE_END)
    cp.erase_line(Constants.VERTICAL_LINE_START, Constants.VERTICAL_LINE_END)
    cp.erase_rectangle(Constants.RECTANGLE_START, Constants.RECTANGLE_END)


if __name__ == '__main__':
    driver = Chrome(CHROME_DRIVER_PATH)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.get(Constants.URL)
    driver.fullscreen_window()
    cp = CanvasPage(driver)
    perform_task()












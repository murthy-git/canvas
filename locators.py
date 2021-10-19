from selenium.webdriver.common.by import By


class CanvasPageLocators:
    line = (By.CLASS_NAME, 'line')
    eraser = (By.CLASS_NAME, 'eraser')
    canvas = (By.ID, 'imageTemp')
    rectangle = (By.CLASS_NAME, 'rectangle')
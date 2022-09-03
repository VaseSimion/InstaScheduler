from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://unsplash.com/s/photos/tree")
    action = ActionChains(driver)

    # get element
    elements = driver.find_elements(By.CLASS_NAME, "GIFah")
    for chunk in elements:
        #print(chunk.get_attribute('innerHTML'))
        part_with_button = chunk.find_element(By.CLASS_NAME, "XIPC3.HxMEi")
        print(part_with_button)
    # create action chain object

    # click the item
        action.click(on_element=part_with_button)

    # perform the operation
        action.perform()
        time.sleep(10)
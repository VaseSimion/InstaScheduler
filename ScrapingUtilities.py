from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://unsplash.com/s/photos/" + sys.argv[1])
    action = ActionChains(driver)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Load more photos')]")
    print(element)
    print(element.get_attribute('innerHTML'))
    action.click(on_element=element)
    action.perform()
    time.sleep(5)
    for i in range(40):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)

    elements = driver.find_elements(By.CLASS_NAME, "GIFah")
    print("Found", len(elements), "elements")

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
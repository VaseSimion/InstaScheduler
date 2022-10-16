from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import requests
import sys


if __name__ == "__main__":
    
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    downloader = webdriver.Chrome()
    driver.get("https://unsplash.com/s/photos/" + sys.argv[1])
    action = ActionChains(driver)

    element = driver.find_element(By.XPATH, "//button[contains(text(),'Load more photos')]")
    print(element)
    print(element.get_attribute('innerHTML'))
    action.click(on_element=element)
    action.perform()
    time.sleep(5)
    for i in range(20):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(3)

    elements = driver.find_elements(By.CLASS_NAME, "GIFah")
    print("Found", len(elements), "elements")

    for chunk in elements:
        part_with_button = chunk.find_element(By.CLASS_NAME, "XIPC3.HxMEi")
        downloader.get(part_with_button.get_attribute('innerHTML').split()[21].split("\"")[1])
        print(part_with_button.get_attribute('innerHTML').split()[21].split("\"")[1])
        time.sleep(3)
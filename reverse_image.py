from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome("drivers/chromedriver.exe")
driver.get("https://images.google.com/")

def reverse_image():
    sleep(.5)
    reject_cookies_button = driver.find_element(By.XPATH, '//button[@id="L2AGLb"]')
    driver.execute_script("arguments[0].click();", reject_cookies_button)

    sleep(.5)

    search_btn = driver.find_element(By.XPATH, '//div[@class="ZaFQO"]')
    driver.execute_script("arguments[0].click();", search_btn)

    sleep(.5)

    upload_btn = driver.find_element(By.XPATH, '//a[text()="Upload an image"]').click()
    # driver.execute_script("arguments[0].click();", search_btn)


    sleep(.5)

    upload_img = driver.find_element_by_id("awyMjb").send_keys(os.getcwd()+"/quiz_image.png")

reverse_image()

sleep(60)
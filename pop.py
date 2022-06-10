from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome("drivers/chromedriver.exe")
driver.get("https://jklm.fun/ukzq")

ok_btn = driver.find_element(By.XPATH, '//button[text()="OK"]')
driver.implicitly_wait(3)
ok_btn.click()
sleep(2)

driver.switch_to.frame(driver.find_element(by=By.TAG_NAME, value="iframe"))

# image = driver.find_element(By.XPATH, '//span[@class="prompt"]')
image = driver.find_element(By.XPATH, '//div[@class="actual"]').get_attribute("style")

url = image[image.find("\"") + 1 : image.rfind("\"")]
print(url)
driver.get(url)

sleep(1)

with open('quiz_image.png', 'wb') as file:
#identify image to be captured
   grabbed_image = driver.find_element(by=By.TAG_NAME, value='img')
#write file
   file.write(grabbed_image.screenshot_as_png)

driver.get("https://images.google.com/")

sleep(.3)
reject_cookies_button = driver.find_element(By.XPATH, '//button[@id="L2AGLb"]')
driver.execute_script("arguments[0].click();", reject_cookies_button)

# sleep(.3)

search_btn = driver.find_element(By.XPATH, '//div[@class="ZaFQO"]')
driver.execute_script("arguments[0].click();", search_btn)

sleep(.3)

upload_btn = driver.find_element(By.XPATH, '//a[text()="Upload an image"]').click()
# driver.execute_script("arguments[0].click();", search_btn)

sleep(.3)

upload_img = driver.find_element_by_id("awyMjb").send_keys(os.getcwd()+"/quiz_image.png")

sleep(15)



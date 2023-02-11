from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

def run():
    driver = webdriver.Chrome()
    driver.get("https://www.twitter.com")
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "input").send_keys("selenium" + Keys.ENTER)
    time.sleep(20)
    # driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div").click()
    driver.quit()

if __name__ == "__main__" :
    run()

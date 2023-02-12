from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint

import time

def run():
    driver = webdriver.Chrome()
    driver.get("https://www.twitter.com")
    time.sleep(randint(3,7))
    driver.find_element(By.TAG_NAME, "input").send_keys("#chelseabun" + Keys.ENTER)
    time.sleep(2)
    output = driver.find_elements(By.CLASS_NAME, "css-1dbjc4n")

    for i in output:
        print(i.text)
    driver.quit()

if __name__ == "__main__" :
    run()

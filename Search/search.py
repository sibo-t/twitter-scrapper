from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from random import randint

import time

def run(n, look_up):
    """Creates a tweetdump.txt file with tweets relating to the searched topic

    Args:
        n (int): Try to look for n amount of unique tweets
        look_up (str): Topic of the tweets
    """

    # Create options object for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.twitter.com")
    time.sleep(randint(3,7))
    driver.find_element(By.TAG_NAME, "input").send_keys("#"+look_up+ Keys.ENTER)

    f= open("tweetdump.txt","w+")

    for i in range(n):
        
        f.write(retrieve_data(driver).text)

        ActionChains(driver)\
            .send_keys(Keys.ESCAPE)\
                .perform()
        time.sleep(randint(5,10))

    f.close()

    driver.quit()

def retrieve_data(driver):
    
    output = driver.find_element(By.TAG_NAME, "main")
    
    ActionChains(driver)\
        .scroll_by_amount(0, 700)\
        .perform()

    return output

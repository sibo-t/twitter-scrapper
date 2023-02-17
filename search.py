from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from random import randint

import time

def run():
    driver = webdriver.Chrome()
    driver.get("https://www.twitter.com")
    time.sleep(randint(3,7))
    driver.find_element(By.TAG_NAME, "input").send_keys("#chelseabun" + Keys.ENTER)

    # output = retrieve_data(driver)

    # for j in range(10):
    #     output.extend(retrieve_data(driver))
    #     ActionChains(driver)\
    #         .send_keys(Keys.ESCAPE)\
    #             .perform()
    #     time.sleep(randint(3,7))
        

    count = 0
    f= open("tweetdump2.txt","w+")

    for i in range(10):
        
        f.write("*********************"+str(count)+"*************************\n")
        f.write("\n")
        f.write(retrieve_data(driver).text)
        f.write("\n")
        f.write("*******************************************************\n")
        f.write("\n")
        count+=1

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


if __name__ == "__main__" :
    run()

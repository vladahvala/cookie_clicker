from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def get_scores(scores):
    """get numbers"""
    try:
        num = int(scores.text.split()[0])
        return num
    except ValueError:
        return 0

def  click_cursor(browser, scores):
    """Click the first product"""
    try:
        price = int(browser.find_element(By.ID, "productPrice").text)
    except ValueError:
        price=0
    if price and price<=get_scores(scores):   
        prod0 = browser.find_element(By.ID, "product0")
        prod0.click()

def main():
    browser = webdriver.Chrome()
    browser.get("https://orteil.dashnet.org/cookieclicker/")
    cookie = browser.find_element(By.ID, "bigCookie") 
    scores = browser.find_element(By.ID, "cookies")
    while True:
        cookie.click()
        time.sleep(0.1)
        num = get_scores(scores)
        click_cursor(browser, scores)
        upgrades = browser.find_elements(By.CLASS_NAME, "upgrade")
        if num > 100 and len(upgrades)>1:
            upgrades[0].click()
            print("upgraded!!!")

if __name__ == '__main__':
    main()
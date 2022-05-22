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

def main():
    browser = webdriver.Chrome() 
    browser.get("https://orteil.dashnet.org/cookieclicker/")
    cookie = browser.find_element(By.ID, "bigCookie")
    #upgrades = browser.find_element(By.CLASS_NAME, "upgrade")
    #upgrade = browser.find_element(By.ID, "upgrade0")
    scores = browser.find_element(By.ID, "cookies")
    while True:
        cookie.click()
        time.sleep(0.1)
        num = get_scores(scores)
        upgrades = browser.find_element(By.CLASS_NAME, "upgrade")
        if num > 100 and len(upgrades)>0:
            upgrades[0].click()
            print("upgraded!!!")

if __name__ == '__main__':
    main()
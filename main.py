# Automatic fill the username and password then login
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
service = Service('C:\\Users\\frien\\Downloads\\chromedriver.exe')

def get_driver():
    # Set options to make browsing easier.
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


def main():
    driver = get_driver()

    # find and fill the username and password
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(1)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.ENTER)
    time.sleep(1)

    # click on homescreen and wait 2 seconds
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print("Successfully logged in " + driver.current_url)
    time.sleep(2)


print(main())

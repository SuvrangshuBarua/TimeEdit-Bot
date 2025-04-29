import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, ElementClickInterceptedException

def timeedit_chalmers(driver):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".leftlistcolumn > a:last-child"))
        )
        element.click()
        print("Clicked on Chalmers University of Technology link.")
        search_course(driver)
    except (TimeoutException, ElementNotInteractableException, ElementClickInterceptedException) as e:
        print(f"Error occurred while clicking the link: {e}")
        return
    
def search_course(driver):
    try:
        search_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ffsearchname"))
        )
        search_box.click()
        search_box.send_keys("DAT520" + Keys.ENTER)
        print("Searched for course DAT520.")
        return
    except (TimeoutException, ElementNotInteractableException) as e:
        print(f"Error occurred while searching for course: {e}")
        return


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


try:

    driver.get("https://cloud.timeedit.net/chalmers/web/public/")
    timeedit_chalmers(driver)
finally:
    time.sleep(10)
    driver.quit()
    print("Driver closed successfully.")
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, ElementClickInterceptedException

def timeedit_chalmers(driver, courses):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".leftlistcolumn > a:last-child"))
        )
        element.click()
        print("Clicked on Chalmers University of Technology link.")
        for course in courses:
            search_course(driver, course)

        objectbasketgo_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "objectbasketgo"))
        )
        objectbasketgo_button.click()
        print("Clicked on the objectbasketgo button.")
    except (TimeoutException, ElementNotInteractableException, ElementClickInterceptedException) as e:
        print(f"Error occurred while clicking the link: {e}")
        return        
        
    
def search_course(driver, course):
    try:
        search_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ffsearchname"))
        )
        search_box.click()
        search_box.clear()
        search_box.send_keys(course + Keys.ENTER)
        print("Found course:", course)

        add_all_button = course_item = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'clickable2') and contains(normalize-space(), '{course}')]"))
        )
        add_all_button.click()

        print("Added course:", course)

        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, f"//div[contains(@class, 'clickable2') and contains(normalize-space(), '{course}')]"))
        )

    except (TimeoutException, ElementNotInteractableException) as e:
        print(f"Error occurred while searching for course: {e}")
        return


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
course_input = input("Enter the course codes separated by semicolon: ").strip().upper()
courses = [code.strip() for code in course_input.split(";") if code.strip()]

try:

    driver.get("https://cloud.timeedit.net/chalmers/web/public/")
    timeedit_chalmers(driver, courses)
finally:
    # Take a screenshot before closing the driver
    driver.save_screenshot("final_result.png")
    print("Screenshot saved as final_result.png")
    time.sleep(10)
    driver.quit()
    print("Driver closed successfully.")
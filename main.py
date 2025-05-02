import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, ElementClickInterceptedException

# constants
ladok_url = "https://www.student.ladok.se/"
timeedit_url = "https://cloud.timeedit.net/chalmers/web/public/"
wait_time = 2  

def get_user_credentials():
    username = input("Enter your username: ").strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    password = input("Enter your password: ").strip()
    if not password:
        raise ValueError("Password cannot be empty.")
    return username, password

def ladok_login(driver, username, password):
    try:
        driver.get(ladok_url)

        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "discoveryServiceIdBtn"))
        ).click()
       
        uni_search_box = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.ID, "searchinput"))
        )
        uni_search_box.click()
        uni_search_box.clear()
        uni_search_box.send_keys("University of Gothenburg" + Keys.ENTER)

        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "text-truncate.label.primary"))
        ).click()

        username_input = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "userNameInput"))
        )

        username_input.click()
        username_input.clear()
        username_input.send_keys(username + Keys.ENTER) 

        password_input = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "passwordInput"))
        )
        password_input.click()
        password_input.clear()
        password_input.send_keys(password + Keys.ENTER)
        print("Entered username and password.")
        return True
    except (TimeoutException, ElementNotInteractableException, ElementClickInterceptedException) as e:
        print(f"Error occurred while clicking the link: {e}")
        return False
    
def extract_course_codes(driver):
    try:
        course_cards = WebDriverWait(driver, wait_time).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "ladok-aktuell-kurs-kort"))
        )

        course_codes = []

        for index, course_card in enumerate(course_cards):
            try:
                course_name_element = course_card.find_element(By.CSS_SELECTOR, "h3.card-title span.ladok-card-body-rubrik a")
                course_name = course_name_element.text.strip()
                course_code = course_name.split(" - ")[-1].strip()
                course_codes.append(course_code)
            except Exception as e:
                print(f"Error occurred while extracting course code from card {index}: {e}")
                continue

        return course_codes

    except (TimeoutException, ElementNotInteractableException) as e:
        print(f"Error occurred while locating course cards: {e}")
        return []
    
def timeedit_chalmers(driver, courses):
    try:
        driver.get(timeedit_url)
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".leftlistcolumn > a:last-child"))
        ).click()

        for course in courses:
            search_course(driver, course)

        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.ID, "objectbasketgo"))
        ).click()

    except (TimeoutException, ElementNotInteractableException, ElementClickInterceptedException) as e:
        print(f"Error occurred while clicking the link: {e}")
        return        
        
    
def search_course(driver, course):
    try:
        search_box = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "ffsearchname"))
        )
        search_box.click()
        search_box.clear()
        search_box.send_keys(course + Keys.ENTER)
        print("Found course:", course)

        add_all_button = course_item = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'clickable2') and contains(normalize-space(), '{course}')]"))
        )
        add_all_button.click()

        print("Added course:", course)

        WebDriverWait(driver, wait_time).until(
            EC.invisibility_of_element_located((By.XPATH, f"//div[contains(@class, 'clickable2') and contains(normalize-space(), '{course}')]"))
        )

    except (TimeoutException, ElementNotInteractableException) as e:
        print(f"Error occurred while searching for course: {e}")
        return

def main():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        username, password = get_user_credentials()
        
        if ladok_login(driver, username, password):
            extract_course_codes(driver)
            courses = extract_course_codes(driver)
            if courses:
                timeedit_chalmers(driver, courses)
            else:
                print("No courses found to process.")
    finally:
        # Take a screenshot before closing the driver
        driver.save_screenshot("final_result.png")
        print("Screenshot saved as final_result.png")
        time.sleep(2)
        driver.quit()
        print("Driver closed successfully.")

if __name__ == "__main__":
    main()
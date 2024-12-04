from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def display_ascii_art():
    # ASCII Waji Qof Ah oo Midab leh
    ascii_art = """
    \033[1;32m     O     O      \033[1;33m
        \  -  /       \033[1;31m
         \___/        \033[0m
     Code by Pop-Smoke and Rohan
    """
    print(ascii_art)

def tiktok_report_generator(username):
    try:
        # ASCII Waji Qof Ah
        display_ascii_art()
        
        # Initialize Chrome WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Navigate to TikTok
        driver.get("https://www.tiktok.com/")
        wait = WebDriverWait(driver, 15)

        # Wait for the search bar to load
        search_bar = wait.until(EC.presence_of_element_located((By.ID, "native-search-input")))

        # Enter the username in the search bar
        search_bar.send_keys(username)
        search_bar.submit()

        # Wait for search results to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-e2e='search-result']")))

        # Open the first user profile from the search results
        first_profile = driver.find_element(By.CSS_SELECTOR, "div[data-e2e='search-result'] a")
        first_profile.click()

        # Wait for the user profile to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-e2e='user-profile']")))

        # Scroll down to ensure all videos load
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Open the first video
        first_video = driver.find_element(By.CSS_SELECTOR, "div[data-e2e='user-post-item']:first-child")
        first_video.click()

        # Wait for the video page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-e2e='video-detail']")))

        # Click the report button
        try:
            report_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Report')]")
            report_button.click()
        except NoSuchElementException:
            print("Report button not found. Exiting.")
            driver.quit()
            return

        # Wait for the report popup to appear
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.report-popup")))

        # Select report reason: Cyberbullying (Customize as needed)
        try:
            cyberbullying_option = driver.find_element(By.XPATH, "//button[contains(text(), 'Cyberbullying')]")
            cyberbullying_option.click()
        except NoSuchElementException:
            print("Cyberbullying option not found.")
        
        # Add logic for other reporting options
        other_options = ["Fake News", "Phishing", "Sexual Content", "Graphic Violence"]
        for option in other_options:
            try:
                report_option = driver.find_element(By.XPATH, f"//button[contains(text(), '{option}')]")
                report_option.click()
                time.sleep(1)  # Allow some time for action completion
            except NoSuchElementException:
                print(f"Option '{option}' not found.")

        print("Reports submitted successfully.")

    except TimeoutException as e:
        print(f"Timeout Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    tiktok_report_generator("example_username")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler
import datetime
import os

log_dir = os.path.join(os.path.dirname(__file__),"logs")
os.makedirs(log_dir,exist_ok=True)
log_file_path = os.path.join(log_dir,"linkedin_bot.log")

handler = RotatingFileHandler(log_file_path , maxBytes=500000, backupCount=3)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger = logging.getLogger("LinkedInBot")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def linkdin_login(email , password):
    
    try:
        driver_path = os.path.join(os.path.dirname(__file__), "drivers", "chromedriver.exe")
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.linkedin.com/login")
        logger.info("Opened LinkedIn login page")
        email_input = driver.find_element(By.NAME ,"session_key")
        email_input.send_keys(email)
        password_input = driver.find_element(By.NAME,"session_password")
        password_input.send_keys(password)
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        logger.info("Credentials submitted")
        try:
            WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.CLASS_NAME, "captcha__challenge"))
            )
            logger.warning("Captcha detected. Please solve it manually.")
            input("Press Enter after solving captcha...")
        
        except:
           logger.info("No captcha detected.")

        try:
            WebDriverWait(driver,10).until(
            ec.presence_of_element_located((By.CLASS_NAME ,"search-global-typeahead__input")))
            logger.info("login successful ")
             
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshots_dir, f"login_success_{timestamp}.png")

            success = driver.save_screenshot(screenshot_path)
            if success:
                 logger.info(f"Screenshot saved at: {screenshot_path}")
            else:
                 logger.warning("Screenshot not saved!")


        except:
            logger.error("Login failed or search bar not found")

    except Exception as e:
        logger.exception("An unexpected error occurred")

    finally:
        driver.quit()   
        logger.info("driver closed")

def main():
    env_path = os.path.join(os.path.dirname(__file__), ".env")

    if os.path.isfile(env_path):
        load_dotenv(env_path)
        email = os.getenv("Email")
        password = os.getenv("Password")

        if not email or not password:
            logger.warning(".env file found, but Email or Password is missing!")
            return 
        
        linkdin_login(email, password)

    else:
        logger.warning(".env file not found! Please create one with your Email and Password.")
        email = input("Email: ")
        password = input("Password: ")
        linkdin_login(email, password)

if __name__=="__main__":
    main()


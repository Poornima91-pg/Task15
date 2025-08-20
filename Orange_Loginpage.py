from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class Orange_login():

    def __init__(self,driver):

        # Initialize the Loginpage object with Selenium WebDriver instance and define element locators for the page.
        self.driver = driver

        # Username,Password & login button locator locator
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

        # Dashboard & error msg locator
        self.dashboard_locator = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
        self.error_message = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")

    # gets username
    def enter_username(self, username):
        try:
            # Waits for the username field to be visible and enters the provided username from excel
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        except (TimeoutException, NoSuchElementException):
            print("Username field not found")
            return False
        return True

    # gets password
    def enter_password(self, password):
        try:
            # Waits for the password field to be visible and enters the provided password from excel
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        except (TimeoutException, NoSuchElementException):
            print("Password field not found")
            return False
        return True

    # Waits until the login button is clickable and clicks it.
    def click_login(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
        except (TimeoutException, NoSuchElementException):
            print("Login button not clickable")
            return False
        return True

    # Check whether login is success or failure
    def get_login_status(self):
        # Returns "Success" if login is successful,"Failed" if error message is displayed,
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.dashboard_locator))
            return "Success"
        except TimeoutException:
            # Dashboard not found, check for error message
            try:
                WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.error_message))
                return "Failed"
            except TimeoutException as e:
                print(e)


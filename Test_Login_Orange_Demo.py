import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Task15.Orange_Loginpage import Orange_login
from Task15.Excel_Utility_file import ExcelUtil
from selenium.webdriver.chrome.options import Options

# Initialize Excel utility (to read test data and write results)
excel = ExcelUtil("D:/Poornima/Ofc/Automation_class/Code/Selenium/Task15/test_data.xlsx")

# Parametrize test with data from Excel → [(row, username, password), ...]
@pytest.mark.parametrize("row,username,password",excel.get_param_data())
def test_login_demosite(row,username,password):
    # Create Chrome options to customize browser behavior
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')

    # Launch Chrome browser with WebDriver Manager and navigate to orange demosite page
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Open OrangeHRM demo site
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Create page object for login
        Orangelogin = Orange_login(driver)

        # Perform login actions
        Orangelogin.enter_username(username)
        Orangelogin.enter_password(password)
        Orangelogin.click_login()

        # Get login result
        status = Orangelogin.get_login_status()

        # Write test results back to Excel
        if status == "Success":
            excel.write_test_result(row, "Passed")
            # assert True
        else:
            excel.write_test_result(row, "Failed")
            # assert False

    finally:
        # closes the browser
        driver.quit()
""""
Invalid_HomePageLogin.py
Program : file containing locators for OrangeHRM
"""


#TestCase_02- OrangeHRM Invalid Login Credential Locators
class InvalidData_Locators:
    #TestCase-02
    username_locator = "username"
    password_locator = "password"
    submit_button = "//button[@type='submit']"
    admin_user = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    logout_button = "Logout"

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    excel_file = "C:\\Users\\sunma\\PycharmProjects\\AT_Project1\\Data\\Test_data_OrangeHRM.xlsx"

    #sheet2
    sheet_number_2 = "Sheet2"
    fail_data = "Test Failed"
    # error message
    error_message_locator = "//div[@class='oxd-alert-content oxd-alert-content--error']"

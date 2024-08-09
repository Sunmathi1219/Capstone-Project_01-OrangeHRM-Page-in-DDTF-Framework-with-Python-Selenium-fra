""""
HomePage.py
Program : file containing locators for OrangeHRM Login Page
"""


#TestCase_01 - OrangeHRM Valid Login Locators
class OrangeHRM_Locators:
    #TestCase-01
    username_locator = "username"
    password_locator = "password"
    submit_button = "//button[@type='submit']"
    admin_user = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    logout_button = "Logout"
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    excel_file = "C:\\Users\\sunma\\PycharmProjects\\AT_Project1\\Data\\Test_data_OrangeHRM.xlsx"
    sheet_number_1 = "Sheet1"
    pass_data = "Test Passed"




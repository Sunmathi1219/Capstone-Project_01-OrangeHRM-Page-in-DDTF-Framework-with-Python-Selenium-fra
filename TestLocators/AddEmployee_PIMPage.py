""""
AddEmployee_PIMPPage.py
Program : file containing locators for OrangeHRM
"""

#TestCase_03- Adding Employee In the PIM Module Locators
class AddEmployee_Page:
    #TestCase-03
    username_locator = "username"
    password_locator = "password"
    submit_button = "//button[@type='submit']"
    admin_user = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    logout_button = "Logout"
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    excel_file = "C:\\Users\\sunma\\PycharmProjects\\AT_Project1\\Data\\Test_data_OrangeHRM.xlsx"

    # sheet3
    sheet_number_3 = "Sheet3"
    dashboard_locator = "//div//div//i[@class='oxd-icon bi-list oxd-topbar-header-hamburger']"
    pim_locator = "//a[@href='/web/index.php/pim/viewPimModule']"
    add_button_locator = "//div[@class='orangehrm-header-container']//button[@type='button']"

    firstname_locator = "//input[@name='firstName']"
    lastname_locator = "lastName"
    middle_name_locator = "middleName"
    employee_id_locator = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"

    enable_button = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    username_loc = "(//input[@class='oxd-input oxd-input--active'])[3]"
    status_locator = "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]"
    password_loc = "(//input[@class='oxd-input oxd-input--active'])[4]"
    confirm_password_loc = "(//input[@type='password'])[2]"
    save_button_locator = "//button[@type='submit']"
    toast_message_locator = "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']//div//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"



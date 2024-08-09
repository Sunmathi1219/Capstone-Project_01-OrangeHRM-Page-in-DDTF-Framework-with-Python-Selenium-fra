""""
DeleteEmployee_PIMPPage.py
Program : file containing locators for OrangeHRM
"""


#TestCase_05- Delete the Employee Detail in PIM Module
class DeleteEmployee_Page:
    #TestCase-04
    username_locator = "username"
    password_locator = "password"
    submit_button = "//button[@type='submit']"
    admin_user = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    logout_button = "Logout"
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    excel_file = "C:\\Users\\sunma\\PycharmProjects\\AT_Project1\\Data\\Test_data_OrangeHRM.xlsx"

    # sheet4
    sheet_number_5 = "Sheet5"
    dashboard_locator = "//div//div//i[@class='oxd-icon bi-list oxd-topbar-header-hamburger']"
    pim_locator = "//a[@href='/web/index.php/pim/viewPimModule']"


    delete_locator = "(//button[@type='button']//i[@class='oxd-icon bi-trash'])[2]"
    delete_button_locator = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"

    #toast message
    toast_message_locator = "//div[@class='oxd-toast-content oxd-toast-content--success']//p[text()='Successfully Deleted']"



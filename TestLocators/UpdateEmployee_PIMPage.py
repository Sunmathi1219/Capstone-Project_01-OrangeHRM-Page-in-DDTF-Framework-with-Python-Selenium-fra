""""
UpdateEmployee_PIMPPage.py
Program : file containing locators for OrangeHRM
"""

#TestCase_04- Edit the Employee Details in PIM Module Locators
class UpdateEmployee_Page:
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
    sheet_number_4 = "Sheet4"
    dashboard_locator = "//div//div//i[@class='oxd-icon bi-list oxd-topbar-header-hamburger']"
    pim_locator = "//a[@href='/web/index.php/pim/viewPimModule']"

    #search employee
    edit_element_locator = "(//button[@type='button']//i[@class='oxd-icon bi-pencil-fill'])[1]"

    #edit element data
    first_name_locator = "//div[@class='--name-grouped-field']//div//div//input[@name='firstName']"
    middle_name_locator = "//div[@class='--name-grouped-field']//div//div//input[@name='middleName']"
    last_name_locator = "//div[@class='--name-grouped-field']//div//div//input[@name='lastName']"

    employee_id_locator = "(//input[@class='oxd-input oxd-input--active'])[2]"
    other_id_locator = "//form[@class='oxd-form']//div[2]//div[1]//div[2]//div//div[2]//input[@class='oxd-input oxd-input--active']"
    driver_license_no_locator = "//form[@class='oxd-form']//div[2]//div[2]//div[1]//div//div[2]//input[@class='oxd-input oxd-input--active']"
    license_exp_locator = "//form[@class='oxd-form']//div[2]//div[2]//div[2]//div//div[2]//input[@class='oxd-input oxd-input--active']"

    nationality_locator = "//form[@class='oxd-form']//div[3]//div[1]/div[1]//div//div[2]//div//div//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    nationality_dropdown_locator = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[6]"

    marital_status_locator = "//form[@class='oxd-form']//div[3]//div[1]//div[2]//div//div[2]//div//div//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    status_dropdown_locator = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]"

    dob_locator = "//form[@class='oxd-form']//div[3]//div[2]//div[1]//div//div[2]//div//div//input[@placeholder='yyyy-dd-mm']"
    gender_locator = "//form[@class='oxd-form']//div[3]//div[2]//div[2]//div//div[2]//div[1]//div[2]//div//label//span"

    save_button1_locator = "(//button[ @type='submit'])[1]"

    toast_message_locator1 = "//div[@class='oxd-toast-content oxd-toast-content--success']//p[text()='Successfully Updated']"


    blood_type_locator = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i"
    blood_dropdown_locator = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"
    test_field_locator = "(//div//div//div[2]//input[@class='oxd-input oxd-input--active'])[7]"
    save_button2_locator = "(//button[ @type='submit'])[2]"

    toast_message_locator2 = "//div[@class='oxd-toast-content oxd-toast-content--success']//p[text()='Successfully Saved']"






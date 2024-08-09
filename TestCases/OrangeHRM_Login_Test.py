"""
OrangeHRM_Login_Test.py
xSuccessfully employee login to OrangeHRM portal with valid username and valid password
Testcase-02:
Login with valid username and invalid password and display error message "invalid Credentials"
TestCase-03:
Add a new employee in the PIM module and should see a message for "successful employee addition"
TestCase-04:
Edit the added Employee details in the PIM Module and see the "Successfully saved" message.
TestCase-05:
Delete the particular employee detail in the PIM Module and should see "successful deleted" message
"""

#import packages
from Utilities.tc_01_excel_functions import HRM_Excel_Functions
from Locators.HomePage import OrangeHRM_Locators
from Locators.Invalid_HomepageLogin import InvalidData_Locators
from Locators.AddEmployee_PIMPage import AddEmployee_Page
from Locators.UpdateEmployee_PIMPage import UpdateEmployee_Page
from Locators.DeleteEmployee_PIMPage import DeleteEmployee_Page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#Exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
#for explicit wait only
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
#for test report
import pytest


class OrangeHRMPage:
    excel_file = OrangeHRM_Locators().excel_file

    #for TestCase-01
    sheet_number_1 = OrangeHRM_Locators().sheet_number_1

    #for TestCase-02
    sheet_number_2 = InvalidData_Locators().sheet_number_2

    #for TestCase-03
    sheet_number_3 = AddEmployee_Page().sheet_number_3

    #for TestCase-04
    sheet_number_4 = UpdateEmployee_Page().sheet_number_4

    # for TestCase-05
    sheet_number_5 = DeleteEmployee_Page.sheet_number_5

    # create object for the Excel Utility Class for TestCase-01
    login_tc_01 = HRM_Excel_Functions(excel_file, sheet_number_1)

    # create object for the Excel Utility Class for TestCase-02
    login_tc_02 = HRM_Excel_Functions(excel_file, sheet_number_2)

    # create object for the Excel Utility Class for TestCase-03
    login_tc_03 = HRM_Excel_Functions(excel_file, sheet_number_3)

    # create object for the Excel Utility Class for TestCase-04
    login_tc_04 = HRM_Excel_Functions(excel_file, sheet_number_4)

    # create object for the Excel Utility Class for TestCase-05
    login_tc_05 = HRM_Excel_Functions(excel_file, sheet_number_5)

    def __init__(self, url):
        try:
            self.url = url
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 20)


        except WebDriverException as e:
            print(e)

    #TestCase-01:
    # login page valid username and valid password datas and datas from Excel file
    def login_Testcase_01(self):
        try:

            self.driver.get(OrangeHRM_Locators().url)

            # row count from the Excel file
            row = self.login_tc_01.row_count()

            #iterate the row to get the data's
            for row in range(2, row + 1):
                username = self.login_tc_01.read_data(row, 7)
                password = self.login_tc_01.read_data(row, 8)

                user_name = self.wait.until(
                    EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().username_locator)))
                user_name.send_keys(username)

                pass_word = self.wait.until(
                    EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().password_locator)))
                pass_word.send_keys(password)

                login_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators().submit_button)))
                login_button.click()

                # validate the login and generate the Test-Case results & reports
                if OrangeHRM_Locators().dashboard_url == self.driver.current_url:

                    print("SUCCESS : Login with Username : {a} & Password : {b}".format(a=username, b=password))
                    self.login_tc_01.write_data(row, 9, OrangeHRM_Locators().pass_data)
                    admin_user = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators().admin_user)))
                    action = ActionChains(self.driver)
                    action.click(on_element=admin_user).perform()
                    self.wait.until(
                        EC.element_to_be_clickable((By.LINK_TEXT, OrangeHRM_Locators().logout_button))).click()
                    return True
                else:
                    print("ERROR: Login is unsuccessful")


        except NoSuchElementException as e:
            print(e)

    #TestCase-02
    # login page valid username and Invalid password datas and datas from Excel file
    def login_Testcase_02(self):
        try:
            self.driver.get(InvalidData_Locators().url)

            # row count from the Excel file
            row = self.login_tc_02.row_count()

            #iterating row data
            for row in range(2, row + 1):
                username = self.login_tc_02.read_data(row, 7)
                password = self.login_tc_02.read_data(row, 8)

                user_name = self.wait.until(
                    EC.presence_of_element_located((By.NAME, InvalidData_Locators().username_locator)))
                user_name.send_keys(username)

                pass_word = self.wait.until(
                    EC.presence_of_element_located((By.NAME, InvalidData_Locators().password_locator)))
                pass_word.send_keys(password)

                login_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, InvalidData_Locators().submit_button)))
                login_button.click()

                # fetch error message from webPage
                error_message = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, InvalidData_Locators().error_message_locator)))

                # validate the login with valid username and invalid password and generate the Test-Case results & reports
                if InvalidData_Locators().url == self.driver.current_url:

                    print(
                        "Success : Login unsuccessful with valid username {a} & Invalid Password {b}".format(a=username,
                                                                                                             b=password))
                    #print error message Text from webpage into console
                    print("Invalid Password Error message for OrangeHRM Login Page: ", error_message.text)
                    self.login_tc_02.write_data(row, 9, InvalidData_Locators().fail_data)
                    self.driver.refresh()
                    return True
                else:
                    print("ERROR")
                    return False

        except NoSuchElementException as e:
            print(e)

    #TestCase-03 Successful employee addition
    def add_employee(self):
        try:
            self.driver.get(AddEmployee_Page().url)

            #row count from the Excel file
            row = self.login_tc_03.row_count()

            #iterate the row and column data
            for row in range(2, row + 1):
                username = self.login_tc_03.read_data(row, 6)
                password = self.login_tc_03.read_data(row, 7)

                user_name = self.wait.until(
                    EC.presence_of_element_located((By.NAME, AddEmployee_Page().username_locator)))
                user_name.send_keys(username)

                pass_word = self.wait.until(
                    EC.presence_of_element_located((By.NAME, AddEmployee_Page().password_locator)))
                pass_word.send_keys(password)

                login_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, AddEmployee_Page().submit_button)))
                login_button.click()

                #validate the login and go to the dashboard
                if AddEmployee_Page().dashboard_url == self.driver.current_url:

                    print("Success : Login into Dashboard url with username {a} and password {b}".format(a=username,
                                                                                                         b=password))
                    print("Tittle od Dashboard Url", self.driver.title)

                    # Add employee details in the PIM Module
                    pim_element = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, AddEmployee_Page().pim_locator)))
                    pim_element.click()
                    add_element = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, AddEmployee_Page().add_button_locator)))
                    add_element.click()

                    # Add employee details from Excel file
                    firstname = self.login_tc_03.read_data(row, 8)
                    middle_name = self.login_tc_03.read_data(row, 9)
                    lastname = self.login_tc_03.read_data(row, 10)
                    employee_id = self.login_tc_03.read_data(row, 11)
                    username1 = self.login_tc_03.read_data(row, 12)
                    password1 = self.login_tc_03.read_data(row, 13)
                    confirm_password1 = self.login_tc_03.read_data(row, 14)

                    #Add employee details webpage locators
                    firstname_element = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, AddEmployee_Page().firstname_locator)))
                    firstname_element.send_keys(firstname)
                    middle_name_element = self.wait.until(
                        EC.presence_of_element_located((By.NAME, AddEmployee_Page().middle_name_locator)))
                    middle_name_element.send_keys(middle_name)
                    lastname_element = self.wait.until(
                        EC.presence_of_element_located((By.NAME, AddEmployee_Page().lastname_locator)))
                    lastname_element.send_keys(lastname)
                    employee_id_element = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, AddEmployee_Page().employee_id_locator)))
                    employee_id_element.send_keys(employee_id)

                    #To click the enable button
                    enable_button_element = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, AddEmployee_Page().enable_button)))
                    enable_button_element.click()

                    username_element = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, AddEmployee_Page().username_loc)))
                    username_element.send_keys(username1)
                    status_element = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, AddEmployee_Page().status_locator)))
                    status_element.click()
                    password_element = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, AddEmployee_Page().password_loc)))
                    password_element.send_keys(password1)
                    confirm_password_element = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, AddEmployee_Page().confirm_password_loc)))
                    confirm_password_element.send_keys(confirm_password1)
                    save_button_element = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, AddEmployee_Page().save_button_locator)))
                    save_button_element.click()

                    # toast message for successful adding information
                    toast_message_element = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, AddEmployee_Page().toast_message_locator)))
                    if toast_message_element.is_displayed():
                        text_message = self.wait.until(
                            EC.element_to_be_clickable((By.XPATH, AddEmployee_Page().toast_message_locator))).text
                        print("Toast Message For Successful Addition: ", text_message)
                        return text_message
                    else:
                        print("ERROR : Successfully Saved Toast Message Not Found")
                        return False



        except NoSuchElementException as e:
            print(e)

    # TestCase-04 Successful employee Update
    def update_employee(self):
        try:
            #print the current url
            print("Tittle of Dashboard Url", self.driver.title)

            # Add employee details in the PIM Module
            pim_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, AddEmployee_Page().pim_locator)))
            pim_element.click()

            #click the edit arrow pencil
            edit_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().edit_element_locator)))
            edit_element.click()
            sleep(3)
            # row count from the Excel file
            row = self.login_tc_04.row_count()

            #extract the editing datas from excel
            for row in range(2, row + 1):
                firstname = self.login_tc_04.read_data(row, 6)
                middle_name = self.login_tc_04.read_data(row, 7)
                lastname = self.login_tc_04.read_data(row, 8)
                employee_id = self.login_tc_04.read_data(row, 9)
                other_id = self.login_tc_04.read_data(row, 10)
                driver_license_no = self.login_tc_04.read_data(row, 11)
                license_exp_date = self.login_tc_04.read_data(row, 12)

                #update the data's to locating elements in webpage
                firstname_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, UpdateEmployee_Page().first_name_locator)))

                # Use ActionChains to clear the textbox
                actions = ActionChains(self.driver)
                actions.click(firstname_element).key_down(Keys.CONTROL).send_keys('a').key_up(
                    Keys.CONTROL).send_keys(
                    Keys.BACKSPACE).perform()

                # Optional: You can now perform further actions, like sending new text
                actions.send_keys(firstname).perform()

                middle_name_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, UpdateEmployee_Page().middle_name_locator)))

                # Use ActionChains to clear the textbox
                actions = ActionChains(self.driver)
                actions.click(middle_name_element).key_down(Keys.CONTROL).send_keys('a').key_up(
                    Keys.CONTROL).send_keys(
                    Keys.BACKSPACE).perform()

                # Optional: You can now perform further actions, like sending new text
                actions.send_keys(middle_name).perform()

                lastname_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, UpdateEmployee_Page().last_name_locator)))

                # Use ActionChains to clear the textbox
                actions = ActionChains(self.driver)
                actions.click(lastname_element).key_down(Keys.CONTROL).send_keys('a').key_up(
                    Keys.CONTROL).send_keys(
                    Keys.BACKSPACE).perform()

                # Optional: You can now perform further actions, like sending new text
                actions.send_keys(lastname).perform()

                employee_id_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, UpdateEmployee_Page().employee_id_locator)))

                # Use ActionChains to clear the textbox
                actions = ActionChains(self.driver)
                actions.click(employee_id_element).key_down(Keys.CONTROL).send_keys('a').key_up(
                    Keys.CONTROL).send_keys(
                    Keys.BACKSPACE).perform()

                # Optional: You can now perform further actions, like sending new text
                actions.send_keys(employee_id).perform()

                other_id_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, UpdateEmployee_Page().other_id_locator)))
                # Use ActionChains to clear the textbox
                actions = ActionChains(self.driver)
                actions.click(other_id_element).key_down(Keys.CONTROL).send_keys('a').key_up(
                    Keys.CONTROL).send_keys(
                    Keys.BACKSPACE).perform()

                # Optional: You can now perform further actions, like sending new text
                actions.send_keys(other_id).perform()

                drivers_no_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, UpdateEmployee_Page().driver_license_no_locator)))
                # Use ActionChains to clear the textbox
                actions = ActionChains(self.driver)
                actions.click(drivers_no_element).key_down(Keys.CONTROL).send_keys('a').key_up(
                    Keys.CONTROL).send_keys(
                    Keys.BACKSPACE).perform()

                # Optional: You can now perform further actions, like sending new text
                actions.send_keys(driver_license_no).perform()

                license_exp_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, UpdateEmployee_Page().license_exp_locator)))
                #license_exp_element.send_keys(license_exp_date)
                # Use ActionChains to clear the textbox
                actions = ActionChains(self.driver)
                actions.click(license_exp_element).key_down(Keys.CONTROL).send_keys('a').key_up(
                    Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

                # Optional: You can now perform further actions, like sending new text
                actions.send_keys(license_exp_date).perform()

                nationality_element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().nationality_locator)))
                #if the dropdown is invisible-# Click on the custom dropdown to open it
                nationality_element.click()

                # Select the option from the opened dropdown
                dropdown = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().nationality_dropdown_locator)))
                dropdown.click()

                marital_element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().marital_status_locator)))
                # if the dropdown is invisible-# Click on the custom dropdown to open it
                marital_element.click()

                #Select the option from the opened dropdown
                marital_dropdown = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().status_dropdown_locator)))
                #marital_dropdown.click()
                # Use JavaScript to trigger the click event on the dropdown
                self.driver.execute_script("arguments[0].click();", marital_dropdown)

                #DOB
                dob = self.login_tc_04.read_data(row, 13)
                #Test_field
                test_field = self.login_tc_04.read_data(row, 14)

                dob_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, UpdateEmployee_Page.dob_locator)))


                # Use ActionChains to clear the textbox
                actions = ActionChains(self.driver)
                actions.click(dob_element).key_down(Keys.CONTROL).send_keys('a').key_up(
                    Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

                # Optional: You can now perform further actions, like sending new text
                actions.send_keys(dob).perform()

                gender_element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().gender_locator)))
                gender_element.click()

                save_button1_element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().save_button1_locator)))
                save_button1_element.click()


                self.driver.execute_script('window.scrollBy(0, 500)')

                #Blood-Type
                blood_type_element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().blood_type_locator)))
                # if the dropdown is invisible-# Click on the custom dropdown to open it
                blood_type_element.click()
                # Select the option from the opened dropdown
                blood_dropdown = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().blood_dropdown_locator)))
                blood_dropdown.click()

                test_field_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, UpdateEmployee_Page().test_field_locator)))
                #test_field_element.send_keys(test_field)

                # Use ActionChains to clear the textbox
                actions = ActionChains(self.driver)
                actions.click(test_field_element).key_down(Keys.CONTROL).send_keys('a').key_up(
                    Keys.CONTROL).send_keys(
                    Keys.BACKSPACE).perform()

                # Optional: You can now perform further actions, like sending new text
                actions.send_keys(test_field).perform()

                save_button2_element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().save_button2_locator)))
                save_button2_element.click()

                # read the toast-message data
                toast_message2 = self.login_tc_04.read_data(row, 15)

                # toast message for successful adding information
                toast_message_element2 = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().toast_message_locator2))).text

                if toast_message2 == toast_message_element2:
                    print(
                        "Success: employee details Saved successfully and Toast message captured :{ToastMessage}".format(
                            ToastMessage=toast_message_element2))

                # toast message for successful adding information
                toast_message_element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().toast_message_locator1)))
                if toast_message_element.is_displayed():
                    text_message = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, UpdateEmployee_Page().toast_message_locator1))).text
                    print("Toast Message for Update Employee Details : ", text_message)
                    return text_message
                else:
                    print("ERROR : Successfully Updated Toast Message Not Found")
                    return False

        except NoSuchElementException as e:
            (print(e))


    #TestCase_05-Delete employee details in PIM module
    def delete_employee(self):
        try:

            # Delete employee details in the PIM Module
            pim_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, DeleteEmployee_Page().pim_locator)))
            pim_element.click()

            #delete employee in the PIM Module
            delete_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DeleteEmployee_Page().delete_locator)))
            delete_element.click()

            # alert window
            delete_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, DeleteEmployee_Page().delete_button_locator)))
            delete_button.click()

            # toast message for successful adding information
            toast_message_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, DeleteEmployee_Page().toast_message_locator)))
            if toast_message_element.is_displayed():
                text_message = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, DeleteEmployee_Page().toast_message_locator))).text
                print("Toast Message for Update Employee Details : ", text_message)
                return text_message
            else:
                print("ERROR : Successfully Deleted Toast Message Not Found")
                return False


        except NoAlertPresentException as e:
            print(e)

        self.driver.quit()

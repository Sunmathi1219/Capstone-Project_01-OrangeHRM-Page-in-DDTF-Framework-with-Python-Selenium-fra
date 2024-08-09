""""
main executable file for generating html report in Excel format for Login TestCase1
"""

from TestCases.OrangeHRM_Login_Test import OrangeHRMPage
from Locators.HomePage import OrangeHRM_Locators

import pytest

url = OrangeHRM_Locators().url
OrangeHRM = OrangeHRMPage(url)


#TestCase_01- OrangeHRM Login with valid username and password
def test_login_Testcase_01():
    assert OrangeHRM.login_Testcase_01() == True
    print("SUCCESS : Login with valid username and password successfully")


#TestCase_02- OrangeHRM Invalid Login Credential
def test_login_TestCase_01():
    assert OrangeHRM.login_Testcase_02() == True
    print("SUCCESS : Login with Invalid password and get Invalid Credential message successfully")


#TestCase_03- Adding Employee In the PIM Module
def test_add_employee():
    assert OrangeHRM.add_employee() == "Successfully Saved"
    print("SUCCESS : Employee details added in the PIM Module successfully")


#TestCase_04- Edit the Employee Details in PIM Module
def test_update_employee():
    assert OrangeHRM.update_employee() == "Successfully Updated"
    print("SUCCESS : Employee details added in the PIM Module successfully")

#TestCase_05- Delete the Employee Detail in PIM Module
def test_delete_employee():
    assert OrangeHRM.delete_employee() == "Successfully Deleted"
    print("SUCCESS : Employee details Deleted in the PIM Module successfully")

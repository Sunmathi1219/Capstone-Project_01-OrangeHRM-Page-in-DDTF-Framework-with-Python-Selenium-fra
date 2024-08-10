
##  Tittle Of Project

OrangeHRM Web Page Automation- Project1
## Table of Contents:
       About OrangeHRM
       Overview of the Project
       Project Structure
       Tools and Technologies used
       Test Case Description
       Features

## About OrangeHRM
          OrangeHRM is an open-source Human Resource Management (HRM) system designed to streamline and automate HR processes for organizations. It provides a comprehensive suite of tools to manage various HR activities, including:
1.	Employee Information Management: Maintains a detailed database of employee information, including personal details, job titles, work experience, and more.
2.	Leave Management: Facilitates the tracking and management of employee leave requests, approvals, and balances.
3.	Time and Attendance Management: Monitors employee work hours, attendance, and schedules.
4.	Performance Management: Supports performance evaluations, goal setting, and appraisals.
5.	Recruitment and Onboarding: Manages the recruitment process, from job postings to candidate tracking and onboarding.
6.	Employee Self-Service: Allows employees to access and update their personal information, submit leave requests, and view their attendance records.
7.	Reporting and Analytics: Provides various reports and analytics to help HR managers make informed decisions.
OrangeHRM is highly customizable and can be extended with additional modules to meet the specific needs of an organization. It is available in both free and paid versions, with the paid versions offering more advanced features and support.
 you can automate various tests and interactions with the OrangeHRM system, such as verifying login functionality, managing employee records, and ensuring the correct functioning of different modules.

## Overview of the Project
        This project is an automated testing suite for the OrangeHRM open-source Human Resource Management system. It utilizes Selenium WebDriver with Python in a data-driven framework to ensure comprehensive test coverage and robustness. The primary goal is to automate the functional and regression testing of the OrangeHRM system.
          This project focuses on automating test cases for the OrangeHRM web application using Selenium with Python. The automation framework is built using a Data-Driven Testing Framework (DDTF) approach, which allows for easy management and execution of test cases with varying inputs. Additionally, the project generates an HTML report after the execution of test cases to summarize the results.

## Project Structure
        The project is structured to be modular and scalable, making it easy to add or modify test cases. The key components include:
•	Test Cases: A set of automated test cases covering the core functionalities of the OrangeHRM application.
•	Data Files: External data files (e.g., CSV, Excel) are used to drive the inputs for the test cases.
•	Selenium WebDriver: Used for interacting with the web elements on the OrangeHRM application.
•	Pytest: The testing framework used to execute the test cases.
•	HTML Report: A detailed report generated after the execution of the test cases, providing a summary of the results.

## Tools and Technologies Used:
      •	Selenium WebDriver: For automating browser interactions.
      • Python: The programming language used for writing the test scripts.
      •	Pytest: The testing framework used for running the test cases.
      •	Data-Driven Testing Framework (DDTF): Utilized to separate the test data from the test scripts, making the tests more flexible and easier to maintain.
      •	Data Management: openpyxl (for Excel-based data-driven testing)
      •	HTML Report: Generated using pytest-html or a similar plugin to provide a visual summary of the test execution results.
      •	PyCharm: The integrated development environment (IDE) used for coding and managing the project.

## Test Case Description:
     This project contains the following five test cases:
TestCase-01:
Test-Objective:-
           Successful Employee Login to OrangeHRM Locator
Precondition:-
    1.	A valid user account to login to be available.
    2.	Orange HRM site is launched on a compatible browser
Steps:-
    1. In the login panel enter the username(TestData:”Admin”)
    2. Enter the password in the password field(TestData:”admin123”)
    3. Click login button
Expected Result:-
        The user is logged in successfully

TestCase-02:
Test-Objective: -
        Invalid Employee Login to OrangeHRM Portal
Precondition:-
    1. A valid user account to login to be available.
    2. Orange HRM site is launched on a compatible browser
Steps:-
    1. In the login panel enter the username (Test Data: ”Admin”)
    2. Enter the password in the password field (Test Data:
” Invalid Password”)
    3. Click login button
Expected Result: -
        A valid error message for invalid credentials is displayed


Test Cases Dealing with PIM Module

TestCase-03:
Test Objective: -
        Add a new employee in the PIM module
Precondition: -
    1. A valid user account to login to be available.
    2. Orange HRM site is launched on a compatible browser
Steps: -
   1. Go to the PIM module from the left pane in the web page
   2. Click on add and add new employee details in the page
   3. Fill in all personal details of the employee and click save
Expected Result: -
     The user should be able to add anew employee in the PIM module and should see a message for successful employee addition

TestCase-04:
Test Objective: -
        Edit an existing employee in the PIM module
Precondition: -
    1. A valid user account to login to be available.
    2. Orange HRM site is launched on a compatible browser
Steps: -
    1. Go to PIM module from the left pane in the webpage
    2. From the existing list of employees in PIM module, edit the employee information of employee and save it.
Expected Result: -
        The user should be able to edit an existing employee information in the PIM and should see a message for successful employee details addition

TestCase-05:
Test Objective: -
        Delete an existing employee in the PIM module
Precondition: -
        1.  A valid user account to login to be available.
        2. Orange HRM site is launched on a compatible browser
Steps:-
        1. Go to PIM module from the left pane in the webpage
        2. From the existing list of employees in PIM module, delete an existing employee information.
Expected Result: -
        The user should be able to delete an existing employee information in the PIM and should see a message for successful deletion

       
## Features:
      Automated testing for OrangeHRM web application.
Data-driven testing framework using Selenium with Python.
Detailed pytest HTML reports.

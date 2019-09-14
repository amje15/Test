from pages.TimesheetPage import TimesheetPage
from ddt import ddt,data,unpack
from pages.LoginPage import LoginPage
from utils.commonutils import *
import unittest
from utils.GetData import get_data
import pytest

timesheet_object=TimesheetPage()
login_object=LoginPage()
name="Adithya SH"

path='/home/adithya_sh/Desktop/selenium_testing/TaskData.csv'


@ddt

class TestTimesheets(unittest.TestCase):

    @pytest.fixture(scope='class', autouse=True)

    def login_to_page(self):
        import logging

        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.INFO)
        login_object.get_login_page()
        login_object.set_username(username)
        login_object.set_password(password)
        login_object.get_homepage()
        timesheet_object.get_timesheet_page()

    @pytest.fixture(scope='class', autouse=True)
    def teardown_test(self):
        pass




    def test_date(self):

        import datetime
        today=datetime.datetime.today().strftime('%Y-%m-%d')
       ## assert today==timesheet_object.get_datepicker_date()

    def test_username(self):

        assert name in timesheet_object.get_username()

        ##assert today in timesheet_object.get_url()


    @data(*get_data(path))
    @unpack
    def test_create_new_task(self,task_code,hrs,mins,desc,type):
        timesheet_object.set_new_task(task_code,hrs,mins,desc,type)


    def test_delete_existing_tasks(self):


        timesheet_object.delete_tasks()

        pass




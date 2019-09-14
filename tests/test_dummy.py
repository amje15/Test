from pages.TimesheetPage import TimesheetPage
from ddt import ddt,data,unpack
from pages.LoginPage import LoginPage
from utils.commonutils import *
import unittest
from utils.GetData import get_data
import pytest

path='/home/adithya_sh/Desktop/selenium_testing/TaskData.csv'

timesheet_object=TimesheetPage()
login_object=LoginPage()
name="Adithya SH"

@ddt

class TestDummy(unittest.TestCase):

    @pytest.fixture(scope='class', autouse=True)

    def login_to_page(self):
        login_object.get_login_page()
        login_object.set_username(username)
        login_object.set_password(password)
        login_object.get_homepage()
        timesheet_object.get_timesheet_page()

    @pytest.fixture(scope='class', autouse=True)
    def teardown_test(self):
        pass

        ##login_object.get_logout()



    def test_delete_existing_tasks(self):
        timesheet_object.delete_tasks()
        pass

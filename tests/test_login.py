from ddt import ddt,data,unpack
from pages.LoginPage import LoginPage
import unittest
from utils.GetData import get_data


path='/home/adithya_sh/Desktop/selenium_testing/LoginData.csv'
login_object = LoginPage()


@ddt
class TestLogin(unittest.TestCase):




    @data (*get_data(path))
    @unpack
    def test_login(self,name,pwd):

        login_object.get_login_page()
        login_object.set_username(name)
        login_object.set_password(pwd)
        login_object.get_homepage()
        login_object.get_logout()
        login_object.quit()





























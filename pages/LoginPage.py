from utils.commonutils import *
import time

d=driver


class LoginPage(object):


    def get_login_page(self):

        d.get('https://qa.hiway.hashedin.com/')
        d.implicitly_wait(10)
        d.maximize_window()
        login_button = d.find_element_by_class_name('btn-danger')
        login_button.click()

    def set_username(self,username):
        signin_textbox = d.find_element_by_class_name("whsOnd")
        signin_textbox.clear()
        signin_textbox.send_keys(username)
        d.find_element_by_class_name("RveJvd").click()
        d.implicitly_wait(3)

    def set_password(self,password):
        pwd = d.find_element_by_name("password")
        pwd.send_keys(password)
        time.sleep(3)
        d.find_element_by_class_name('RveJvd').click()

    def get_homepage(self):
        d.find_element_by_class_name('btn').click()

    def get_logout(self):
        d.find_element_by_class_name('username-position').click()
        time.sleep(3)
        d.find_element_by_xpath('//*[@id="menu_container_1"]/md-menu-content/md-menu-item/a').click()

    def quit(self):
        global d
        d.quit()
        d=driver_init()








    def get_error_message(self):
        error_message=d.find_element_by_class_name('TQGan')
        return error_message
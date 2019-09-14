from utils.commonutils import *


d=driver

import time

##Locators

TIMESHEET_BUTTON='//a[@aria-label="Timesheet"]'
DATEPICKER='//md-datepicker[@ng-model="onDate"]'
USERNAME='//h2[@class="ng-binding"]'
PROJECT_CODE='input[type="search"]'
HOURS='newEntry.hrs'
MINS='newEntry.min'
DESCRIPTION='newEntry.description'
ADD_TASK_BUTTON='/html/body/md-content/div/div/md-card/md-card-text/form/div[1]/button'
TYPE='//md-select[@ng-model="newEntry.type"]'
DELETE_BUTTONS='//md-icon[@title="Delete"]'


class TimesheetPage(object):



    def get_timesheet_page(self):
        time.sleep(3)

        d.find_element_by_xpath(TIMESHEET_BUTTON).click()

    def get_url(self):
        return d.current_url

    def get_datepicker_date(self):
        datepicker=d.find_element_by_xpath(DATEPICKER)
        date=d.execute_script(datepicker.get_attribute('ng-change'))

    def get_username(self):
        username=d.find_element_by_xpath(USERNAME)
        return username.text

    def set_new_task(self,project_code,hrs,mins,desc,type):
        d.find_element_by_css_selector(PROJECT_CODE).send_keys(project_code)
        d.find_element_by_name(HOURS).send_keys(hrs)
        d.find_element_by_name(MINS).send_keys(mins)
        d.find_element_by_name(DESCRIPTION).send_keys(desc)
        d.find_element_by_xpath(TYPE).send_keys(type)
        d.find_element_by_xpath(ADD_TASK_BUTTON).click()
        d.find_element_by_css_selector(PROJECT_CODE).clear()
        d.find_element_by_name(HOURS).clear()
        d.find_element_by_name(MINS).clear()
        d.find_element_by_name(DESCRIPTION).clear()


    def delete_tasks(self):

        d.implicitly_wait(20)
        buttons=d.find_elements_by_xpath(DELETE_BUTTONS)
        no_of_buttons=len(buttons)
        d.implicitly_wait(5)
        for i in range(no_of_buttons):
            button = d.find_element_by_xpath(DELETE_BUTTONS)
            d.implicitly_wait(5)
            button.click()
            no_of_buttons-=1












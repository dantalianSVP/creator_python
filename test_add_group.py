# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import  Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.Login(wd, username="admin", password="secret")
        self.creation_group(wd, Group(name="FTP", header="gasd", footer="qed"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.Login(wd, username="admin", password="secret")
        self.creation_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def test_add_empty_one_group(self):
        wd = self.wd
        self.Login(wd, username="admin", password="secret")
        self.creation_group(wd,Group(name="123", header="", footer=" "))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def creation_group(self, wd, group):
        self.Open_group_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        # submit group
        wd.find_element_by_name("submit").click()
        self.return_group_page(wd)

    def Open_group_page(self, wd):

        wd.find_element_by_link_text("groups").click()

    def Login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

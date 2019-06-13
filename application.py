from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    # ______Вспомогательные методы

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_group_page(self,):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def creation_group(self, group):
        wd = self.wd
        self.Open_group_page()
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
        self.return_group_page()

    def Open_group_page(self,):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def Login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self,):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()

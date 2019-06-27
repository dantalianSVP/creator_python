

class GroupHelper:


    def __init__(self, app):
        self.app = app

    def return_group_page(self,):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
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


    def delete_first_group(self):
        wd = self.app.wd
        self.Open_group_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit
        wd.find_element_by_name("delete").click()
        self.return_group_page()

    def edit_group(self, group):
        wd = self.app.wd
        self.Open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@name='edit']").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        wd.find_element_by_name("update").click()
        self.return_group_page()



    def Open_group_page(self,):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


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
        self.fill_form_group(group)
        # submit group
        wd.find_element_by_name("submit").click()
        self.return_group_page()

    def fill_form_group(self, group,):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys("%s" % text)

    def Open_group_page(self,):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def delete_first_group(self):
        wd = self.app.wd
        self.Open_group_page()
        self.select_first_group()
        #submit
        wd.find_element_by_name("delete").click()
        self.return_group_page()

    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.Open_group_page()
        self.select_first_group()
        wd.find_element_by_xpath("//input[@name='edit']").click()
        self.fill_form_group(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_group_page()





    def edit_group(self, new_group_data):
        wd = self.app.wd
        self.Open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@name='edit']").click()
        self.fill_form_group(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_group_page()


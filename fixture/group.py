from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_group_page(self, ):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.Open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_form_group(group)
        wd.find_element_by_name("submit").click()
        self.return_group_page()
        self.group_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys("%s" % text)

    def fill_form_group(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def Open_group_page(self, ):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self, ):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.Open_group_page()
        self.select_group_by_index(index)
        # submit
        wd.find_element_by_name("delete").click()
        self.return_group_page()
        self.group_cache = None

    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, ):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.Open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_xpath("//input[@name='edit']").click()
        self.fill_form_group(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.Open_group_page()
        self.select_group_by_id(id)
        # submit
        wd.find_element_by_name("delete").click()
        self.return_group_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_group(self, new_group_data):
        wd = self.app.wd
        self.Open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@name='edit']").click()
        self.fill_form_group(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.Open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.Open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

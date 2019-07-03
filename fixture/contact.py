from selenium.webdriver.support.ui import Select




class ContactHelper:

    def __init__(self, app):
        self.app = app


    def sumbit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def zapolnenie_aday(self):
        wd = self.app.wd
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("12")
        wd.find_element_by_xpath("(//option[@value='12'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("May")
        wd.find_element_by_xpath("(//option[@value='May'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2009")

    def zapolnenie_bday(self,):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        # select date of drop-list
        Select(wd.find_element_by_name("bday")).select_by_visible_text("5")
        # transfer value "5"
        wd.find_element_by_xpath("//option[@value='5']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("October")
        wd.find_element_by_xpath("//option[@value='October']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2008")

    def filling_form_to_contact(self, properties,):
        wd = self.app.wd
        self.fill_form(properties)

    def fill_form(self, properties):
        wd = self.app.wd
        self.change_field_value("firstname", properties.firstname)
        self.change_field_value("middlename", properties.middlename)
        self.change_field_value("lastname", properties.lastname)
        self.change_field_value("nickname", properties.nickname)
        self.change_field_value("title", properties.title)
        self.change_field_value("company", properties.company)
        self.change_field_value("address", properties.address)
        self.change_field_value("home", properties.home)
        self.change_field_value("mobile", properties.mobile)
        self.change_field_value("work", properties.work)
        self.change_field_value("fax", properties.fax)
        self.change_field_value("email", properties.email)
        self.change_field_value("email2", properties.email2)
        self.change_field_value("email3", properties.email3)
        self.change_field_value("homepage", properties.homepage)
        self.change_field_value("address2", properties.address2)
        self.change_field_value("phone2", properties.phone2)
        self.change_field_value("notes", properties.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys("%s" % text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.Open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.Open_home_page()

    def Open_home_page(self, ):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_all_contact(self):
        wd = self.app.wd
        self.Open_home_page()
        wd.find_element_by_xpath("//input[@id='MassCB']").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.Open_home_page()

    def edit_contact(self, properties):
        wd = self.app.wd
        self.Open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form(properties, wd)
        wd.find_element_by_name("update").click()
        self.Open_home_page()

    def open_page_for_create_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def create_cont(self, properties):
        wd = self.app.wd
        self.open_page_for_create_new_contact()
        self.filling_form_to_contact(properties)
        self.zapolnenie_bday()
        self.zapolnenie_aday()
        self.sumbit_contact()
        self.Open_home_page()

    def count(self):
        wd = self.app.wd
        self.Open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
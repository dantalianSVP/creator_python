from selenium.webdriver.support.ui import Select

from model.properties import Properties


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

    def zapolnenie_bday(self, ):
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

    def filling_form_to_contact(self, properties, ):
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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.Open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.Open_home_page()
        self.clist = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_index_for_edit(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def Open_home_page(self, ):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("Delete")) > 0:
            wd.find_element_by_link_text("home").click()

    def edit_contact_by_index(self, index, properties):
        wd = self.app.wd
        self.Open_home_page()
        self.click_edit(index)
        self.fill_form(properties)
        wd.find_element_by_name("update").click()
        self.Open_home_page()
        self.clist = None

    def edit_contact_byy_index(self, index):
        wd = self.app.wd
        self.Open_home_page()
        row = wd.find_elements_by_name("empty")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_elements_by_tag_name("a").click

    def open_page_for_create_new_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("//edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create_cont(self, properties):
        wd = self.app.wd
        self.open_page_for_create_new_contact()
        self.filling_form_to_contact(properties)
        self.zapolnenie_bday()
        self.zapolnenie_aday()
        self.sumbit_contact()
        self.Open_home_page()
        self.clist = None

    def count(self):
        wd = self.app.wd
        self.Open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    clist = None

    def get_contact_list(self):
        if self.clist is None:
            wd = self.app.wd
            self.Open_home_page()
            self.clist = []
            for element in wd.find_elements_by_xpath("//*[@name = 'entry']"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                lastname = cells[1].text
                firstname = cells[2].text
                self.clist.append(Properties(id=id, lastname=lastname, firstname=firstname,
                                             homephone=all_phones[0], mobilephone=all_phones[1],
                                             workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.clist)

    def click_edit(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Properties(firstname=firstname, lastname=lastname, id=id, homephone=homephone,
                          mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

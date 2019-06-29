from selenium import webdriver

from fixture.delcont import ModifyContact
from fixture.modifygroup import ModifyGroup
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.delcont = ModifyContact(self)
        self.modifygroup = ModifyGroup(self)




    def open_home_page(self,):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()

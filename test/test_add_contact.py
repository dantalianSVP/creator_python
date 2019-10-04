# -*- coding: utf-8 -*-
from model.properties import Properties
import pytest
import random
import string


# генерация тестовых данных
def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [
               Properties(firstname="", middlename="", lastname="",
                          nickname="", company="", address="", title="",
                          home="", mobile="", email="", work="", fax="",
                          email2="", email3="", address2="", phone2="",
                          notes="", homepage="")] + [
               Properties(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                          lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                          company=random_string("company", 10),
                          address=random_string("address", 10), title=random_string("title", 10),
                          home=random_string("home", 10), mobile=random_string("mobile", 10),
                          email=random_string("email", 10), work=random_string("work", 10),
                          fax=random_string("fax", 10),
                          email2=random_string("email2", 10), email3=random_string("email3", 10),
                          address2=random_string("address2", 10),
                          phone2=random_string("phone2", 10), notes=random_string("notes", 10),
                          homepage=random_string("homepage", 10))
               for i in range(5)
           ]

# передача данных в тест
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    for contact in testdata:
        old_clist = app.contact.get_contact_list()
        app.contact.create_cont(contact)
        app.contact.Open_home_page()
        new_clist = app.contact.get_contact_list()
        assert len(old_clist) + 1 == len(new_clist)
        old_clist.append(contact)
        assert sorted(old_clist, key=Properties.id_or_max) == sorted(new_clist, key=Properties.id_or_max)

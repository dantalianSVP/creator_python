# -*- coding: utf-8 -*-
from model.properties import Properties
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [
    Properties(firstname=firstname, middlename=middlename, lastname=lastname,
               nickname=nickname, company=company, address=address, title=title,
               home=home, mobile=mobile, email=email, work=work, fax=fax,
               email2=email2, email3=email3, address2=address2, phone2=phone2,
               notes=notes, homepage=homepage)
    for firstname in ["", random_string("firstname", 10)]
    for middlename in ["", random_string("middlename", 10)]
    for lastname in ["", random_string("lastname", 10)]
    for nickname in ["", random_string("nickname", 10)]
    for company in ["", random_string("company", 10)]
    for address in ["", random_string("address", 10)]
    for title in ["", random_string("title", 10)]
    for home in ["", random_string("home", 10)]
    for mobile in ["", random_string("mobile", 10)]
    for email in ["", random_string("email", 10)]
    for work in ["", random_string("work", 10)]
    for email2 in ["", random_string("email2", 10)]
    for email3 in ["", random_string("email3", 10)]
    for address2 in ["", random_string("address2", 10)]
    for phone2 in ["", random_string("phone2", 10)]
    for notes in ["", random_string("notes", 10)]
    for homepage in ["", random_string("homepage", 10)]
    for fax in ["", random_string("fax", 10)]

]

# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app):#, contact):
    for contact in testdata:
        old_clist = app.contact.get_contact_list()
        app.contact.create_cont(contact)
        app.contact.Open_home_page()
        new_clist = app.contact.get_contact_list()
        assert len(old_clist) + 1 == len(new_clist)
        old_clist.append(contact)
        assert sorted(old_clist, key=Properties.id_or_max) == sorted(new_clist, key=Properties.id_or_max)

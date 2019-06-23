# -*- coding: utf-8 -*-

from model.properties import Properties
from model.addition_properties import Addition


# test-case one
def test_add_contact(app):
        app.session.Login(username="admin", password="secret")
        app.contact.open_page_for_create_new_contact()
        app.contact.filling_form_to_contact(Properties(firstname="QQQ", middlename="WWW", lastname="EEE",nickname="SSS",
                                                    company="CCC",address="GGG", title="111", home="zzz",mobile="VVV",
                                                    email="TTT", work="9371992", fax="123"),
                                     Addition(email2="eee", email3="PPP",address2= "ddd",phone2="123",notes="eee"))
        app.contact.zapolnenie_bday()
        app.contact.zapolnenie_aday()
        app.contact.zapolnenie_dop_poley(Addition(address2="BAZOQUA", phone2="79996311111", notes="законы просты",
                                               email2= "spenc", email3= "ssss"))
        app.contact.sumbit_contact()
        app.session.logout()

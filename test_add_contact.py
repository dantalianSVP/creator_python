# -*- coding: utf-8 -*-

import pytest
from properties import Properties
from addition_properties import Addition
from fixture_cont import Application

@pytest.fixture
def app(request):
    fuxture = Application()
    request.addfinalizer(fuxture.destroy)
    return fuxture


# test-case one
def test_add_contact(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.open_page_for_create_new_contact()
        app.filling_form_to_contact(Properties(firstname="QQQ", middlename="WWW", lastname="EEE",nickname="SSS",
                                                    company="CCC",address="GGG", title="111", home="zzz",mobile="VVV",
                                                    email="TTT", work="9371992", fax="123"),
                                     Addition(email2="eee", email3="PPP",address2= "ddd",phone2="123",notes="eee"))
        app.zapolnenie_bday()
        app.zapolnenie_aday()
        app.zapolnenie_dop_poley(Addition(address2="BAZOQUA", phone2="79996311111", notes="законы просты",
                                               email2= "spenc", email3= "ssss"))
        app.sumbit_contact()
        app.logout()

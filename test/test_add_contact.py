# -*- coding: utf-8 -*-

from model.properties import Properties

def test_add_contact(app):
    old_clist = app.contact.get_contact_list()
    clist = Properties(firstname="QQQ", middlename="WWW", lastname="EEE",nickname="SSS",
                                                    company="CCC",address="GGG", title="111", home="zzz",mobile="VVV",
                                                    email="TTT", work="9371992", fax="123",
                                     email2="eee", email3="PPP",address2= "ddd",phone2="123",notes="eee",homepage='TATATA')
    app.contact.create_cont(clist)
    app.contact.Open_home_page()
    new_clist = app.contact.get_contact_list()
    assert len(old_clist) + 1 == len(new_clist)
    old_clist.append(clist)
    assert sorted(old_clist, key=Properties.id_or_max) == sorted(new_clist, key=Properties.id_or_max)
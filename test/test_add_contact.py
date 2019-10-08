# -*- coding: utf-8 -*-
from model.properties import Properties
import pytest


def test_add_contact(app, db, json_contacts):
        contact = json_contacts
        old_clist = db.get_contact_list()
        app.contact.create_cont(contact)
        app.contact.Open_home_page()
        new_clist = db.get_contact_list()
        assert len(old_clist) + 1 == len(new_clist)
        old_clist.append(contact)
        assert sorted(old_clist, key=Properties.id_or_max) == sorted(new_clist, key=Properties.id_or_max)

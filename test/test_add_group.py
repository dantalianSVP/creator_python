# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="FTP", header="gasd", footer="qed"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

def test_add_empty_one_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="123", header="", footer=" "))
    app.session.logout()

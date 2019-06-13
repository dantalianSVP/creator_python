# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# ____Start test case

def test_add_group(app):
    app.Login(username="admin", password="secret")
    app.creation_group(Group(name="FTP", header="gasd", footer="qed"))
    app.logout()

def test_add_empty_group(app):
    app.Login(username="admin", password="secret")
    app.creation_group(Group(name="", header="", footer=""))
    app.logout()

def test_add_empty_one_group(app):
    app.Login(username="admin", password="secret")
    app.creation_group(Group(name="123", header="", footer=" "))
    app.logout()

# ____ End test case

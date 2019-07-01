from model.group import Group


def test_edit_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.edit_group(Group(name="SLAYER", header="SLAYER", footer="SLAYER"))
    app.session.logout()



def test_delete_first_group(app):
    app.session.Login(username="admin", password="secret")
    app.modifygroup.delete_first_group()
    app.session.logout()

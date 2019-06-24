
def test_delete_contact(app):
    app.session.Login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
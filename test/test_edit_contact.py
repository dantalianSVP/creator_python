from model.properties import Properties


def test_edit_contact(app):
    app.session.Login(username="admin", password="secret")
    app.contact.edit_contact(Properties(firstname="DIMITRASH",
                                        middlename="DIO", lastname="Dmitr", nickname="DLN",
                                        company="Sccc",address="KIBA", title="PARAVOZ",home="977777",
                                        mobile="44444",email="33333", work="321", fax="3213321321"))
    app.session.logout()
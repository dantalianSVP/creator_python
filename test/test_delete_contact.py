from model.properties import Properties


def test_delete_contact(app):
    if app.group.count() == 0:
        app.contact.create_cont(Properties(firstname="QQQ", middlename="WWW", lastname="EEE",nickname="SSS",
                                                    company="CCC",address="GGG", title="111", home="zzz",mobile="VVV",
                                                    email="TTT", work="9371992", fax="123",
                                     email2="eee", email3="PPP",address2= "ddd",phone2="123",notes="eee",homepage='TATATA'))
    app.delcont.delete_first_contact()

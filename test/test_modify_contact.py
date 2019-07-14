from model.properties import Properties


def test_edit_contact(app):
    old_clist = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_cont(Properties(firstname="QQQ", middlename="WWW", lastname="EEE", nickname="SSS",
                                           company="CCC", address="GGG", title="111", home="zzz", mobile="VVV",
                                           email="TTT", work="9371992", fax="123",
                                           email2="eee", email3="PPP", address2="ddd", phone2="123", notes="eee",
                                           homepage='TATATA'))
    #app.contact.edit_contact(Properties(firstname="DIMITRASH"))
    clist = Properties(middlename="GGWP")
    clist.id = old_clist[0].id
    app.contact.edit_contact(clist)
    new_clist = app.contact.get_contact_list()
    assert old_clist == new_clist
    old_clist[0] = clist
    assert sorted(old_clist, key=Properties.id_or_max) == sorted(new_clist, key=Properties.id_or_max)
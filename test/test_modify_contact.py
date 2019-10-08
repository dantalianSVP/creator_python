import random

from model.properties import Properties

def test_edit_contact(app,db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_cont(Properties(firstname="QQQ", middlename="WWW", lastname="EEE", nickname="SSS",
                                           company="CCC", address="GGG", title="111", home="zzz", mobile="VVV",
                                           email="TTT", work="9371992", fax="123",
                                           email2="eee", email3="PPP", address2="ddd", phone2="123", notes="eee",
                                           homepage='TATATA'))
    #app.contact.edit_contact(Properties(firstname="DIMITRASH"))
    old_clist = db.get_contact_list()
    cont = random.choice(old_clist)
    inq = old_clist.index(cont)
    clist = Properties(firstname="FAFAFAFAFAFAFAFAFFAFAF")
    clist.id = old_clist[inq].id
    app.contact.edit_contact_by_id(clist.id, clist)
    new_clist = db.get_contact_list()
    assert len(old_clist) == app.contact.count()
    if check_ui:
        assert sorted(old_clist, key=Properties.id_or_max) == sorted(new_clist, key=Properties.id_or_max)
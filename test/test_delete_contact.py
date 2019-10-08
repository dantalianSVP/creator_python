import random

from model.properties import Properties


def test_delete_contact(app, db):
    if app.contact.count() == 0:
        app.contact.create_cont(Properties(firstname="QQQ", middlename="WWW", lastname="EEE", nickname="SSS",
                                           company="CCC", address="GGG", title="111", home="zzz", mobile="VVV",
                                           email="TTT", work="9371992", fax="123",
                                           email2="eee", email3="PPP", address2="ddd", phone2="123", notes="eee",
                                           homepage='TATATA'))
    old_clist = db.get_contact_list()
    contact = random.choice(old_clist)
    app.contact.delete_contact_by_id(contact.id)
    new_clist = db.get_contact_list()
    assert len(old_clist) - 1 == len(new_clist)
    old_clist.remove(contact)
    assert old_clist == new_clist

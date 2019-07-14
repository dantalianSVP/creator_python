from model.properties import Properties
from random import randrange

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create_cont(Properties(firstname="QQQ", middlename="WWW", lastname="EEE",nickname="SSS",
                                                    company="CCC",address="GGG", title="111", home="zzz",mobile="VVV",
                                                    email="TTT", work="9371992", fax="123",
                                     email2="eee", email3="PPP",address2= "ddd",phone2="123",notes="eee",homepage='TATATA'))
    old_clist = app.contact.get_contact_list()
    index = randrange(len(old_clist))
    app.contact.delete_contact_by_index(index)
    new_clist = app.contact.get_contact_list()
    assert len(old_clist) -1 == len(new_clist)
    old_clist[index:index+1] = []
    assert old_clist == new_clist


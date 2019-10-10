from model.group import Group
import random

from model.properties import Properties


def test_add_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New_group_for_test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create_cont(Properties(firstname="test"))
    id_group = random.choice(db.get_group_list()).id
    id_contact = random.choice(db.get_contact_list()).id
    app.contact.add_contact_in_group(id_contact, id_group)
# assert db.get_contact_by_id(id_contact) in orm.get_contacts_in_group(Group(id=id_group))

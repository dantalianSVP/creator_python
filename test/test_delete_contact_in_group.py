import random
from model.group import Group
from model.properties import Properties

def test_del_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create_cont(Properties(firstname="first"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_not_empty_group_list()
    if len(groups) == 0:
        group = random.choice(orm.get_group_list())
        contact = random.choice(orm.get_contacts_not_in_group(group))
        app.contact.add_contact_in_group(contact, group)
        groups = orm.get_not_empty_group_list()
        group = random.choice(groups)
        old_contacts_in_group = orm.get_contacts_in_group(group)
        contact_to_remove = random.choice(old_contacts_in_group)
        app.contact.delete_contact_from_group(contact_to_remove, group)
        old_contacts_in_group.remove(contact_to_remove)
        new_contacts_in_group = orm.get_contacts_in_group(group)
        assert sorted(old_contacts_in_group, key=Properties.id_or_max) == sorted(new_contacts_in_group,
                                                                              key=Properties.id_or_max)
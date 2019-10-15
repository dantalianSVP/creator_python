import random
from model.group import Group
from model.properties import Properties

# def test_del_contact_from_group(app, db, orm):
#     if len(db.get_contact_list()) == 0:
#         app.contact.create_cont(Properties(firstname="first"))
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="test"))
#     groups = orm.get_not_empty_group_list()
#     if len(groups) == 0:
#         group = random.choice(orm.get_group_list())
#         contact = random.choice(orm.get_contacts_not_in_group(group))
#         app.contact.add_contact_in_group(contact, group)
#         groups = orm.get_not_empty_group_list()
#         group = random.choice(groups)
#         old_contacts_in_group = orm.get_contacts_in_group(group)
#         contact_to_remove = random.choice(old_contacts_in_group)
#         app.contact.delete_contact_from_group(contact_to_remove, group)
#         old_contacts_in_group.remove(contact_to_remove)
#         new_contacts_in_group = orm.get_contacts_in_group(group)
#         assert sorted(old_contacts_in_group, key=Properties.id_or_max) == sorted(new_contacts_in_group,
#                                                                               key=Properties.id_or_max)





def test_del_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New_group_for_test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create_cont(Properties(firstname="Firstname_test"))
    id_group_list = []
    id_group_list_with_contacts = []
    groups_list = db.get_group_list()
    for group in groups_list:
        id_group_list.append(group.id)
    for id_group in id_group_list:
        if len(orm.get_contacts_in_group(Group(id=id_group))) != 0:
            id_group_list_with_contacts.append(id_group)
    if len(id_group_list_with_contacts) == 0:
        id_contact = random.choice(db.get_contact_list()).id
        id_group = random.choice(db.get_group_list()).id
        app.contact.add_contact_in_group(id_group, id_contact)
        id_group_list_with_contacts.append(id_group)
    id_group = random.choice(id_group_list_with_contacts)
    id_contact = random.choice(orm.get_contacts_in_group(Group(id=id_group))).id
    app.contact.dellete_contact_from_group(id_group, id_contact)
    assert db.get_contact_by_id(id_contact) not in orm.get_contacts_in_group(Group(id=id_group))
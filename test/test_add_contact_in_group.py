from model.group import Group
import random

from model.properties import Properties


def test_add_contact_in_group(app, db, orm, json_groups):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="FTP", header="gasd", footer="qed"))
    if len(db.get_contact_list()) == 0:
        app.contact.create_cont(Properties(firstname="test"))
    groups = db.get_group_list()
    available_groups = []
    for group in groups:
        x=orm.get_contacts_not_in_group(group)
        if len(orm.get_contacts_not_in_group(group)) != 0:
            available_groups.append(group)
    if len(available_groups) == 0:
        group = json_groups
        app.group.create(group)
        group.id = orm.get_id_of_new_group()
    else:
        group = random.choice(available_groups)
    contact = random.choice(orm.get_contacts_not_in_group(group))
    group_id = group.id
    contact_id = contact.id
    app.contact.add_contact_in_group(group_id, contact_id)
    assert orm.verify_contact_in_group(group, contact) is True

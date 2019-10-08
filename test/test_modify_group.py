import random

from model.group import Group
from random import randrange

def test_modify_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="FTP", header="gasd", footer="qed"))
    old_groups = db.get_group_list()
    grp = random.choice(old_groups)
    inq = old_groups.index(grp)
    group = Group(name="New Group")
    group.id = old_groups[inq].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[inq] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
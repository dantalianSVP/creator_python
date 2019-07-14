from model.group import Group


def test_modify_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New Group")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="PAPARIZI", header="PAPARIZI", footer="PAPARIZI"))
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
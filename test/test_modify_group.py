from model.group import Group


def test_modify_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="PAPARIZI", header="PAPARIZI", footer="PAPARIZI"))
    app.group.modify_first_group(Group(name="New Group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
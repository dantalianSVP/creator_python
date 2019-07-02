from model.group import Group


def test_edit_group(app):
    app.group.edit_group(Group(name="SLAYER", header="SLAYER", footer="SLAYER"))

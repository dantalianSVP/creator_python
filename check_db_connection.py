import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

# Создание коннекта к БД


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    test = db.get_contacts_not_in_group(Group(id="15"))
    for item in test:
        print(item)
    print(len(test))
finally:
   pass
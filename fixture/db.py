from model.group import Group
import pymysql.cursors
from model.properties import Properties


# Создали класс для конекта к БД
class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    # Метод загрузки информации о группах и о контактах из БД
    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, foorter) = row
                # помещаем объект в список
                list.append(Group(id=str(id), name=name, header=header, footer=foorter))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated = '0000-00-00 00:00:00' ")
            for row in cursor:
                (id, firstname, lastname) = row
                # помещаем объект в список
                list.append(Properties(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_by_id(self, id_in):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, middlename, nickname, company, "
                           "title, address, email, email2, email3, home, mobile, work, phone2 "
                           "FROM addressbook WHERE deprecated='0000-00-00 00:00:00' and id='%s'" % id_in)
            (id, firstname, lastname, middlename, nickname, company, title,
             address, email, email2, email3, home, mobile, work, phone2) = cursor.fetchone()
            contact_return = Properties(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename,
                                        nickname=nickname, company=company, title=title, address=address, email=email,
                                        email2=email2, email3=email3, homephone=home, mobilephone=mobile,
                                        workphone=work,
                                        secondaryphone=phone2)
        finally:
            cursor.close()
        return contact_return

    # Разрушение фикстуры (метод)
    def destroy(self):
        self.connection.close()

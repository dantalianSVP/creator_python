from model.group import Group
import pymysql.cursors


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

    # Разрушение фикстуры (метод)
    def destroy(self):
        self.connection.close()

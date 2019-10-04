
import mysql.connector

# Создали класс для конекта к БД
class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connect(host=host, database=name, user=user, password=password)

# Разрушение фикстуры (метод)
    def destroy(self):
        self.connection.close()


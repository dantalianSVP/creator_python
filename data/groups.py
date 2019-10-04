# import random
# import string
from model.group import Group

testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

# # генерация тестовых данных
# def random_string(prefix, maxlen):
#     symbol = string.ascii_letters + string.digits + " "
#     return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])
#
#
# testdata = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]


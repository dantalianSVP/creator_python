from sys import maxsize

class Properties:

    def __init__(self, firstname=None,middlename=None,lastname=None,nickname=None,company=None,address=None,home=None,
                 mobile=None,email=None,title=None,work=None,fax=None,address2=None, phone2=None,notes=None,email2=None,email3=None,homepage=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.email = email
        self.title = title
        self.work = work
        self.fax = fax
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.id = id



    def __repr__(self):
           return "%s:%s%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


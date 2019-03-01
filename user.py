from dataSource import DataSource
import string
import random

class User:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.uname = ""
        self.email = ""
        self.password = ""
        self.dataSource = DataSource()
    
    def createUser(self):
        try:
            self.fname = self.dataSource.getRandomFirstName()
            self.lname = self.dataSource.getRandomLastName()
            self.uname = f"{self.fname}.{self.lname}.{self.idGenerator()}"
            self.email = f"{self.uname}@gmail.com"
            self.password = self.idGenerator(10)
        except:
            return False
        return True

    def getUser(self):
        return self

    def printUserData(self):
        print(f"""=
Full name: {self.fname} {self.lname}
Username: {self.uname}
Email: {self.email}
Password: {self.password}
=
""")

    def saveUser(self, fileName = 'createduser.csv'):
        csvRow = f"{self.fname},{self.lname},{self.uname},{self.email},{self.password}\n"
        with open('createdUsers.csv','a') as f:
            f.write(csvRow)
        print(f"saved user {self.uname}")

    def idGenerator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


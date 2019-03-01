# steps to follow
# import datasoure
from dataSource import DataSource as DataSource
#import user
from user import User as User

# create a datasource
# the file should be in format firstname,lastname
# eg: 
fileName = 'names.csv'
data = DataSource(fileName)

# you can get all the first names generated
names = data.getFirstNames()
print(names)

# you can get all the first names generated
names = data.getLastNames()
print(names)

# you can get a random first name
name = data.getRandomFirstName()
print(name)

# you can get a random last name
name = data.getRandomLastName()
print(name)

# create a user object
user = User()

# create a new user which returns a boolean
if(user.createUser()):
# and then save it
    user.saveUser('createdUser.csv')

# get the user details
userObj = user.getUser()

# print the user details
userObj.printUserData()
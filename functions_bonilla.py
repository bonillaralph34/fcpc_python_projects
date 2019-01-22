#default value
def who(x = 10, y = 50, z = 30):
    print(x+y+z)

who()

#explicit assignment of parameters
def who(x, y = 50, z = 30):
    print(x+y+z)

who(10)

#explicit assignment of parameters
def who(x,y,z):
    print(x+y+z)

who(10,50,30)

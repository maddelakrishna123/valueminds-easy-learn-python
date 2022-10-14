import sys

"""

This script is used to demonstrate the various data types of python
how to read the data from user

how to read as commandLine arguments
"""
# myData = 45;

# myData = 3.4;
# myData = 'Python Demo'
# myData = True;
# myData = bool(1)
# myData = [1 , 2]
# myData = {1 , 2}
# myData = (1 ,2)
# myData = {"id":101,"name":"krishna kumar"}
# print(myData)
# print(type(myData))

# Reading Data from User
# x = input('Enter  Data')
# print(x);
# x,y = input('Enter two Data elements').split();
# x,y =[int(a) for  a in input('Enter two Numbers').split()]
# print("{} + {} = {} ".format(x,y,(x+y)))

arguments = sys.argv
print(len(arguments))

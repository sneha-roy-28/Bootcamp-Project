
import hashlib
my_string=input("Enter your string : ")

#using sha1 algorithm
my_string2=hashlib.sha1(my_string.encode())
print(my_string2)

#using sha256 algorithm
my_string3=hashlib.sha256(my_string.encode())
print(my_string3)

#using shake_256 algorithm
my_string4=hashlib.shake_256(my_string.encode())
print(my_string4)


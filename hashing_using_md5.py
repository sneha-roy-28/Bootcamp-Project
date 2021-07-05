
import hashlib
my_string=input("Enter your string : ")
# encoding my_string using encode()
# then sending to md5()
my_string2=hashlib.md5(my_string.encode())
print(my_string2)

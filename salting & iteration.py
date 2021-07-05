
import hashlib
#initialize salting in string data type
my_string="a12345b"
#create iterations
for i in range(5) :
    my_string2=hashlib.md5(my_string.encode())
#print the final result
print(my_string2)    
    
    
    


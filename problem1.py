##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
username = ""
count = 0
while True:
    print(count)
    if count > 9:
        print("Too many failed attempts. Access Denied")
        break
    username = str(input("Enter username:"))
    wabungus = str(input("Enter password:"))
    if username != "admin" and  wabungus != "12345":
        print("Access Denied")
        count = count + 1
    if username != "admin":
        print("Access Denied")
        count = count + 1
    if wabungus != "12345":
        print("Access Denied")
        count = count + 1
    else:
        print("Access granted")
        break    

            
        
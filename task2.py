#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
Remember to use input().strip() to input str type variables
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""

username = ""
while True:
    username = str(input("Enter username:"))
    if username != "admin":
        print("Access Denied")
    else:
        break
while True:
    wabungus = str(input("Enter password:"))
    if wabungus != "12345":
        print("Access denied")
    else:
        break
print("Access granted")

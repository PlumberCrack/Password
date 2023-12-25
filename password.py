import random
char = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()]}_+-={[]|:;<>,.?/")
#Create random passowrd
password_length = 25 
password = ''.join(random.choice(char) for _ in range(password_length))
#Retrun output 
print(f"Your new password is: {password}")
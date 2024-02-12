#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PASSWORD GENERATOR

#A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.

#User Input: Prompt the user to specify the desired length of the password.

#Generate Password: Use a combination of random characters to generate a password of the specified length.

#Display the Password: Print the generated password on the screen.

import string
import random

#take a password length from user

password_length=int(input("Enter Length of the Password"))

print('Choose a character set for password from these:\n1. Digits\n2. Letters\n3. Special Characters\n4. Exit')

characterList=""

while(True):
    choice=int(input("Pick a number"))
    
    if(choice==1):
        characterList +=string.ascii_letters
    
    elif(choice==2):
        characterList +=string.digits
        
    elif(choice==3):
        characterList +=string.punctuation
        
    elif(choice==4):
        break
        
    else:
        print("Please pick a valid Character Set Option!!!")
        
password=[]

for i in range(password_length):
    randomcharacter=random.choice(characterList)
    
    password.append(randomcharacter)
    
print("The random password is: "+ "".join(password))


# In[9]:


#PASSWORD GENERATOR

#A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.

#User Input: Prompt the user to specify the desired length of the password.

#Generate Password: Use a combination of random characters to generate a password of the specified length.

#Display the Password: Print the generated password on the screen.

import string
import random

#take a password length from user

password_length=int(input("Enter Length of the Password"))

# store all characters in lists 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

#for a strong password, length should be minimum 8 characters

while True:
 
    try:
 
        characters_number = int(password_length)
 
        if characters_number < 8:
 
            print("Your number should be at least 8.")
 
            user_input = input("Please, Enter your number again: ")
 
        else:
 
            break
 
    except:
 
        print("Please, Enter numbers only.")
 
        password_length = input("How many characters do you want in your password? ")
    
# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# calculate 30% & 20% of number of characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))
 
 
# generation of the password (60% letters and 40% digits & punctuations)
result = []
 
for x in range(part1):
 
    result.append(s1[x])
    result.append(s2[x])
 
for x in range(part2):
 
    result.append(s3[x])
    result.append(s4[x])
 
 
# shuffle result
random.shuffle(result)
 
 
# join result
password = "".join(result)
print("Strong Password: ", password)


# In[ ]:





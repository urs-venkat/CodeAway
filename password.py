#importing random library

import random

#making lists  for generating paswords from it

#Alphabets list

alpha_list=list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")

#Numbers list

nums_list=list("1234567890")

#Symbols list

symb_list=list("!@#$%^%*")

#taking input of size of password

pass_size=int(input("Enter size of the password\n"))

#Taking input of number of alphabets in the password

no_of_alphabets=int(input("Enter how many no of alphabets do you want in your password:\n"))


#Taking input of number of Integers in the password

no_of_intergers=int(input("Enter how many no of integers do you want in your password:\n"))

#Taking input of no of symbols to be in password

no_of_symbols=int(input("Enter how many no of symbols do you want in your password:\n"))


#Creating empty list for appending random charactors from above lists

new_list=[]

#for loop for random charactors from alphaphets lists

for i in range(no_of_alphabets):
     new_list.append(random.choice(alpha_list))

#for loop for random charactors from integers lists

for i in range(no_of_intergers):
     new_list.append(random.choice(nums_list))

#for loop for random charactors from symbols lists

for i in range(no_of_intergers):
     new_list.append(random.choice(symb_list))

#Shuffling the new_list
     
random.shuffle(new_list)

#displaying the generated password

print("Your Generated Password is","".join(new_list))




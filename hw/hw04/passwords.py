#Get the input
first_name = input("Welcome to the username and password generator!\n\
Please enter your first name: ")
last_name = input("Please enter your last name: ")
favorite_word = input("Please enter your favorite word: ")
print()
first_name = first_name.lower()
last_name = last_name.lower()

#Make the user name
#The username generated by your program should consist of the first letter
#from the user's first name, followed by the first seven letters from their last name,
#and a random integer between 0 and 99. The letters in the username should all be lower case,
#and you should add * (asterisk) characters as necessary if the last name is shorter than 
#seven characters. (Hint: Add some extra * 's (asterisks) to the last name before you select
#the seven-character piece, whether you need them or not.) For full credit, your solution 
#must build a single string containing all of these characters and then print it, 
#rather than just printing each piece separately. You should also be polite and 
#personalize the response by including the user's first name, as shown above.
import random
last_name_asterisk = last_name
random_number_one = str(random.randint(0,100))
if len(last_name) < 7:
     for i in range (7 - len(last_name)):
          last_name_asterisk += '*'
user_name = first_name[0] + last_name_asterisk + random_number_one
print(f"Thanks {first_name}, your user name is {user_name}\n")

#Make the password1
#The username generated by your program should consist of the first 
# letter from the user's first name, followed by the first seven letters 
# from their last name, and a random integer between 0 and 99. The letters 
# in the username should all be lower case, and you should add * (asterisk) 
# characters as necessary if the last name is shorter than seven characters. 
print("Here are three suggested passwords for you to consider:\n")
random_number_two = str(random.randint(10,100))
first_name_one = first_name.replace('a','@').replace('o', '0').replace('l', '1').replace('s', '$')
last_name_one = last_name.replace('a','@').replace('o', '0').replace('l', '1').replace('s', '$')
password_one = first_name_one + random_number_two + last_name_one
print(f"Password 1: {password_one}")

#Make the password2
#The second password is an "acronym", consisting of the first and last character from 
# the user's first name, the first and last character of their last name, and the first 
# and last letter of their favorite word. In each case, the first letter of the pair should 
# be lower case and the second should be upper case.
password_two = user_name[0] + (user_name[-1]).upper() + last_name[0]\
+ (last_name[-1]).upper() + favorite_word[0] + (favorite_word[-1]).upper()
print(f"Password 2: {password_two}")

#Make the password3
#The third password takes a random-length portion of the first name, 
# combined with random-length portions of the favorite word and last name (in any order).
#  In each case, those random-length pieces should start at the beginning of the string,
#  and the code should be written such that it's possible to get the entire string 
# if the largest possible random number is produced. At least one character from each part 
# (first name, last name, and favorite word) should appear in the password.
password_three = first_name[:random.randint(1,len(first_name))] +\
last_name[:random.randint(1,len(last_name))] +\
favorite_word[:random.randint(1,len(favorite_word))]
print(f"Password 3: {password_three}")

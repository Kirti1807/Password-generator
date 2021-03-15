# This is a strong password generator code with minimum password length 8

import random
l = random.randint(8,32)
special = ['~','!','@','#','$','%','&','*','<','>','?','/','|']

lower =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

upper =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number =['0','1','2','3','4','5','6','7','8','9']

total = special + lower + upper + number
# atleast one character of all type
p = random.choice(special) +random.choice(lower) +random.choice(upper) +random.choice(number) 
for i in range (l-4):
    a = random.choice(total)
    p = p + a
print(p)

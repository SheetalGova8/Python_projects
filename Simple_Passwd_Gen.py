import random

uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter = uppercase_letter.lower()
digits = "0123456789"
symbols = "()[]{},:.-_/\\?+*#"

upper,lower,num,syms = True,True,True, True

all=""

if upper:
    all += uppercase_letter
if lower:
    all += lowercase_letter
if num:
    all += digits
if syms:
    all += symbols
    
length = 20
amount = 20

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
    
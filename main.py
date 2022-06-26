import random
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFHJKLZXCVBNM"
NUMBER = "0123456789"
Symbol = "[]{}#()*;._-"

all=lower + upper + NUMBER + Symbol
lenght = 9
password = "".join(random.sample(all,lenght))
print(" The Password You Generated Is :",password)

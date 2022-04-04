user_input = str(input("Welcome to my Abbreviation Generator :) Enter your word(s) : "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
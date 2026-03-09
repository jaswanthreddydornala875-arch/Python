str1=input("Enter a word/sentance:")
str2="" #null string to add the updated string
for i in str1:
    if i in "qwertyuiopasdfghjklzxcvbnm": #to check for the letter is small/not
        str2+=i.upper() # .upper() function to convert to upper case
    else:
        str2+=i
print(str2)
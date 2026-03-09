str1=input("Enter a word/sentance:")
char=input("Enter a letter to remove:")
str2=""
for i in str1:
    if char!=i: # adding letter if it is required
        str2+=i
print(str2)
        
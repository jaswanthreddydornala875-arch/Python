str1=input("Enter a word/sentance:")
Char=input("Enter a letter:")
count=0
for i in str1:
    if Char==i:
        count+=1
print(count)
str1=input("Enter a word:")
str2=str1[::-1] # This will reverse a string and it is assigned to 2nd string
if(str1==str2):
    print("Palindrome")
else:
    print("Not a Palindrome")
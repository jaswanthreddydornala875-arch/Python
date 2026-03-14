user_input=map(int,input("Enter numbers with space:").split())
user_list=list(user_input)
user_list2=[]
for i in user_list:
    if i not in user_list2:
        user_list2.append(i)
print(user_list2)
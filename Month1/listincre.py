#User input
User_input=map(int,input("Enter numbers with space").split())
User_list=list(User_input)
# (init,stop,step)
for i in range(len(User_list)):
    for j in range(len(User_list)):
            if(User_list[i]<User_list[j]):
                c=User_list[i]
                User_list[i]=User_list[j]
                User_list[j]=c
print(User_list)


import random

rps=["rock","paper","scissor"]

select_input_by_user=input("select rock for type 0 or select paper for type 1 or select scissor for type 2\n")
select_input_by_user=int(select_input_by_user)
select_input_by_computer =random.randint(0,2)
print(f"You select \n {rps[select_input_by_user]} \nComputer select \n{rps[select_input_by_computer]}")
if select_input_by_user == select_input_by_computer:
    print("draw")
elif select_input_by_user=="0" and select_input_by_computer=="1":
    print("you lose")
elif select_input_by_user==1 and select_input_by_computer==0:
    print("you wine")
elif select_input_by_user==1 and select_input_by_computer==2:
    print("you lose")
elif select_input_by_user==2 and select_input_by_computer==1:
    print("you win")
elif select_input_by_user==2 and select_input_by_computer==0:
    print("you lose")
elif select_input_by_user==0 and select_input_by_computer==2:
    print("you win")
else:
    print("invalid input")

# list_of_friends = ['logno','toha','symun','noman']
#
# print(len(list_of_friends))
# print(list_of_friends[random.randint(0,3)])
# sates_of_bangladesh=["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh","Sylhet"]
#
# sates_of_bangladesh.append("feni")
# sates_of_bangladesh.extend(['toha','logno'])
#
# print(sates_of_bangladesh)





import days_4_my_module
# print(random.randint(1, 100))
# print(days_4_my_module.this_is_pi_value)

# heads_or_tails=random.randint(1,2)
# print(had_or_tail)

# if heads_or_tails==1:
#     print('head')
# elif heads_or_tails==2:
#     print('tail')
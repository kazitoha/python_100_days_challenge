
# day3


print('''            ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\sss/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""` ''')

print('Welcome to this Treasure Island')
print('your mission is find a treasure island and you are at your goal.')
start_or_not= input('start the game ? (y or n)\n')
if start_or_not.lower() == 'y':

    left_or_write=input("Insert left or right? (l or r)\n")

    if left_or_write=='l':
        swim_or_wait=input('swim or wait ? (s or w) \n')
        if swim_or_wait.lower()=='s':
            print('You lose!')
        elif swim_or_wait.lower()=='w':
            which_door=input('Which door red or blue? (r or b)\n)')
            if which_door.lower()=='r':
                print('You lose!')
            elif which_door.lower()=='b':
                print('''You win!
                
                
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\s||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\s/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
                
                
                ''')
            else:
                print('invalid input!')
        else:
            print('invalid input!')
    elif left_or_write=='r':
        print("Game Over")
    else:
        print('invalid input!')
else:
    print("get out from here")

# print("welcome to pizza store")
# size=input("enter the size of your pizza (S,M or L):  \n")
# pepperoni = input("enter the pepperoni of your pizza  (Y or N):  \n")
# extra_cheese = input("enter the extra cheese of your pizza (Y or N):  \n")
# bill=0
#
# if size == "S" or size =="s":
#     bill=15
#     print("your select small size pizza")
#     if pepperoni == "Y" or pepperoni == "y":
#         bill += 2
#         print("your select pepperoni")
#     if extra_cheese == "Y" or extra_cheese == "y":
#         bill += 1
#         print("your select extra cheese")
#     print(f"Your bill is {bill}")
# elif size == "M" or size =="m":
#     bill=20
#     print("your select medium size pizza")
#     if pepperoni == "Y" or pepperoni == "y":
#         bill += 3
#         print("your select pepperoni")
#     if extra_cheese == "Y" or extra_cheese == "y":
#         bill += 1
#         print("your select extra cheese")
#     print(f"Your bill is {bill}")
# elif size == "L" or size =="l":
#     bill=25
#     print("your select large size pizza")
#     if pepperoni == "Y" or pepperoni == "y":
#         bill += 3
#         print("your select pepperoni")
#     if extra_cheese == "Y" or extra_cheese == "y":
#         bill += 1
#         print("your select extra cheese")
#     print(f"Your bill is {bill}")
# else:
#     bill=0
#     print("unvalid input")
#
#




# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
#
# if bmi < 18.5:
#     print("underweight")
# elif bmi >= 18.5 and bmi < 25:
#     print("normal weight")
# elif bmi >= 25:
#     print("overweight")

# 🚨 Do not modify the values above
# Write your code below 👇
# numbers=int(input("enter a rendom number\n"))
# if numbers % 2 == 0:
#     print('this is even number')
# else:
#     print('this is odd number')

# height=int(input("enter your height in cm: "))
# if height >= 120:
#     print("You can ride rollercoster")
# else:
#     print("You can't ride rollercoster")


# days 2

# total_bill=int(input("Enter your total bill\n"))
# total_tip_persentage=int(input("Enter tipp percentage\n"))
# how_many=int(input('How many pepole with you\n'))
#
# total_amount_per_person=(((total_bill/100) * total_tip_persentage ) + total_bill)/how_many
# # get_pasentage_of_tipp= total_bill/100 * total_tip_persentage
# # bill_with_tipp =total_bill + get_pasentage_of_tipp
# # final_bill=bill_with_tipp/how_many
# round_it=round(total_amount_per_person,2)
# print(f"Total bill per person {round_it}")


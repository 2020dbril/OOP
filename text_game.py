user_name=input('what is your name?')
#the user input of all the names of the crew members in the game
print(user_name, "You have been selected to fly to mars")
crew_1 =input("Enter 1 crew member's name and hit enter")
crew_2 =input("Enter the second crew member's name and hit enter")
crew_3 =input("Enter the third crew member's name and hit enter")
crew_4 =input("Enter the fourth member's name and hit enter")
crew_5 =input("Enter the fifth member's name and hit enter")
#This is the decision of what the spend money on
print('you have to carefully choose what you spend on food, fuel and on upgrading your rocket, choose wisely')
#where the data is stored
food_array=[]
fuel_amount=[]
ship_protection=[]

class money():

    def money_distribution():
        print('you are given 1 million $, how much will you spend on everything? Recommended:690,000 on ship, 10,000 on food and 300,000 on fuel')
        food_price = int(input("enter the amount you want to spend on food"))
        fuel_amount = int(input("enter the amount you want to spend on fuel"))
        ship_protection = int(input("enter the amount you want to spend on ship protection"))
        if food_price+fuel_amount+ship_protection >= 1000000:
            print("your smart finess the system")
#depending on your decision you die or you live
        return food_price, fuel_amount, ship_protection
food_price, fuel_amount, ship_protection = money_distribution()
#icecream defined out the function for later use
icecream = 0

class food():


    def food_store(food_price):
        print("you can choose from the following foods: 1 bag of potato $3,1 bag of dried meat $5, ,1 bag of icecream $1, 1 bag of beans + rice $3 and 1 bag of dried mango $2")
        print("consuming different foods have different health benefits necessary further in the game")
        amount_potatoes=int(input("how many bags of potatoes?"))
        food_array.append(amount_potatoes)
        food_price=food_price - amount_potatoes*3
        bag_of_meat=int(input("how many bags of dried meat?"))
        food_array.append(bag_of_meat)
        food_price=food_price - bag_of_meat*5
        #global allows icecream to be referred to outside the function
        global icecream
        icecream=int(input("how many tubs of icecream"))
        food_array.append(icecream)
        food_price=food_price-icecream*1
        beansnrice=int(input("how many bags of beans and rice?"))
        food_array.append(beansnrice)
        food_price=food_price-beansnrice*3
        dried_mango=int(input("how many bags of dried mango"))
        food_price=food_price-dried_mango*2
        food_array.append(dried_mango)
        print(food_array)
food_store(food_price)

def conflict(icecream):
    print("a deadly alien is eating an unknown amount of the food supply, do you try kill the alien or let it be?")
    action=input('')
    if action == ("kill the alien"):
        print("the alien is too strong, you die")
    if action == ("let it be"):
        print("the alien ate all your icecream and died from eating too much")
        food_array.remove(icecream)
    print(food_array)
conflict(icecream)

import random
class Astro():

    def __init__(self, hp, name):
        self.hp = hp
        self.name = name

    def battle(self, other):
        print(self.name, 'is in a fight with ',other.name)
        #get user input for an attack
        pick_attack = input('what attack? shoot or punch')

        if pick_attack == 'shoot':
            attack = random.randint(0,25)
        else:
            attack = random.randint(0,50)

        other.hp = other.hp - attack
        print(self.name,'did', attack,'damage to', other.name)
        print(other.name,'has', other.hp,'health left\n')

        if other.hp >0:
            return(other.battle(self))
        else:
            print(self.name,'won')

crew_2 = Astro(100,crew_2)
Alien = Astro(100,'Alien')
crew_2.battle(Alien)

import random

user_name = input("Enter your Number: ")
print("Thank you!!! Mr."+user_name)

somefruit = '''apple apricot berry banana cherry muskmelon lemon orange strawberry blueberry respberry mango gauva'''

fruit = somefruit.split(' ')

randomFruit = random.choice(fruit)
print(randomFruit)

for i in randomFruit:
    print()
    print("_",end=" ")
    print("\n")

fruitChance = len(randomFruit)+1

while fruitChance != 0:
    try:
        guess_fruit = input("Enter your guessing fruit: ")
    except:
        print("Enter fruit name: ")
        continue    
    if guess_fruit == randomFruit:
        print("Congratualation!!! Mr."+user_name+" You Win")
        break
    else:
        fruitChance -= 1
        print("you have only ",fruitChance," chance for you !!!")
if fruitChance == 0:
    print("You Loose Mr."+user_name+" Better Luck Nexttime!!!")       

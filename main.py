name =input("What is your name? ")
place =input("Give me a place. ")
animal =input("Give me an animal. ")
fruit =input("Give me an a fruit. ")
verb =input("Give me a verb. ")
number = int(input("Give me a number. "))
total_fruit = number * 2

print(f""" One day, a boy named {name} went to the {place} and saw a {animal}. He was holding a {fruit}. The {animal} snatched the {fruit} and started {verb}. """)

again =input("Do you want to play again? (yes or no)").lower().strip()
while again == "yes":
    name =input("What is your name? ")
    place =input("Give me a place. ")
    animal =input("Give me an animal. ")
    fruit =input("Give me an a fruit. ")
    verb =input("Give me a verb. ")
    number = int(input("Give me a number. "))
    total_fruit = number * 2
    
    print(f""" In August holiday, {name} went  to {place} by a {animal}. In the middle of the way, the {animal} started to get tired. As soon they were of the road, the {animal} started {verb}. """)

while again == "yes":
    name =input("What is your name? ")
    place =input("Give me a place. ")
    animal =input("Give me an animal. ")
    fruit =input("Give me an a fruit. ")
    verb =input("Give me a verb. ")
    number = int(input("Give me a number. "))
    total_fruit = number * 2

    print(f""" One day, {name} went to the market to buy {number} {fruit}. On the way he kicked a {animal}. The {animal} chased him until he was tired. The {animal} bit his leg hard it left while its mouth was bloody. """)

    print("Thank you for playing. ")
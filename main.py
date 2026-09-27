name =input("What is your name? ")
place =input("Give me a place. ")
animal =input("Give me an animal. ")
fruit =input("Give me a fruit. ")
verb =input("Give me a verb. ")
number = int(input("Give me a number. "))
total_fruits = number * 2
story1 = f""" One day, a boy named {name} went to {place} and saw a {animal}. He was holding {total_fruits} {fruit}. The {animal} snatched the {fruit} and started {verb}. """
story2 = f""" One day, {name} went to the market to buy {total_fruits} {fruit}. On the way he kicked a {animal}. The {animal} chased him until he was tired. The {animal} bit his leg hard it left while its mouth was bloody. """
story3 = f""" In August holiday, {name} went  to {place} by a {animal}. In the middle of the way, the {animal} started to get tired. As soon they were of the road, the {animal} started {verb}. """

choice =int(input("Choose a story? (1, 2 or 3)"))

if choice == 1:
    print(story1)
elif choice == 2:
    print(story2)
else:
    print(story3)

again =input("Do you want to play again? (yes/no)").lower().strip()

while again == "yes":

    name =input("What is your name ?")
    place =input("Give me a place . ")
    animal =input("Give me an animal . ")
    fruit =input("Give me a fruit . ")
    verb =input("Give me a verb . ")
    number = int(input("Give me a number . "))
    total_fruits = number * 2
    story1 = f""" One day, a boy named {name} went to {place} and saw a {animal}. He was holding {total_fruits} {fruit}. The {animal} snatched the {fruit} and started {verb}. """
    story2 = f""" One day, {name} went to the market to buy {total_fruits} {fruit}. On the way he kicked a {animal}. The {animal} chased him until he was tired. The {animal} bit his leg hard it left while its mouth was bloody. """
    story3 = f""" In August holiday, {name} went  to {place} by a {animal}. In the middle of the way, the {animal} started to get tired. As soon they were of the road, the {animal} started {verb}. """

    choice =int(input("Choose a story? (1, 2 or 3)"))

    if choice == 1:
        print(story1)
    elif choice == 2:
        print(story2)
    else:
        print(story3)

    again =input("Do you want to play again? (yes/no)").lower().strip()
print("Thank you for playing. ")
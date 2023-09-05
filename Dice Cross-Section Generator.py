import random
ans = int(input("1) Generate a random dice.\n2) Generate a dice with given top.\nEnter your choice: "))

if ans==1:
    dice_list = [1,2,3,4,5,6]
    x = random.choice(dice_list)
    dice_list.remove(x)
    dice_list.remove(7-x)
    y = random.choice(dice_list)
    dice_list.remove(y)
    dice_list.remove(7-y)
    z = random.choice(dice_list)
    dice_list.remove(z)
    dice_list.remove(7-z)
    print("Generated Dice:")
    print("    _____")
    print(f"____|_{z}_|________")
    print(f"|_{x}_|_{y}_|_{7-x}_|_{7-y}_|")
    print(f"    |_{7-z}_|")
elif ans==2:
    dice_list = [1,2,3,4,5,6]
    top = int(input("Enter the value to display on top of dice: "))
    dice_list.remove(top)
    dice_list.remove(7-top)
    y = random.choice(dice_list)
    dice_list.remove(y)
    dice_list.remove(7-y)
    z = random.choice(dice_list)
    dice_list.remove(z)
    dice_list.remove(7-z)
    print("Generated Dice: ")
    print("    ____")
    print(f"____|_{z}_|________")
    print(f"|_{y}_|_{top}_|_{7-y}_|_{7-top}_|")
    print(f"    |_{7-z}_|")
else:
    print("Please enter a valid input.")
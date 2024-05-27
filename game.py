from requiredImports import *
from requiredFunctionModules import *

# from mods.modLoader import loadallmods
# loadallmods()
# time.sleep(1)

os.system("cls")
player = readFile(playerdata)

if not player:
    print("Hello this is an rpg for DGT!")
    print("Please enter a username!")
    username = input("> ")
    os.system("cls")
    player["username"] = username
    player["weapon"] = {"displayName": "Rusty Blade", "id": 1, "damage": 1, "nextUpgradeCost": 10}
    player["armour"] = {"displayName": "Leather Armour", "id": 1, "protection": 1, "nextUpgradeCost": 10}
    player["skills"] = [{"skillDisplayName": "TEMP", "id": 1, "skillLevel": 1}]
    player["gold"] = 0
    print("Welcome " + username)
    time.sleep(2)
    os.system("cls")
    firstPlay = True

    save(player)
else:
    firstPlay = False
    print("Welcome back " + player["username"])
    time.sleep(2)


while True:
    os.system("cls")
    if firstPlay:
        print("This appears to be your first time playing this game!")
        tutorialConfirm = input("Would you like to play a tutorial? (y/n): ").lower()
        if tutorialConfirm == "y":
            os.system("cls")
            print("Welcome to the tutorial!")
            time.sleep(2)
            print("Your goal is to have fun... and dont die to death!")
            time.sleep(4)
            os.system("cls")
            print("For real, your goal is to become as strong as possible and earn as much gold as possible")
            time.sleep(4)
            os.system("cls")
            print("You can fight enemies and buy new items to help you fight!")
            print("")
            print("And while buying new items you can also train your character!")
            time.sleep(10)
            print("Have fun!")
            time.sleep(2)
            os.system("cls")
            print("Dont die or else :)")
            time.sleep(0.2)
            firstPlay = False
            continue
        elif tutorialConfirm == "n":
            firstPlay = False
            continue
        else:
            os.system("cls")
            print("!!! Please enter y or n !!!")
            time.sleep(2)
            continue
    print("Inventory")
    print("Fight")
    print("Shop")
    print("Exit")
    print("")
    print("What do you want to do?")
    choice = input("> ").lower()

    player = readFile(playerdata)

    if choice == "inventory":
        inventory(player)
    elif choice == "fight":
        fight(player)
        continue
    elif choice == "shop":
        shop(player)
        continue
    elif choice == "r":
        # This option is temporary to speed up the development process
        continue
    elif choice == "exit":
        os.system("cls")
        save(player)
        print("See you next time!")
        time.sleep(2)
        os.system("cls")
        break
    else:
        os.system("cls")
        print(choice, "is not a valid option!")
        time.sleep(2)
        continue

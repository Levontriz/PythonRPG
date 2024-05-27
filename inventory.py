from requiredImports import *


def inventory(player):
    while True:
        os.system("cls")
        print(f"Your current gold is {player["gold"]} \n")
        print("Weapon")
        print("Armour")
        print("Exit")
        print("\nPlease select an inventory menu")
        inventoryOption = str(input("> ").lower())
        os.system("cls")
        if inventoryOption == "weapon":
            weapon = player["weapon"]
            print(f"Your current weapon is the {weapon["displayName"]} and it does {weapon["damage"]} damage \n")
            print("Press enter to continue...")
            input()
            break
        elif inventoryOption == "armour":
            armour = player["armour"]
            print(f"Your current armour is the {armour['displayName']} and it has {armour['protection']} protection \n")
            print("Press enter to continue...")
            input()
            break
        elif inventoryOption == "exit":
            break
        else:
            print("Invalid option please select out of the available options!")
            time.sleep(2)
            continue

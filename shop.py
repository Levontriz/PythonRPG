from requiredImports import *


def shop(player):
    while True:
        os.system("cls")
        print("Weapon")
        print("Armour")
        print("\nWhat item do you want to upgrade?")
        upgradeSelected = str(input("> ").lower())

        if upgradeSelected == "weapon":
            while True:
                os.system("cls")
                weaponCostUpgrade = player["weapon"]["nextUpgradeCost"]
                print(f"The upgrade cost for your weapon is {weaponCostUpgrade} gold")
                print("\nDo you want to continue with the upgrade? (Y/N)")
                continueUpgrade = str(input("> ").lower())

                if continueUpgrade == "y":
                    os.system("cls")
                    if (player["gold"] - weaponCostUpgrade) >= 0:
                        player["gold"] -= weaponCostUpgrade
                        player["weapon"]["nextUpgradeCost"] = round(player["weapon"]["nextUpgradeCost"] * 1.60)
                        player["weapon"]["id"] += 1
                        player["weapon"]["displayName"] = getWeaponDisplayName(player["weapon"]["id"])
                        player["weapon"]["damage"] = getWeaponDamage(player["weapon"]["id"])
                        save(player)

                        print(
                            f"Weapon successfully upgraded to the {player["weapon"]["displayName"]} and does {str(player["weapon"]["damage"])} damage!!! \n")

                        print("Press enter to continue...")
                        input()
                        break
                    else:
                        print("You do not have enough gold to buy the next weapon!")
                        time.sleep(2)
                        os.system("cls")
                        break
                elif continueUpgrade == "n":
                    print("At least you remember how much gold you have :)")
                    time.sleep(2)
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Please enter Y or N")
                    time.sleep(2)
                    continue
        elif upgradeSelected == "armour":
            while True:
                os.system("cls")
                armourCostUpgrade = player["armour"]["nextUpgradeCost"]
                print(f"The upgrade cost for your armour is {armourCostUpgrade} gold")
                print("\nDo you want to continue with the upgrade? (Y/N)")
                continueUpgrade = str(input("> ").lower())

                if continueUpgrade == "y":
                    os.system("cls")
                    if (player["gold"] - armourCostUpgrade) >= 0:
                        player["gold"] -= armourCostUpgrade
                        player["armour"]["nextUpgradeCost"] = round(player["armour"]["nextUpgradeCost"] * 1.60)
                        player["armour"]["id"] += 1
                        player["armour"]["displayName"] = GetArmourDisplayName(player["armour"]["id"])
                        player["armour"]["protection"] = getArmourProt(player["armour"]["id"])
                        save(player)

                        print(f"Armour successfully upgraded to the {player["armour"]["displayName"]} and has {str(player["armour"]["protection"])} protection!!! \n")

                        print("Press enter to continue...")
                        input()
                        break
                    else:
                        print("You do not have enough gold to buy the next armour!")
                        time.sleep(2)
                        os.system("cls")
                        break
                elif continueUpgrade == "n":
                    print("At least you remember how much gold you have :)")
                    time.sleep(2)
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Please enter Y or N")
                    time.sleep(2)
                    continue
            break
        else:
            os.system("cls")
            print("Invalid upgrade selected please select from the available options!")
            time.sleep(2)
            continue

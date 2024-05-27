import os
import json
import time

playerdata = "./Database/player.json"


# playerRead returns the player database in a json object
def readFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as filePreload:
        fileJson = json.load(filePreload)
        return fileJson


# Save is used to dump json data given by the script into teh database for player
def save(player):
    with open(playerdata, 'w', encoding='utf-8') as playerPreload:
        json.dump(player, playerPreload)


# Unimplemented selection menu maker
def selectionMenu():
    print("temp")


# Returns the display name of a weapon using the weapon id
def getWeaponDisplayName(weaponId):
    weaponId -= 1
    weaponsList = "./Database/weaponList.json"
    weaponListJson = readFile(weaponsList)

    return weaponListJson[weaponId]["displayName"]


# Returns the display name of the armour from the armour id

def GetArmourDisplayName(armourId):
    armourId -= 1
    armourList = "./Database/armourList.json"
    armourListJson = readFile(armourList)

    return armourListJson[armourId]["displayName"]


# Returns the damage of a weapon using the weapon id
def getWeaponDamage(weaponId):
    weaponId -= 1
    weaponsList = "./Database/weaponList.json"
    weaponListJson = readFile(weaponsList)

    return weaponListJson[weaponId]["damage"]


# Returns the protection of the armour from the armour id
def getArmourProt(armourId):
    armourId -= 1
    armourList = "./Database/armourList.json"
    armourListJson = readFile(armourList)

    return armourListJson[armourId]["protection"]

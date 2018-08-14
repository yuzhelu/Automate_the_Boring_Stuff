def displayInventory(inventory):
    print("Inventory:")
    item_Total = 0
    for k, v in inventory.items():
        item_Total += v
        print ('Item: ' + str(k) + ' Amount: ' + str(v))
    print('Total number of items: ' + str(item_Total))


def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] = inventory[addedItems[i]]+1



dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = {'gold coin': 42, 'rope': 1}

addToInventory(inv, dragonLoot)

displayInventory(inv)

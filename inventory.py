inventory = {'Steel Dagger': 2, 'Leather Cape': 1, 'Ring of Stealth': 2, 'Rope': 3}

def displayInventory(inventory):
    print("Inventory:")
    item_Total = 0
    for k, v in inventory.items():
        item_Total = item_Total + v
        print ('Item: ' + str(k) + ' Amount: ' + str(v))
    print('Total number of items: ' + str(item_Total))


displayInventory(inventory)

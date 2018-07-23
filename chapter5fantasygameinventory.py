#automate the boring stuff with python page 121
#include addToInventory() function

stuff = {'rope' : 1, 'torch' : 6,'gold coin':42, 'dagger' : 1, 'arrow' : 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for a,b in inventory.items():
        print(a,b)
        total += b
    print('Total number of items: '+str(total))

def addToInventory(inventory, addedItems):
    for c in addedItems:
        if c not in inventory.keys():
            inventory[c] = 0

    for a,b in inventory.items():
        inventory[a] += addedItems.count(str(a))
    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

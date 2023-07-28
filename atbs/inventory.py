# inventory.py
import copy

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v)+' '+k)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    newInv = copy.copy(inventory)
    for k, v in inventory.items():
        for i in addedItems:
            if k == i:
                newInv[k] = newInv[k] + 1
            else:
                newInv.setdefault(i, 1)
    return newInv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
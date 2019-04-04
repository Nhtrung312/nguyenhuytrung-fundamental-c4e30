inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ['seashell' , 'strangeberry' , 'lint']
print(inventory)
del inventory['backpack'][1]
print(inventory)
so = int(input(" nhập số muốn thêm : "))
inventory['gold'] = inventory.get('gold') +so 
print(inventory['gold'])
print(inventory['pouch'])


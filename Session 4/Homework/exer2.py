prices = {"banana" : 4 , 
           "apple" : 2,
          'orange' : 1.5,
            "pear" : 3    }

stock = { "banana" : 6,
           "apple" : 0,
          "orange" : 32,
            "pear" : 15    }

total = {}
#in ra giá tiền và số lượng 
for k in prices :
    print(k)
    print("price :", prices[k])
    print("stock :", stock[k])
    print('        ')
#tính tổng tiền 
for k in prices :
    total[k] = prices[k]*stock[k]
print(total)
tongtien = 0
for i in range(len(total)) :
    tongtien = tongtien + total[k]
print("money i would make if i sold all my food :",tongtien)
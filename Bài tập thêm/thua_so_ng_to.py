so = int(input("nhập số : "))
thua_so = []
so_de_chia = 2
k = 0
while True :
    if so%so_de_chia == 0 and so/so_de_chia != 1 :
        thua_so[k] = so_de_chia 
        k +=1 
        so = so/so_de_chia
    elif so%so_de_chia != 0 and so/so_de_chia !=1 :
        while True :
            so_de_chia += 1 
            for i in range(2,so_de_chia) :
                if so_de_chia%i == 0 :
                    continue 
                
                    
                else :
                    break 

text = str(input(" mời nhập chuỗi kí tự "))
dem_so = {}
for ki_tu in text :
    a = dem_so.get(ki_tu,0) + 1   
    dem_so[ki_tu] = dem_so.get(ki_tu,0) + 1 

    
for i in dem_so :

 print(i,'  ',dem_so[i])
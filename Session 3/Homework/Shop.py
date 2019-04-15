our_items = ["T-shirt","Sweater"]
chon = input( " Well come to our shop, what do you want ( C ,R , U , D, thoat )")
while True :
    if chon != 'C' and chon != 'D' and chon != 'U' and chon != 'R' and chon != 'thoat' :
        chon = input( ' choose again pls :' ) 

    elif chon == 'thoat' :
        break

    elif chon == 'C':
        print("our items :")
        for i in range(len(our_items)) :
         print(our_items[i], ',',end = '' )
    elif chon == 'R':
        print(" you enter new item : jeans ")
        our_items.append('jeans')
        for i in range(len(our_items)) :
            print(our_items[i],',',end ='') 
        
    elif chon == 'U':
        print(" you update  position 2")
        our_items[1] = 'skirt'
        for i in range(len(our_items)) :
            print(our_items[i],',',end ='')
    else :
        if len(our_items) < 3  :
            print("you can't delete position 3")
        else :
            del our_items[2]
            for i in range(len(our_items)) :
             print(our_items[i],',',end ='')
    
    #chon = input('moi nhap lai :')

    


            


        
       





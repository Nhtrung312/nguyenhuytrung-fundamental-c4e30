print(' If x = 8 , then what is th value of 4(x + 3) :')
answer = { "1":"35" , "2":"36" , "3":"40" , "4":"44" }
for k in answer :
    print(k,'. ',answer[k])
choice = int(input(" Your choice :"))
if choice == 4 :
    print('Bingo')
    a = 1
else : 
    a = 0
print('Jack scored these marks in 5 math tests : 49,81,72,66 and 52. What is the mean :')
answer2 = {1 : 'About 55' , 2 : 'About 65' , 3 : 'About 75' , 4 : 'About 85 ' }
for h in answer2 :
    print(h,'. ',answer2[h])
choice2 = int(input(" Your choice :"))
if choice2 == 2 :
    print('Bingo')
    b = 1 
else :
    b = 0
print('You correctly answer ',a+b,'out of 2 question') 
    
        

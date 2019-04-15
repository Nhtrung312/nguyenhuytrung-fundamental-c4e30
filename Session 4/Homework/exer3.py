while True :
    print(' If x = 8 , then what is th value of 4(x + 3) :')
    answer = { "1":"35" , "2":"36" , "3":"40" , "4":"44" }
    for k in answer :
        print(k,'. ',answer[k])
    choice = int(input(" Your choice :"))
    if choice == 4 :
        print('Bingo')
        break
    else :
        continue




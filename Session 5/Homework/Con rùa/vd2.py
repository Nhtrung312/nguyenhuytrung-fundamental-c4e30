def is_inside(l1,l2):
    if l2[0] < l1[0] < l2[0] + l2[2] and l2[1] < l1[1] < l2[1]+l2[3] :

        print('True')

    else :
        print('False')
l1 = [200,120]
l2 = [140,60,100,200]
is_inside(l1,l2)


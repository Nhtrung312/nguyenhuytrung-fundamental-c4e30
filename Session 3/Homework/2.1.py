flock = [5,7,300,90,24,50,75]
print(" hello, my name is Trung and these are my sheep size")
print(flock)

print("my biggest sheep has size ",max(flock),"les's shear it ")

for i in range(len(flock)) :
    if flock[i] == max(flock) :
        v = i
        del flock[v]
    

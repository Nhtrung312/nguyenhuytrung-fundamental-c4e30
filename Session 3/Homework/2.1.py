flock = [5,7,300,90,24,50,75]
print(" hello, my name is Trung and these are my sheep size")
print(flock)

print("my biggest sheep has size ",max(flock),"les's shear it ")

for i in range(len(flock)) :
    if flock[i] == max(flock) :
      break
flock[i] = 8
print(' After shearing , here is my flock ')
print(flock)
for y in range(3) :
  print('month :',y+1)
  for i in range(len(flock)) :
        flock[i] = flock[i] + 50
  print('one month has passed , now here is my flock :') 
  print(flock) 
  print("my biggest sheep has size ",max(flock),"les's shear it ")
  for x in range(len(flock)) :
           if flock[x] == max(flock) :
             break
  flock[x] = 8
  print(' After shearing , here is my flock ')
  print(flock)
print(" My flock has size in total : ", sum(flock))
money = sum(flock)*2
print(' I would get ',sum(flock),' * 2$ =',money,'$' )

    

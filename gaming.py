import random
a = input("enter player 1:")
b = input("enter player 2:")
d1 = random.randint(1,25)
d2 = random.randint(1,25)
s1 = 25
s2 = 25
print("player 1 guess")
while True:
    g=int(input("Enter your guess"))
    s1 = s1-1
    if(d1==g):
       print("ur guess is correct")
       break
    elif(d1<g):
       print("ur guess is more")
    else:
        print("ur guess is less")
    
print("player 2 guess")
while True:
    g=int(input("Enter your guess"))
    s2 = s2-1
    if(d2==g):
       print("ur guess is correct")
       break
    elif(d2<g):
       print("ur guess is more")
    else:
       print("ur guess is less")
if(s1==s2):
   print("MATCH IS DRAW!!!")
elif(s1>s2):
   print( "WINNER",a)
else:
   print("WINNER",b)
    

    
      
           

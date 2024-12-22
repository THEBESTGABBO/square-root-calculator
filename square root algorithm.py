from mpmath import *

while True:
    num=input("Enter a number to get its square root: ")
    prec=input("Enter the precision of the square root (number of digits): ")

    mp.dps= int(prec) #sets mpf precision

    sqrt=""
    for i in range(int(prec)): #iterates as many times as "precision" says
        x=9 #support variable for 9 to 0 counting
        for j in range(10): #iterates through digits from 9 to 0
            if mpf(sqrt+str(x))**2<mpf(num) and mpf(sqrt+str(x))**2!=mpf(num):
                if i==0:
                    sqrt=str(x)+"."
                else:
                    sqrt=sqrt+str(x)
                break
            elif mpf(sqrt+str(x))**2==mpf(num):
                if i==0:
                    sqrt=str(x)+"."
                else:
                    sqrt=sqrt+str(x)
            else:
                x-=1

    print(sqrt)

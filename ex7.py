#CORRETO!
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def ePrimo(num):
    cont = 0
    for x in range(1,num+1):
        if(num%x == 0):
            cont+=1
    if cont == 2:
        return True
    else:
        return False

def main():
    nTermo = int(input("DIGITE O ENESIMO TERMO!!!\n"))
    value = 1
    cont = 0
    
    while cont<nTermo:
        if(ePrimo(value)):
            if cont == nTermo-1:
                print(f"O {nTermo}º número primo é {value}")
                break
            cont+=1
            value+=1
        else:
            value+=1

if __name__ == "__main__":
    main()
#CORRETO!
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def primoOuNao(num):
    cont = 0
    for x in range(1, num+1):
        if num%x == 0:
            cont+=1
    if cont == 2:
        return True
    else:
        return False

def main():
    soma = 0
    
    for y in range(1, 2000000):
        if(primoOuNao(y)):
            soma+=y
    print(soma)
    
if __name__ == "__main__":
    main()
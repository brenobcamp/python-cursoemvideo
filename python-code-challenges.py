# Python Code Challenges // Linkedin Learning
# 01 Find prime numbers

def get_prime_numbers ():
    num = int(input("Type a number to know its factorization in prime numbers: "))
    numfactor = num
    factorlist = []
    while numfactor != 0:
        for x in range(2, num+1):
            if x%x == 0 and x%2 != 0:
                numfactor/x
                factorlist.append(x)
    print(factorlist)        
#get_prime_numbers()

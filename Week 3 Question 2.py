"""
PRIME(number,divisor)
     IF number=0
        OUTPUT number "is not prime"
    ELSE IF number=1
        OUTPUT number "is not prime"
    ELSE IF divisor=1:
        OUTPUT numer "is prime"
    ELSE
        IF number divisible by divisor
           OUTPUT number "is not prime"
        ELSE
           return PRIME(number, divisor-1)
PRIME_CHECK()
number<-input "please enter a number"
return PRIME(number, number-1)
"""

def prime(number,divisor): 
    if number==0:
        print (str(number)+" is not prime")
    elif number==1:
        print (str(number)+" is not prime")
    elif divisor==1:
        print (str(number)+" is prime") 
    else:
        if number%divisor==0: 
            print(str(number)+" is not prime")
        else:
            return (prime(number,divisor-1)) 

def prime_check():
    number=int(input("Please enter a number: "))
    return prime(number,number-1)

print (prime_check())

"""
Line 26: this is the base case as the divisors will keep dividing until 1 is reached.
         If the only factor of x is 1, then its prime;
Line 28: if the input is divisible by any other number apart from itself and 1
         then it won't be prime;
Line 31: otherwise, recursively keep checking each number until it reches
         the limit, which is starting from number-1;

Reference:
http://stackoverflow.com/questions/37095508/how-do-i-find-a-prime-number-using-recursion-in-python
"""

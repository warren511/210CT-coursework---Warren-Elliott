def factorial(x):                           
    if x==1 or x==0:                        #1
        return (1)                          #1
    else:                                   #1
        n=x*factorial(x-1)                  #1
        return n                            #1

def reverse(n):                              
    if n=="": #base case                    #1
        return n                            #1
    else:                                   #1
        return reverse(n[1:])+n[0]          #1

def trailing_zeros(n):
    z=str(factorial(n))                     #1
    reverse_z=str(reverse(z))               #1
    result=0                                #1
    for i in reverse_z:                     #n
        if i=="0":                          #n
            result+=1                       #n
        else:                               #n
            break                           #n
            print ("0")                     #n 
    print (result)                          #1

print (trailing_zeros(5))

"""
#Lines 1,2,3,4,5,6: a recursive factorial function is created that will find
                    the factorial of any number; the base case for this recursion
                    is in Line 2 where if x <- 1, 1 is returned, as the factorial
                    of 1 is 1;
#Lines 8,9,19,11,12: this following recursive function will reverse the number obtained
                     from the previous function; in this function, n is considered as a
                     string and the base case is in Line 9 where the recursion stops if
                     there is an empty string;
#Line 14: function to find the number of trailing zeros: this function will call the previous
          recursive functions, count the number of zeros from the reversed factorial and stop
          when there is not a zero;
#Line 15: calling the factorial function and converting into a string to be reversed in the
          reversing function;
#Line 16: calling the reverse function above to reverse the string and storing it in the
          variable reverse_z;
#Line 17: starting result that will be output: this will count the number of zeros;
#Lines 18,19,20: iterating through the reverse_z variable: if the character in the string is “0”,
                 +1 is added to the result variable;
#Lines 21,22,23,24: otherwise, break the loop, output the result;

Run time bound:
1+1+1+n+n+n+n+n+1==4+5n
hence the runtime bound for worst case scenario is O(n)
"""


    
    

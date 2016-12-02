"""
CLOSEST_SQUARE(N)
    (n_root)<-square root(n)                (1)
    conversion<-convert(n_root)to int       (1)
    result<-do conversion to power 2        (1)
    IF n=result                             (1)
        OUTPUT n                            (1)
    ELSE                                    (1)
        OUTPUT result                       (1)
    ENDIF

//Line 3:find the square of n;
//Line 4:convert it into an integer;
//Line 5:raise this integer to the power of 2 to compare it with the input;
//Line 7:if the squared integer is the same as the input, return it;
//Line 9:otherwise, return the calculated result of the highest perfect square

run time bound for the following algorithm is O(1) which means that will
execute any input at the same time as the graph will be constant throughout.
   
References:
https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/
http://users.csc.calpoly.edu/~jdalbey/SWE/pdl_std.html
"""

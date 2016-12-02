"""
BINARY_SEARCH(L,low,high)
    start<-0
    end<-length L-1

    WHILE start LESS OR EQUAL TO end
          midpoint<-(start+end)//2
          IF L[midpoint]LESS OR EQUAL TO high and L[midpoint] GREATER OR EQUAL THAN low
             return TRUE
          ELSE IF L[midpoint]>high
             end=midpoint-1
          ELSE IF L[midpoint]<low
             end=midpoint+1
          ENDIF

          IF L[midpoint]<high and L[midpoint]>low:
             return TRUE
          ELSE
             return FALSE
    ENDWHLE
"""
L=[2,3,5,7,9,10,13,12,11]

def binary_search(L,low,high):#25
    start=0#26
    end=len(L)-1
    
    while start<=end: 
        midpoint=(start+end)//2
        if L[midpoint]<=high and L[midpoint]>=low:
            return True
        elif L[midpoint]>high:
            end=midpoint-1
        elif L[midpoint]<low:
            start=midpoint+1

        if L[midpoint]<high and L[midpoint]>low:
            return True
        else:
            return False

print (binary_search(L,11,13))

"""
Lines 29,30,31,32,33,34,35,36: Binary search is implemented. The list gets divided by 2
      and compared with the parameters given. The start and end variables which are the
      positions in the list are changged at each iteration.
Lines 38,39,40,41,42: if the final midpoint is in between the parameters, then output true.
      If not, false.
RUNTIME BOUND: O(log n)
"""

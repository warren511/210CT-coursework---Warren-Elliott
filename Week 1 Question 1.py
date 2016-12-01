import random                         #1   
original_list= [5,3,8,6,1,9,2,7]

def shuffle(d):
    shuffled_output=[]                #1   
    index_list=list(range(0,len(d)))  #1   
    random.shuffle(index_list)        #1   

    for integer in index_list:        #n             
        x=d[integer]                  #n   
        shuffled_output.append(x)     #n
        print (shuffled_output)       #1

shuffle(original_list)

"""
Line 1: in order to use the random.shuffle function, random is imported;
Line 5: firstly, an empty list is created; shuffled integers will be
        added onto it and this will be the printed output;
Line 6: a list of indexes is created for it to be shuffled using
        the random.shuffle function;
Line 7: this shuffles the indexes of the original_list 
Line 10:for each item in the now shuffled index_list, a variable x is
        created which assigns the index to the original_list(d)
Line 11:this variable x is then added onto the output list.
        The x variable is the new assigned integer from the shuffled
        index list;

Big O notation is:
1+1+1+n+n+n+1
4+3n == O(n)
"""

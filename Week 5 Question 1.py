def list(L): 
    sublist=[]
    start_point=0
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            sublist.append(L[start_point:i+1])
            start_point=i+1
    sublist.append(L[start_point:i+i])    
    print(sublist)

    output=[]
    for x in range (len(sublist)-1):
        if sublist[x]>sublist[x+1]:
            output.append(sublist[:x+1])
            print(output)
        
    print (output)

        
       
"""
Lines 5,6,7: within the iteration, compare each item in the list
     with the next item. If it is bigger than the next item,
     create a sublist and store the iteration creating a new start
     point to carry on with the iteration;
Lines 12,13,14,15,16,17: this compares the sublists within the
       newly created list which will output the longest list;

Reference:
https://rosettacode.org/wiki/Longest_increasing_subsequence#Python
http://www.java2s.com/Tutorials/Python/List/How_to_get_sub_list_by_slicing_a_Python_List.htm
http://stackoverflow.com/questions/18570740/python-split-a-list-into-sub-lists-based-on-index-ranges
"""

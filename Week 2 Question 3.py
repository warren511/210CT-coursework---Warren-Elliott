"""
ADDITION(B,C)
    for x range length of B                                                               //n  
        for i in range length of B[0]                                                     //n*n
            addition_result1[x][i]<-ADD b[x][i] and c[x][i]                               //n*n
    return addition_result                                                                //1

SCALE_BY_2(addition_result)
    for x range length of addition_result                                                 //n
        scaled_result[x][i]<-multiply addition_result[x][i] by 2                          //n
    return scaled_result                                                                  //1
    
MULTIPICATION (B,C)
    for x range length of B                                                               //n
        for i in range length C[0]                                                        //n*n
            for each loop range length of C                                               //n*n*n
                multiplication_result[x][i]<-multiply B[x][loop] and C[loop][i]           //n*n*n
    return multiplication_result                                                          //1

SUBTRACT(multiplication_result,scaled_result)
        for x range length of multiplcation_result                                        //n
            for i in range (length multiplication result[0])                              /n*n
                final_result[x][i]<-SUBTRACT multiplication_result[x][i] and scaled_result[x][i] //n*n
        return final_result                                                               //1

    

//A=B*C –2*(B+C) in order to compute this function, a bidmas approach is used;
//Lines 2,3,4,5,6: starting by adding the B and C matrix inside the equation. Add
                   by iterating each list representing a column and a row in the matrix;
//Lines 8,9,10,11: then scale the result obtained from the previous function by two;
//Lines 13,14,15,16,17:the same way the adding functon was implemented, a multiplication
                       function is added which will compute B*C;
//Lines 19,20,21,22: finally the last subtraction function follows the same structure
                     as addition and multiplication, where multiplication_result and scaled
                     result are added as arguments.
                     These are subtracted and the result is outputed in line 23.

RUNTIME BOUND:
n+(n*n)+(n*n)+1+n+n+1+n+(n*n)+(n*n*n)+(n*n*n)+1+n+(n*n)+(n*n)+1
2n^2+5n^2+5n+4
O(N^3) as nested loops are present.    

//references:https:www.programiz.com/python-programming/examples/add-matrix
                 //www.programiz.com/python-programming/examples/multiply-matrix
"""

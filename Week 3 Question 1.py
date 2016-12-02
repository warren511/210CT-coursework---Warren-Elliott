"""
REVERSED_SENTENCE()
    sentence<-input sentence
    newList<-[]
    newWord<-empty string
    for charater in sentence
       IF charater not space
          append iteration to newWord
       ELSE:
          append newWord to newList
          create new empty string
       ENDIF
    IF sentence not space:
       append newWord to newList
    ENDIF
    outputList=[]
    outputList=reverse newList
    output<-"".separate outputList
    OUTPUT (output)
"""
def reversed_sentence():
    sentence=str(input("enter a sentence"))
    newList=[] 
     newWord=" "
    for character in sentence:
        if character != " ":
            newWord+=character
        else:
            newList.append(newWord)
            newWord=" "
    if sentence != " ":
        newList.append(newWord)

    outputList=[]
    outputList=newList[::-1]
    output="".join(outputList)
    print (output)

"""
Line 22: this is the input that will be reversed;
Lines 23: creating an empty list where the list will be sliced
Line 24: group each word into a string within newList
Line 25: this iteration goes through every character in the string
Line 26: if the charater in the string is not a space,
         each character that has been iterated will go to newWord;
Line 28: otherwise, once there is a space, store the word to the
         list and recreate the variable to keep adding characters
Line 30: recreating this conditional for the last
         word as there are no futher spaces after the last word;
Line 34: this line reverses the list and stores into a new list called output list
Line 25: the variables in this array are then split into strings stored
         under the string variable "output"
"""

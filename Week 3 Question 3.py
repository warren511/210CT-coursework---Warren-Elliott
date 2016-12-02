"""
REMOVE_VOWELS(sentence)
   vowels<-"aeiouAEIOU"
   IF not sentence
      return sentence
    ELSE IF sentence[0] in vowels:
            return REMOVE_VOWELS(sentence[1:])
    return sentence[0]+REMOVE_VOWELS(sentence[1:])
"""
def remove_vowels(sentence):
    vowels="aeiouAEIOU"
    if not sentence: 
        return sentence
    elif sentence[0] in vowels: 
        return remove_vowels(sentence[1:]) 
    return sentence[0] + remove_vowels(sentence[1:]) 
print (remove_vowels('hello world'))

"""
Lines 12,13: base case. keep recursing until there are no characters left
Lines 14,15:if the first character is in the string vowels
            skip it and process the remaining characters
Lines 16: recurse until base case

Reference:
http://stackoverflow.com/questions/25166338/recursive-function-to-remove-vowels
"""

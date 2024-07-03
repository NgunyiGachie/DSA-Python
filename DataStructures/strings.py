# Q1.Write a program to create a new string made of an input string’s first, middle, and last character.

# program to create a new string made of an input's first, middle, and last character
# input string
# output string containining first, middle, and last character

def my_string(str1):
    middle = str1[len(str1)//2]
    result = str1[0] + middle + str1[-1]
    return result

#Q2 Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore('_)

# input a string containing a combination of different letters
# output a string split into a combination of two letters. If a combination is odd, the missing number is replaced with an ('_)

def split_string(str1):
    if len(str1) % 2 != 0:
        str1 += '_'

    string_pairs = [str1[i:i+2] for i in range(0, len(str1), 2)]
    return string_pairs

#Q3 Create a function to determine if the count of each of the characters in a string can be equal if we remove

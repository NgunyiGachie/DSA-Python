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

#Q3 Create a function to determine if the count of each of the characters in a string can be equal if we remove a single character from that string

# input - a string containing n number of characters
# process - remove one character from the string
# output - return true if the count is same when the character is removed else false.

def solve(s):
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    values = list(frequencies.values())
    unique_values = set(values)
    
    if len(unique_values) == 1:
        return True

    if len(unique_values) == 2:
        freq1, freq2 = unique_values
        count1 = values.count(freq1)
        count2 = values.count(freq2)
        
        if (count1 == 1 and (freq1 == freq2 + 1 or freq1 == 1)) or \
           (count2 == 1 and (freq2 == freq1 + 1 or freq2 == 1)):
            return True

    return False
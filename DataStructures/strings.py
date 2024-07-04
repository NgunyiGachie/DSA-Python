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

"""With your birthday coming up soon, your eccentric friend sent you a message to say "happy birthday": At first it looks like a song, but upon closer investigation, you realize that your friend hid the phrase "happy birthday" thousands of times inside his message. In fact, it contains it more than 2 million times! To thank him, you'd like to reply with exactly how many times it occurs.
To count all the occurences, the procedure is as follows: look through the paragraph and find a 'h'; then find an 'a' later in the paragraph; then find an 'p' after that, and so on. Now count the number of ways in which you can choose letters in this way to make the full phrase.
More precisely, given a text string, you are to determine how many times the search string appears as a sub-sequence of that string.
Write a function called countSubsequences that takes two arguments: needle, the string to be  search for and haystack, the string to search in. In our example, "happy birthday" is the needle and the birthday message is the haystack. The function should return the number of times needle occurs as a sub-sequence of haystack. Spaces are also considered part of the needle."""

def count_subsequences(needle, haystack):
    counts = [0] * (len(needle) + 1) # list to store each character in needle. The list is initialized to zero because we have not found any subsequence yet. 
    counts[0] = 1 # empty needle is a subsequence of haystack
    for char in haystack:
        for i in range(len(needle) -1, -1, -1): # iterate through needle in reverse order using the same character twice
            if char == needle[i]:
                counts[i + i] += counts[i]
    return counts[len(needle)]
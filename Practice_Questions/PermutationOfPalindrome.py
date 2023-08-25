# Check if it's permutation of palindrome or not
# Permutation does not need to be limited to just dictionary word.

# Example -  Input :: "Tact coa"
# Output  -   True :: "taco cat"

# For permutation we check if # of odd character is less than or equal to 1
# so that all even characters can fit on both sides equally for 2 at left and 2 at right or 1 at left
# and one at right. or if odd is 0 so still it can be palindrome half on left and half on right

def character_number(char):
    lower_a = ord('a')
    lower_z = ord('z')
    upper_a = ord('A')
    upper_z = ord('Z')
    character_val = ord(char)

    if lower_a <= character_val <= lower_z:
        return character_val - lower_a
    elif upper_a <= character_val <= upper_z:
        return character_val - upper_a
    else:
        return -1

def if_permutation_of_palindrome(word):
    count_array = [0 for i in range(ord('z') - ord('a') +1)]
    # First we have to check we only calculate on alphabetic character set not any other character
    for letter in word:
        letter_number = character_number(letter)
        if letter_number != -1:
            count_array[letter_number] += 1

    odd_count = sum([i%2 for i in count_array])
    return odd_count <= 1



print(if_permutation_of_palindrome("no x in nixon"))

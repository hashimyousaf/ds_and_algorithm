"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed,
etc. Furthermore, you may assume that the original data does not contain any

digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
"""

# We are gonne use two stack, one for num and one for string.
# If we get [ or alphabet we will push it to strStack


def decodeString(s: str) -> str:
    numstack = []
    strstack = []
    temp_num = ""
    for char in s:
        if char.isdigit():
            temp_num += char
        elif char.isalpha() or char == '[':
            strstack.append(char)
            if temp_num != "":
                numstack.append(temp_num)
            temp_num = ""
        else: # it's goin to be ]  --> closing brackets
            # pop until you find [
            # concatenate all the letters
            # multiple it with numstack.pop()
            # Push back to the stack
            temp_str = ""
            while strstack:
                popped_elemet = strstack.pop()
                if popped_elemet == '[':
                    break
                temp_str = popped_elemet + temp_str

            if numstack:
                temp_str = int(numstack.pop()) * temp_str

            for i in temp_str:
                strstack.append(i)

    return "".join(strstack)



if __name__ == '__main__':
    print(decodeString("3[a2[c]]"))   # accaccacc
    print(decodeString("3[a]2[bc]"))   # aaabcbc
    print(decodeString("100[leetcode]"))

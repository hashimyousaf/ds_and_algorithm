from collections import Counter
def if_permutation_through_sorting(source, target):
    # sort both string and compare it
    if len(source) != len(target):
        return False
    source = sorted(source) # NlogN where N is the length of our strings(source or target bcz they are equal now)
    target = sorted(target)

    for index in range(len(source)):
        if source[index] != target[index]:
            return False
    return True
    # TC is Nlogn


def if_permutation(source, target):
    if len(source) != len(target):
        return False

    counter = [0] * 256
    for char in source:
        counter[ord(char)] += 1

    for char in target:
        if counter[ord(char)] == 0:
            return False
        counter[ord(char)] -= 1
    return True
    # TC is N

def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)



print(if_permutation_through_sorting("abbc", "babc"))
print(if_permutation("abbc", "babc"))
print(check_permutation_pythonic("abbc", "babc"))
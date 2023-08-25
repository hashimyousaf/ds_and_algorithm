"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine
and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""



class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_dict = {}
        for char in magazine:
            # magazine_dict[char] =  1 if char in magazine_dict else magazine_dict[char] + 1
            if char in magazine_dict:
                magazine_dict[char] += 1
            else:
                magazine_dict[char] = 1
                # {a: 2, b: 1}

        for char in ransomNote:
            if char in magazine_dict and magazine_dict[char] > 0:
                magazine_dict[char] -= 1
            else:
                return False
        return True

print(Solution.canConstruct(ransomNote = "aa", magazine = "aab"))
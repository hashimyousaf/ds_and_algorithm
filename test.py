
class Solution:
    def longestStrChain(self, words) -> int:
        dp = {}
        res = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1 :]
                if prev in dp:
                    dp[word] = dp[prev] + 1 if dp[prev] + 1 > dp[word] else dp[word]
                    res = max(res, dp[word])

        return res

failed_case_list = ["c","cd","ab","bcd","abc","abcd","abcde"]
pass_case_list = ["a","b","ba","bca","bda","bdca"]

#print(Solution().longestStrChain(failed_case_list))


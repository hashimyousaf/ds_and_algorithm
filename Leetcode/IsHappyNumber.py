class Solution:
    dict_to_check = {}

    def check_if_loop(self, num):
        if num not in self.dict_to_check:
            self.dict_to_check[num] = True
        else:
            return -1

    def isHappy(self, n: int) -> bool:
        if n >= 1 and n <= 2147483847:
            square_sum = 0
            for number in str(n):
                square_sum += int(number) * int(number)
            if square_sum == 1:
                return True
            else:
                return False if self.check_if_loop(square_sum) == -1 else self.isHappy(square_sum)


print(Solution().isHappy(13))
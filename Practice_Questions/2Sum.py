# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

def two_sum(nums, target):
    results = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
               results.append((nums[i], nums[j]))
    return results

def two_sum_optimized(arr_list, target):
    hash_map = {}

    for i in range(len(arr_list)):
        resultant = target - arr_list[i]
        if resultant in hash_map and hash_map[resultant] != i:# to catter the case [3,3]  target = 6
            print(arr_list[i], resultant)

        hash_map[arr_list[i]] = i




if __name__ == '__main__':
    # Input: nums = [2,7,11,15], target = 9
    print(two_sum([2,7,11,15, 2], 9))
    print("two_sum_optimized([2,7,11,15, 2], 9)")
    two_sum_optimized([2,7,11,15, 2], 9)
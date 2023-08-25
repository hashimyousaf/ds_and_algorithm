"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0

        resultant_arr = []

        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                resultant_arr.append(nums1[i])
                i += 1
            else:
                resultant_arr.append(nums2[j])
                j += 1
        # Check which elements need to be append to the resultant
        while i < len1:
            resultant_arr.append(nums1[i])
            i += 1
        while j < len2:
            resultant_arr.append(nums2[j])
            j += 1

        if len(resultant_arr) % 2 == 0:
            # it means resultant has Even length so have to sum two mid elements and divide it by 2
            return (resultant_arr[int(len(resultant_arr) / 2)] + resultant_arr[int(len(resultant_arr) / 2) - 1]) / 2
        else:
            # mean it has odd length just return the middle element of the resultant
            return resultant_arr[int(len(resultant_arr) / 2)]

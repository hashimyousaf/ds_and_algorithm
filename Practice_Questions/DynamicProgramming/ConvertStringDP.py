"""
S1 and S2 are given strings
Convert S2 to S1 using delete, insert or replace operations
Find the minimum count of edit operations

Example:
    - S1 = "catch"
    - S2 = "carch"
    - output = 1   (replace r with t, S2 will become the S1)

    - S1 = "table"
    - S2 = "tbres"
    - output = 3   (Insert "a" to second position, replace "r" with "l" and delete "s")
"""
# Convert One String to Another with minimum operation in Python
# Divide and conquor technique
def findMinOperationTopDownDP(s1, s2, index1, index2, memo):
    if index1 == len(s1):
        return len(s2)-index2
    if index2 == len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return findMinOperationTopDownDP(s1, s2, index1+1, index2+1, memo)
    else:
        dict_key = str(index1) + str(index2)
        if dict_key not in memo:
            deleteOp = 1 + findMinOperationTopDownDP(s1, s2, index1, index2+1, memo)
            insertOp = 1 + findMinOperationTopDownDP(s1, s2, index1+1, index2, memo)
            replaceOp = 1 + findMinOperationTopDownDP(s1, s2, index1+1, index2+1, memo)
            memo[dict_key] =  min (deleteOp, insertOp, replaceOp)
        return memo[dict_key]

def find_min_operation_bottom_up_practice(s1, s2):
    count = 0
    if len(s1) > 0 and len(s2) > 0:
        s1_index = 0
        s2_index = 0
        while s1_index < len(s1) and s2_index < len(s2):
            if  s1[s1_index] == s2[s2_index]:
                # just pass it with out incrementing the count
                s1_index += 1
                s2_index += 1
            elif (s1_index+1 != len(s1)) and s2[s2_index] == s1[s1_index +1] :
                # So it was an insert
                s1_index += 1
                count += 1
            elif (s2_index+1 != len(s2)) and s2[s2_index + 1] == s1[s1_index]:
                # So it was a delete operation
                s2_index += 1
                count += 1
            else:
                # it's going to be the replace operation just increment for both of them
                s1_index += 1
                s2_index += 1
                count +=1
        if s1_index == len(s1):
            # it mean it(s1) was the short string we have to perform delete operaiton on s2
            count += len(s2) - s2_index
        else:
            # it means it(s2) was the short string we have to perform insert operation to make it equla to S1
            # but how many, just take count of remaining character
            count += len(s1) - s1_index
        return count
    else:
        return None



temp_dict = {}
print(findMinOperationTopDownDP("table", "tbrltt", 0, 0, temp_dict))
print(find_min_operation_bottom_up_practice("table", "tbrltt"))
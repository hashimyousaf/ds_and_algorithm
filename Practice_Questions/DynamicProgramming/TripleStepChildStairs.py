"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement
a method to count how many possible ways the child can run up the stairs.
"""

# Top down approach DP
def running_child_triple_step(counter, stairs, memo):
    if counter == stairs:
        return 1
    elif counter > stairs:
        return 0
    else:
        if (counter, stairs) not in memo:
            way1 = running_child_triple_step(counter + 1, stairs, memo)
            way2 = running_child_triple_step(counter + 2, stairs, memo)
            way3 = running_child_triple_step(counter + 3, stairs, memo)
            memo[(counter, stairs)] = way1 + way2 + way3

        return memo[(counter, stairs)]

# Bottom up approach DP
def running_child_triple_step_bottom_up(stairs):
    memo = {}
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4
    if stairs == 1:
        return 1
    elif stairs == 2:
        return 2
    elif stairs == 3:
        return 4
    else:
        for i in range(4,stairs+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[stairs]




if __name__ == '__main__':
    print(running_child_triple_step(0, 38, {}))
    print(running_child_triple_step_bottom_up(38))
    print("Hashim")
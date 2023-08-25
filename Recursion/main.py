def power_of_two(n):
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    if n == 0:
        return 1
    else:
        power = power_of_two(n-1)
        return power * 2

def factorial(n):
    assert 0 <= n == int(n), "The value must of positive integer."
    if n in [0, 1]:
        return 1
    else:
        return factorial(n-1) * n

def fibanacci(n):
    assert 0 <= n == int(n), "The value for fibanacci number should be positive integer."
    if n in [0, 1]:
        return n
    else:
        return fibanacci(n-1) + fibanacci(n-2)

# How to find the sum of digits of a positive number using recursion
def sum_of_digts_using_recursion(n):
    assert n >= 0 and int(n) == n, "Number can't be negative, please provide +ve number."
    if n == 0:
        return 0
    else:
        return sum_of_digts_using_recursion(int(n/10)) + (n%10)

# How to calculate the power of a number using recursion
def power_of_number(base, power):
    # 2 pow 3 = 2 * 2 * 2
    assert 0 < power == int(power), "Power must be positive integer number only."
    if power == 0:
        return 1
    if power == 1:
        return base
    return power_of_number(base, power-1) * base

# How to find GCD(greatest common divisor) of two numbers using recursion
# euclidean algo says if we divide greater value with lower and then keep getting remainder until
# we get remainder 0, it can give us greatest common diviser of two number
def gcd(a, b): # 12, 48
    assert int(a) == a and int(b) == b, "The numbers must be integer only!"
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def dec_to_binary(n):
    # calculation for 10
    # 10/2 = 5 rem =1
    #  5/2 = 2 rem =0
    #  2/2 = 1 rem =1
    #  1/2 = 0 rem =1
    if n == 0:
        return 0
    else:
        return n%2 + dec_to_binary(int(n/2)) * 10
    # dec(1) --> 1* 10
    # dec(2) --? 10 * 10
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])

#RECURSIVE RANGE SOLUTION
def reverse_string(str):
    # Has -> reverse_string( as ) + H
    # as -> reverse_string(s) + a
    # s -> reverse_string([]) + s
    if len(str) <= 1:
        return str
    else:
        return reverse_string(str[1:]) + str[0]
def reverse_string_without_recursion(str):
    half_of_str = len(str)/2
    str = list(str)
    for i in range(0, int(half_of_str)):
        temp = str[i]
        str[i] = str[-i -1]
        str[-i -1] = temp
    return ''.join(str)

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])

def capitalizeWords(arr):
    if len(arr) <= 1:
        return [arr[0].upper()]
    else:
        return [arr[0].upper()] + capitalizeWords(arr[1:])

if __name__ == '__main__':
    # print(power_of_two(3))
    # print(factorial(4))
    # print(fibanacci(8)) # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    # print(sum_of_digts_using_recursion(138)) # 14
    #print(power_of_number(base=2, power=3))
    #print(gcd(48, 18))
    # print(dec_to_binary(2))
    # print(productOfArray([3,2,3]))
    # print(reverse_string("Yousaf"))
    # print(reverse_string_without_recursion("Hashim Yousaf"))
    print(capitalizeFirst(["this", "is", "hashim"]))
    print(capitalizeWords(['i', 'am', 'learning', 'recursion']))




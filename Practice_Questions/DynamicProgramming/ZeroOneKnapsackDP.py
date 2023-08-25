"""
Given the weight and profit on N items and these items can not be broken into pieces. Create a function to find
the maximum profit within given capacity of C using Top Down method.

Example:
    - profits = [31, 26, 72, 17]
    - Weights = [3, 1, 5, 2]
    - Capacity = 7

    Answer is 98
"""
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def zoKnapsack(items, capacity, currentIndex, tempDict):
    dictKey = str(currentIndex) + str(capacity)
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif dictKey in tempDict:
        return tempDict[currentIndex]
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity - items[currentIndex].weight,
                                                          currentIndex + 1, tempDict)
        profit2 = zoKnapsack(items, capacity, currentIndex + 1, tempDict)
        tempDict[dictKey] = max(profit1, profit2)
        return tempDict[dictKey]
    else:
        return 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zoKnapsack(items, 7, 0, {}))
if __name__ == '__main__':
    dict1 = {"one": 1, "two": 2, "three": 3}
    dict2 = dict1.copy()
    dict2["one"] = 11
    print(id(dict1["one"]))
    print(id(dict2["one"]))

    list1 = [1, 2, 3]
    list2 = list1.copy()
    list2[0] = 11
    print(list1[0])
    print(list2[0])



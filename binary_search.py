def binary_search(nums: list, target: int) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mi = (lo + hi) // 2
        if nums[mi] == target:
            return mi
        elif nums[mi] < target:
            lo = mi + 1
        else:
            hi = mi - 1
    return -1


test0 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    },
    'target': 10,
    'output': 9
}

test1 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    },
    'target': 11,
    'output': -1
}

test2 = {
    'input': {
        'nums': [1]
    },
    'target': 1,
    'output': 0
}

test3 = {
    'input': {
        'nums': [1]
    },
    'target': 2,
    'output': -1
}

tests = [test0, test1, test2, test3]
for test in tests:
    print(binary_search(test['input']['nums'], test['target']) == test['output'], end=" ")
    print(test)

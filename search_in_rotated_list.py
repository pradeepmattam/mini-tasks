test0 = {
    'input': {
        'nums': [11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    },
    'target': 10,
    'output': 11
}

test1 = {
    'input': {
        'nums': [23, 25, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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
        'nums': [2,3,1]
    },
    'target': 4,
    'output': -1
}

test4 = {
    'input': {
        'nums': [21,22,23,24,25]
    },
    'target': 4,
    'output': -1
}

test5 = {
    'input': {
        'nums': [21,22,23,24,25]
    },
    'target': 23,
    'output': 2
}

test6 = {
    'input': {
        'nums': [23, 25, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    },
    'target': 23,
    'output': 0
}

def find_pivot(nums: list):
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mi = (lo + hi) // 2
        if mi > 0 and nums[mi] < nums[mi-1]:
            return mi
        elif nums[mi] <= nums[hi]: #right half is sorted
            hi = mi - 1
        else:
            lo = mi + 1
    return 0

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

tests = [test0, test1, test2, test3, test4, test5, test6]

def search_rotated_list (nums: list, target: int) -> int:
    pivot = find_pivot(nums)
    index = binary_search(nums[:pivot], target)
    if index == -1:
        index = binary_search(nums[pivot:], target)
        if index != -1:
            return len(nums[:pivot]) + index
    else:
        return index
    return -1

for test in tests:
    print(search_rotated_list(test['input']['nums'], test['target']) == test['output'], end=" ")
    print(test)

'''
problem statement:
 Given a sorted list - the list rotated unknown number of times,
 write a function to find the number of times the list is rotated.
 assumption: List entries can repeat.
0.
test0 = {
    'input' : {
        'nums': [101,101, 24,24, 56,56, 89, 90,90]
    },
    'output' : 2
}
 1.
test1 = {
    'input': {
        'nums': [10,11,11,5,5,6,7,8,8,9]
    },
    'output': 3
}

2.
test2 = {
    'input': {
        'nums': [5,5,5,5, 6, 9, 0, 2, 3, 4]
    },
    'output': 6
}

 edge cases
 3.
test3 = {
    'input': {
        'nums': [1,1,1,1,1,1]
    },
    'output': 0
}

 4.
test4 = {
    'input': {
        'nums': []
    },
    'output': 0
}

5.
test5 = {
    'input': {
        'nums': [1,2,3,5,6,7,7,7,7,7,8,9]
    },
    'output': 0
}

6.
test6 = {
    'input': {
        'nums': [1,2,3,4,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,0]
    },
    'output': 20
}
linear search solution approach:
1. initialize the index to 1
2. compare the value at the index position with the index-1 value
3. if the element at index position is lesser than the index-1 value return index
4. else increment the index and repeat step 2-3.

binary search solution approach:
if len(input list) <=1 return 0
1. initialize variable lo to 0 and hi to len(input list)-1
2. while lo<=hi, derive the middle index with floor div and retrieve the middle value
3. if value @ middle index is less than the value at middle index -1 return middle index
4. if value @ middle index is less than the last element, set hi to middle index - 1
5. else if value @ middle index is greater than the last element, set lo to middle index + 1
6. repeat  2-5
7. return 0


'''

def ls_count_list_rotations(nums: list):
    if len(nums) <= 1:
        return 0
    index = 1
    while index < len(nums):
        if nums[index] < nums[index-1]:
            return index
        index += 1
    return 0

def bs_count_list_rotations(nums: list):
    if len(nums) <= 1:
        return 0
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


def verify_ls_solution(nums, output):
    return ls_count_list_rotations(nums) == output


def verify_bs_solution(nums, output):
    return bs_count_list_rotations(nums) == output


test0 = {
    'input' : {
        'nums': [101,101, 24,24, 56,56, 89, 90,90]
    },
    'output' : 2
}


test1 = {
    'input': {
        'nums': [10,11,11,5,5,6,7,8,8,9]
    },
    'output': 3
}


test2 = {
    'input': {
        'nums': [5,5,5,5, 6, 9, 0, 2, 3, 4]
    },
    'output': 6
}

test3 = {
    'input': {
        'nums': [1,1,1,1,1,1]
    },
    'output': 0
}


test4 = {
    'input': {
        'nums': []
    },
    'output': 0
}


test5 = {
    'input': {
        'nums': [1,2,3,5,6,7,7,7,7,7,8,9]
    },
    'output': 0
}

test6 = {
    'input': {
        'nums': [1,2,3,4,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,0]
    },
    'output': 20
}

tests = [test0, test1, test2, test3, test4, test5, test6]

for test in tests:
    print('Test Result:' + str(verify_ls_solution(test['input']['nums'], test['output'])), end = ' ')
    print('for ' + str(test))

print('------------------------------------------')
print('------------------------------------------')

for test in tests:
    print('Test Result:' + str(verify_bs_solution(test['input']['nums'], test['output'])), end = ' ')
    print('for ' + str(test))


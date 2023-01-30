def main():
    n = eval(input())
    print(solution([int(x) for x in input().split()]))


def solution(nums):
    if len(nums) < 6:
        return len(nums)

    next = {
        4: 8,
        8: 15,
        15: 16,
        16: 23,
        23: 42
    }

    stack = []
    curr = []
    for num in nums:
        if not curr:
            stack.append([num])
        else:
            for 
            if next[curr[-1]] == num:
                curr.append(num)
            else:


main()
'''
4 8 15 16 23 42
4 8 15 16 23 42
8
16
4
'''

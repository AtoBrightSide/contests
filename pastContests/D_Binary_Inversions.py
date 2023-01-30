def main():
    t = eval(input())
    for _ in range(t):
        n = input()
        print(solution([int(x) for x in input().split()]))

def solution(nums):
    flag = False
    turned_on = inversions = 0
    for num in nums:
        if num:
            flag = True
            turned_on += 1
        if flag and not num:
            inversions += turned_on
    
    # 0s and 1s to [left, right]
    ones = [[nums[0], nums[-1]]]
    zeroes = [[1 - nums[0], 1 - nums[-1]]]
    
    # to left
    for i in range(1, len(nums)):
        ones.append([ones[-1][0] + nums[i], ones[-1][1]])
        zeroes.append([zeroes[-1][0] + 1 - nums[i], zeroes[-1][1]])
    
    # to right
    for i in range(len(nums) - 2, -1, -1):
        ones[i][1] = ones[i + 1][1] + nums[i]
        zeroes[i][1] = zeroes[i + 1][1] + 1 - nums[i]
    
    for i in range(len(nums)):
        if nums[i]: 
            ones[i] = [ones[i][0] - 1, ones[i][1] - 1]
        else:       
            zeroes[i] = [zeroes[i][0] - 1, zeroes[i][1] - 1]

    ans = inversions
    for i, num in enumerate(nums):
        curr = ans + ((ones[i][0] - zeroes[i][1]) if num else (- ones[i][0] + zeroes[i][1]))
        inversions = max(inversions, curr)

    return inversions
        

main()
def main():
    for _ in range(eval(input())):
        eval(input())
        print(*solution([ch for ch in input()]))

def solution(line):
    L = len(line)
    if L == 1:
        return [0]

    count = [0] * L
    
    left = 0
    for i, per in enumerate(line):
        if per == "L":
            count[i] = left
        left += 1
    right = 0
    for i in range(L - 1, -1, -1):
        if line[i] == "R":
            count[i] = right
        right += 1
    
    total = sum(count)
    ans = []
    l, r = 0, L - 1
    while l < r:
        if line[l] == "L":
            total += abs(count[l] - (L - l - 1))
            ans.append(total)
        if line[r] == "R":
            curr = abs(count[r] - r)
            total += curr

            ans.append(total)
        
        l += 1
        r -= 1
    
    while len(ans) < L:
        ans.append(total)

    return ans
    

main()
def main():
    t = eval(input())
    for _ in range(t):
        print(solution(input()))

def solution(nums):
    stack = [nums[0]]
    popped = []
    for i in range(1, len(nums)):
        while stack and stack[-1] > nums[i]:
            curr = stack.pop()
            if curr == "9": 
                popped.append("9")
            else:   
                popped.append(str(int(curr) + 1))

        stack.append(nums[i])
    
    popped.sort()
    ans = []
    i = j = 0
    while i < len(stack) and j < len(popped):
        if stack[i] <= popped[j]:
            ans.append(stack[i])
            i += 1
        else:
            ans.append(popped[j])
            j += 1
    
    if i < len(stack):
        ans.extend(stack[i:])
    if j < len(popped):
        ans.extend(popped[j:])
    
    return "".join(ans)

main()

'''

stack = 1 1 1 4 4 8 8 8 9 9 9 9 9 9 9
                          ,
3 1 4 7 5 2 2 7 7 6 9 1 9 9 1
1 1 1 
4 8 5 6 8 8 3 3 7 9 9 9

0 4 8 2 9
0 2 9
9 5

'''
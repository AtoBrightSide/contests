def main():
    n = eval(input())
    costs = list(map(int, input().split()))
    strings = []
    for _ in range(n):
        strings.append([ch for ch in input()])
    
    print(solution(costs, strings))

def solution(costs, strings):
    memo = {}
    def dp(i, flag):
        if i >= len(strings):
            return 0
        
        if (i, flag) not in memo:
            prev_string = strings[i - 1][::-1] if flag else strings[i - 1]
            
            reverse = dont_reverse = float("inf")
            if prev_string <= strings[i]:
                dont_reverse = dp(i + 1, False)
            if prev_string <= strings[i][::-1]:
                reverse = costs[i] + dp(i + 1, True)
                
            memo[(i, flag)] = min(reverse, dont_reverse)
        
        return memo[(i, flag)]

    ans = min(dp(1, False), costs[0] + dp(1, True))
    return ans if ans != float("inf") else -1
    
# main()
import sys
import threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start(); thread.join()

def main():
    for _ in range(eval(input())):
        n = eval(input())
        s = [int(x) for x in input().split()]
        print(solution(s))


def solution(s):
    L = len(s)
    memo = {}

    def dp(i, turned_on):
        if i >= L:
            return 0
        
        if (i, turned_on) not in memo:
            flip = dont_flip = L
            if turned_on and s[i]:
                dont_flip = dp(i + 1, turned_on)
            elif turned_on:
                flip = 1 + dp(i + 1, turned_on)
            
            if not turned_on and s[i]:
                flip = min(1 + dp(i + 1, False), dp(i + 1, True))
            elif not turned_on:
                dont_flip = dp(i + 1, False)
            
            memo[(i, turned_on)] = min(flip, dont_flip)

        return memo[(i, turned_on)]
    
    return dp(0, False)


main()
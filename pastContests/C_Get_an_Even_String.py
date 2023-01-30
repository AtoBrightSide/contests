from collections import deque


def main():
    t = eval(input())
    for _ in range(t):
        print(solution(input()))


def solution(s):
    ans = []
    i = 0
    count = 0
    while i < len(s):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            ans.append(s[i])
            ans.append(s[i + 1])
            i += 2
        else:
            curr = s[i]
            i += 1
            while i < len(s) and curr != s[i]:
                i += 1
            if i < len(s) and curr == s[i]:
                ans.append(curr)
                ans.append(s[i])
            i += 1
    print(ans)
    return len(s) - len(ans) - (0 if len(ans) % 2 == 0 else 1)


main()

'''
aabb
'''
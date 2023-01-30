def main():
    t = eval(input())
    for _ in range(t):
        print(solution(input(), input()))


def solution(n, s):
    n = eval(n)

    count = 0

    def dp(i, curr):
        nonlocal count
        if i < n:
            curr += 1 if s[i] == "+" else -1
            if curr == 0:
                count += 1

            dp(i + 1, curr)
            if i > 0 and s[i - 1] == s[i] == "-":
                dp(i + 2, curr + 3)
        

    for i in range(n):
        dp(i, 0)
    
    return count


main()

def main():
    t = eval(input())
    for _ in range(t):
        print(solution(input(), input()))

def solution(s, c):
    if len(s) == 1:
        return "YES" if s == c else "NO"
    
    L = len(s)
    for i, ch in enumerate(s):
        if ch == c:
            if i % 2 == 0 and (L - i - 1) % 2 == 0:
                return "YES"
    
    return "NO"

main()
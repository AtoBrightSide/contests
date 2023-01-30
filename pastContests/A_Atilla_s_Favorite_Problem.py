def main():
    t = eval(input())
    for _ in range(t):
        n = input()
        print(solution(input()))

def solution(s):
    ans = 1
    for ch in s:
        index = ord(ch) - 97 + 1
        ans = max(ans, index)
    
    return ans

main()
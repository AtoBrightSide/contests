from collections import Counter
def main():
    n = eval(input())
    print(solution(input().lower()))
def solution(s):
    return "YES" if len(Counter(s)) == 26 else "NO"

main()
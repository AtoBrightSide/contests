from collections import Counter


def main():
    t = eval(input())
    for _ in range(t):
        print(solution(input()))


def solution(n):
    if not int(n) % 7:
        return int(n)
    
    n = int(n)
    mod = n % 7
    if mod > int(str(n)[-1]):
        return n + 7 - mod

    return n - mod
main()

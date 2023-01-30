import math

def main():
    for _ in range(eval(input())):
        solution(eval(input()))


def solution(n):
    if n == 1:
        print(f"1\n1 2")
        return
    
    print(math.ceil(n / 2))
    i, n = 1, 3 * n
    while i < n:
        print(f"{i} {n}")
        i += 3
        n -= 3


main()
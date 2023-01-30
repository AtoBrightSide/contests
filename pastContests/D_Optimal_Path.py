def main():
    for _ in range(eval(input())):
        n, m = input().split()
        print(solution(int(n), int(m)))

def solution(n, m):
    return sum([i for i in range(1, m + 1)]) + sum([i for i in range(m, (m * n) + 1, m)]) - m

main()

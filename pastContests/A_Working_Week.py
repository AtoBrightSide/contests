def main():
    for _ in range(eval(input())):
        print(solution(eval(input())))


def solution(n):
    one = n // 3
    two = (2 * one) - 1
    return min(abs(one - two) - 1, abs(two - n) - 1, one - 1)


main()
def main():
    for _ in range(eval(input())):
        print(solution( [int(x) for x in input().split()] ))


def solution(board):
    n, m = board[0], board[1]
    return "Tonya" if (n % 2 == m % 2) else "Burenka"


main()
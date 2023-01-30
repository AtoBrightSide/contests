def main():
    for _ in range(eval(input())):
        l, r, x = input().split()
        a, b = input().split()
        print(solution(int(l), int(r), int(x), int(a), int(b)))


def solution(l, r, x, a, b):
    if a == b:
        return 0
    if (abs(l - a) < x and abs(r - a) < x) or r - l < x:
        return -1
    if abs(a - b) >= x:
        return 1
    
    can = False
    if abs(a - r) >= x:
        if abs(r - b) >= x:
            return 2
        elif abs(l - b) >= x:
            can = True
    if abs(a - l) >= x:
        if abs(l - b) >= x:
            return 2
        elif abs(r - b) >= x:
            can = True

    return 3 if can else -1


main()

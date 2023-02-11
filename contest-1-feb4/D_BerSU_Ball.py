def main():
    n = eval(input())
    boys = [int(x) for x in input().split()]
    m = eval(input())
    girls = [int(x) for x in input().split()]

    print(solution(sorted(boys, reverse=True), sorted(girls, reverse=True)))

def solution(boys, girls):
    pairs = 0
    while boys and girls:
        if abs(boys[-1] - girls[-1]) <= 1:
            boys.pop()
            girls.pop()
            pairs += 1
        elif boys[-1] > girls[-1]:
            girls.pop()
        else:
            boys.pop()
    
    return pairs
    

main()
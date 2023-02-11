def main():
    for _ in range(eval(input())):
        n = eval(input())
        enemy = [int(x) for x in input()]
        gregor = [int(x) for x in input()]

        print(solution(enemy, gregor))

def solution(enemy, gregor):
    pawns = 0
    for i, spot in enumerate(enemy):
        if spot == 0 and gregor[i] == 1:
            pawns += 1
            gregor[i] = 2
        elif spot == 1:
            if i - 1 >= 0 and gregor[i - 1] == 1:
                pawns += 1
                gregor[i - 1] = 2
            elif i + 1 < len(gregor) and gregor[i + 1] == 1:
                pawns += 1
                gregor[i + 1] = 2
    
    return pawns
main()
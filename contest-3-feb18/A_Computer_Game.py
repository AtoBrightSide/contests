def main():
    for _ in range(eval(input())):
        eval(input())
        row1 = [int(x) for x in input()]
        row2 = [int(x) for x in input()]
        print(solution(row1, row2))

def solution(row1, row2):
    for i in range(len(row1)):
        if i + 1 < len(row1) and row1[i + 1] and row2[i + 1]:
            return "NO"
    
    return "YES"

main()
def main():
    for _ in range(eval(input())):
        print(solution(input()))

def solution(s):
    if len(s) <= 10:
        return s
    
    return s[0] + str(len(s) - 2) + s[-1]

main()
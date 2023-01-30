def main():
    t = eval(input())
    for _ in range(t):
        n, a, b = input().split()
        print(solution(int(n), int(a), int(b)))

def solution(n, a, b):
    if n - (a + b) > 1 or n == a == b:
        return "Yes"
    
    return "No"

main()
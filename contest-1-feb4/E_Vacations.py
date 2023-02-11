def main():
    
    eval(input())
    days = [int(x) for x in input().split()]
        
    print(solution(days))

def solution(days):
    prev = days[0]
    rest = 0 if days[0] else 1
    
    for i in range(1, len(days)):
        if days[i] == prev or prev == 3 or days[i] == 0:
            rest += 1
            prev = 0
        else:
            if days[i] == 3 and prev == 2:
                prev = 1
            elif days[i] == 3 and prev == 1:
                prev = 2
            else:
                prev = days[i]
    
    return rest

main()
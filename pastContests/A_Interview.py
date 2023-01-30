def main():
    n = eval(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(solution(a, b, n))

def solution(a, b, n):
    ans = 0
    for i in range(n):
        temp_b = temp_a = 0
        for j in range(i, n):
            temp_a |= a[j]
            temp_b |= b[j]
        
        ans = max(ans, temp_a + temp_b)

    return ans
main()

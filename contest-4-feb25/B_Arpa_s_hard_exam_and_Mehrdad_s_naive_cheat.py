def main():
    n = eval(input())
    if n == 0:
        return 1
    ans = [8,4,2,6]
    return ans[(n % 4) - 1]

print(main())
'''
1 = 8
2 = 64
3 = 32
4 = 16
5 = 48
6 = 64
7 = 32
8 = 16
9 = 


'''
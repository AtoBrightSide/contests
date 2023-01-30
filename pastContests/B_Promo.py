def main():
    n, q = input().split()
    price = [int(x) for x in input().split()]
    price.sort(reverse=True)
    prefix = [price[0]]
    for i in range(1, len(price)):
        prefix.append(prefix[-1] + price[i])
    for _ in range(int(q)):
        x, y = input().split()
        print(solution(prefix, int(x), int(y)))

def solution(prefix, x, y):
    left = x - y
    return prefix[x-1] - (prefix[left - 1] if x != y else 0)



main()
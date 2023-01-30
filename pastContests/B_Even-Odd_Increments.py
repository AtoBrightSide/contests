def main():
    t = eval(input())
    for _ in range(t):
        n, q = input().split()
        n = eval(n)
        count = total = 0
        for a in input().split():
            count += 1 if int(a) % 2 == 0 else 0
            total += int(a)
        
        for _ in range(eval(q)):
            tp, val = input().split()
            val = int(val)
            # even
            if tp == "0":
                total += (count * val)
                if val % 2:
                    count = 0
            
            if tp == "1":
                total += (int(n) - count) * val
                if val % 2:
                    count = n
            
            print(total)

# def solution(arr, query):
    
main()

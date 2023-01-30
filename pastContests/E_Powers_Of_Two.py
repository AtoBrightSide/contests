from collections import defaultdict
from collections import deque
from heapq import *
from collections import Counter
import bisect
 
def inp():
  n, k = input().split()
  solution(int(n), int(k))

def solution(n, k):
  if k > n and n != 1:
    print("NO")
    return
  if n == k or n == 1:
    print("YES")
    print(*[1] * k)
    return 
  
  ans = []
  while n:
    for i in range(31, -1, -1):
      shift = 1 << i
      if shift <= n:
        n -= shift
        ans.append(int(shift))
  
  if len(ans) > k:
    print("NO")
    return
  if len(ans) == k:
    print("YES")
    print(*ans)
    return
  
  print("YES")
  i = 0
  while len(ans) != k:
    while i < len(ans) and ans[i] == 1: 
      i += 1
    ans[i] /= 2
    ans.append(int(ans[i]))
  
  ans = [int(x) for x in ans]
  print(*ans)
  '''
  9 5 => 4 2 1 1 1
  
  10 1 => X
  10 2 => 8 2
  10 3 => 4 4 2
  10 4 => 4 2 2 2
  10 5 => 2 2 2 2 2
  10 6 => 2 2 2 2 1 1 1
  
  16 15 => 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
  
  7 1 => X
  7 2 => X
  7 3 => 4 2 1
  7 4 => 4 1 1 1
  7 5 => 2 2 1 1 1
  7 6 => 2 1 1 1 1 1
  
  23 3 => X
  
  '''
  
  
inp()

# import sys
# import threading
# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# thread = threading.Thread(target=inp)
# thread.start(); thread.join()
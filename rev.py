import sys


n = int(input().strip())
#n = raw_input()
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.reverse()
print(*arr)

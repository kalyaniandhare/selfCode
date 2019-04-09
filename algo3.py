import sys


def calculate_algo(a, b, k, s):
    for i in range(a-1, b):
        s[i] += k
    return s

def get_lists(l, s):
    for i in l:
        s = calculate_algo(i[0], i[1], i[2], s)
    return max(s)
        
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    s = []
    for i in range(n):
        s.append(0)
    l = []
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        l.append([int(a), int(b), int(k)])
    ans = get_lists(l, s)
    print(ans)

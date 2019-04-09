import re

def getPattern(p):
    print(p)
    te = list(p)
    
    i = 0
    for ch in p:
        print(ch)
        for m in re.finditer(ch, p):
            ind = m.start()
            te[ind] = str(i)
            i = i+1
    return ''.join(te)


s = ["abb", "abc", "xyz", "xyy"]
p = input()
ans = []
pans = getPattern(p)
for each in s:
    a = getPattern(each)
    if a == pans:
        ans.append(each)

print(ans)

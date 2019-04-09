n = int(input())
words = []
for i in range(n):
    words.append(input())

m = int(input())
find_words = []
for i in range(m):
    find_words.append(input())


ans = dict()

for word in words:
    if word in find_words:
        if word in ans:
            ans[word] += 1
        else:
            ans[word] = 1
    else:
        ans[word] = 0

print(ans)
for word in find_words:
    if word in ans:
        print(ans[word])
    else:
        print(0)
        

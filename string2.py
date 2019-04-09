a = "saveChangesInTheEditor"

count = 1
for i in a:
    print i
    if a == '':
        count = 0
    if i.isupper():
        count += 1

print(count)

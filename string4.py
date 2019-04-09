# 11
# middle-Outz
# 2
n = int(input())
s = raw_input()
k = int(input())

out = ''

def getAlphabate(small, capital, value, k, i):
    remain = 122-value
    k = k-remain
    k1 = k % 26
    #print(k1 , 'remaining', k)
    if k1 == 0:
        return k1, ord('z')
    else:
        return k1, ord('a')
    
for i in s:
    value = ord(i)
    small = 97
    capital = 65
        
    if (value >= 97 and value <= 122) or (value >= 65 and value <= 90):
        if k > 26:
            k2, val = getAlphabate(small, capital, value, k, i)
            sk = k2-1 if k2!=0 else k2
            value = val
            print('!!!!!!!!!!!', sk, value)
        else:
            sk = k2

        if value == 122:
            value = small + (sk-1)
        elif value == 90:
            value = capital + (sk-1)
        else:
            value += sk
            print('esle', value)
                
        out = out+ chr(value)
        print('$$$$$$$$$$$$$$$$$', out, chr(value))
    else:
        out = out + i
print(out)

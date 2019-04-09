# print("hello")

# print(type("Hello, World!"))

# # a = 12
# # print(type(a))

# # print(type(17))
# # print("Hello, World")
# # print(type(3.2))
# # print(type("17"))
# # print(type("3.2"))

# print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')

# print("Oh no", "she exclaimed", "Ben's bike is broken!")

# # message = """This message will
# # span several
# # lines."""
# # print(message)

# print("""This message will span
# several lines
# of the text.""")
# print("python1")
# print('''"my first python prg,new world"''')
# print('''"my first python prg,new world"''')

string1 = "my first python prg,new world"
string2 = string1 + " prajackta"
string3 = string1+ "xyz"
#print(string3)
st=string1+string2+string3+ " pqr"
print(st)
print(len(st))
print(len(string1))
#print(string1, string2)




# a = 12
# b = str(a)
# c = float(a)
# d = int(b)

# print(a, b, type(a), type(b), c, d)


# var1 = 'abcd'
# print(var1)
# var1 = 'dsds'
# print(var1)
# t=21
# s=str(t)
# p=float(t)
# r=int(t)
# print(a,b,c,d,type(s),type(p),type(r))


# def printing():

#     print('test')

# def testing(**kwargs):
#     #print(kwargs)
#     array = [1,2,3,4,5,6,7]

    
#     array.append(12)
#     array.append(122)
#     array.append(121)
#     print(array)
#     print(type(array))
#     print(array[3:])
#     array2 = array[3:] + array[:3]
#     print(array[:-2])
#     print(array[:2], array2)


# def dictionary():
#     list1 = [1,2,3,4]
#     dictionary1 = {'name': 'kalyani', 'add':'pune', 'number': list1}

#     print(dictionary1['name'])

#     dictionary1['name'] = 'prajackta'
#     print(dictionary1)
#     del dictionary1['name']
#     print(dictionary1)
    
    
# data = testing(a=1, b=2, c=2323, v='4343', g=23.45)

# # dictionary()
# # print(data)
# # a1=[11,22,33,44]
# # a1.append(55)
# # a1.append(66)
# # print(a1)
# # print(type(a1))

# def pyt():
#     l1=[21,2,3,4]
#     di1={'name': 'prajakta', 'add':'dhule', 'number':l1}
#     print(di1)
#     print(di1['name'])


# pyt()
    

def functions():

    count = 3
    a = [1,2,3,4,5]

    for i in range(len(a)):
        #print(i, a[i])
        s = a[i] * 2
        #print(s)

    for i in a:
        print(i)
        print(i*100)

    while count!=0:
        print(count)
        count = count - 1

    di1={'name': 'prajakta', 'add':'dhule', 'number': '23'}

    for k,v in di1.items():
        print(k, v)

    print(di1.keys())
    print(di1.values())
        
functions()
a=1
if a==10:
   print('true')
else:
   print('false')
   a=[1,2,4,55,66]



for i in a:
    print(i)
    print(i*50)

n=5
while n==5:
    print(n)
    n=n+2

def testing(*args):
    for i in args:
        print(i, type(i))


testing(12, 45 , 're')

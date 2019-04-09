'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
a = int(input())
gcd = []
ele = []
for i in range(a):
    gcd_and_num_of_elm = raw_input().split(' ')
    array_of_elem = raw_input().split(' ')
    gcd.append(gcd_and_num_of_elm)
    ele.append(array_of_elem)

count_of_array = []

def get_gcd_value(num, value, count):
    
    value = num%gcd_elem
    print(num, value, count)
    if value!=0:
        if value < num:
            elem = num-value
            count += 1
            count = get_gcd_value(elem, 0, count)
        elif value >= num:
            elem = num + 1
            count += 1
            count = get_gcd_value(elem, 0, count)

    return count

for elements in range(a):
    gcd_elem = int(gcd[elements][0])
    no_of_elem = int(gcd[elements][1])
    arr = [int(num) for num in ele[elements]]
    count = 0
    count1 = 0
    for i in arr:
        count1 += get_gcd_value(i, 0, 0)
    count_of_array.append(count1)
    print(count1)

# for i in range(len(count_of_array)):
#     print(i)


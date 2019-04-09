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

if len(count_of_array) == 1:
    print(count_of_array[0])
    for i in range(count_of_array):
        print(i)

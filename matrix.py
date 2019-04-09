import sys
import os
import copy
'''Complete the function below.'''

def check_horizontal(input1, output, count):
    for input_string in input1:
        string = ''.join(input_string)
        if string == output:
            count += 1
    return count


def check_digonal(inp1, output, ip1_rows, count):
    input_list=[]
    #inp1 = copy.deepcopy(input1)
    j = 0
    t = []
    for data in inp1:    
        t.append(data.pop(j))
        j += 1
    input_list.append(t)

    count = check_horizontal(input_list, output, count)
    input_list.reverse()
    count = check_horizontal(input_list, output, count)
    return count

def check_digonal_reverse(inp1, output, ip1_rows, count):
    
    input_list=[]
    #inp1 = copy.deepcopy(input1)
    for data in inp1:
        data.reverse()
        input_list.append(data)
    check_digonal(input_list, output, ip1_rows, count)
    return count


def check_vartical(inp1, output, ip1_rows, count):
    #inp1 = copy.deepcopy(input1)
    input_list=[]
    for i in range(0, ip1_rows):
        t = []
        for data in inp1:
            t.append(data.pop(0))
        input_list.append(t)
    count = check_horizontal(input_list, output, count)
    
    return count
    
def word_count(input1, input2):
    count = 0
    ip1_rows = len(input1[0])
    input_list2 = input1
    input_list3 = input1
    input_list4 = input1
    count = check_horizontal(input1, input2, count)
    count = check_vartical(input_list2, input2, ip1_rows, count)
    count = check_digonal(input_list3, input2, ip1_rows, count)
    count = check_digonal_reverse(input_list4, input2, ip1_rows, count)
    return count

ip1_rows = 0
ip1_cols = 0
ip1_rows = int(raw_input())
ip1_cols = int(raw_input())
ip1 = []
for ip1_i in xrange(ip1_rows):
    ip1_temp = map(str,raw_input().strip().split(' '))
    ip1.append(ip1_temp)
try:
    ip2 = raw_input()
except:
    ip2 = None

output = word_count(ip1, ip2)
print(str(output))

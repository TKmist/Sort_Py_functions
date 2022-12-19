import os
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]


in_file = open(input_path, 'r')

count = -1
function_code_lines = []
Functions = {}
while True:
    line = in_file.readline()
    
    if line.startswith('def'):
        function_code_lines = []
        count = 0
        
        func_name = line.split('(')[0].replace('def','').replace(' ','')
        func_vars = line.split('(')[1].split(')')[0].replace(' ','').split(',')
        function = {'Variables': func_vars,
                        'Code': function_code_lines}
    else:
        if count>=0:
            count += 1
            function['Code'].append(line)
    
    Functions[func_name]=function
    if not line:
        break
in_file.close()


KEYS = list(Functions.keys())
KEYS.sort()

with open(output_path, 'w') as funct_write:
    funct_write.write("'''Sorted functions'''\n\n")
with open(output_path, 'a') as funct_write:
    for k in KEYS:
        funct_write.write('\n\ndef '+k+'('+','.join(Functions[k]['Variables'])+'):\n')
        for L in Functions[k]['Code']:
            funct_write.write(L)




#Generate ANDNOT function using McCulloch-Pitts neural net by a python program. 

'''
Expected AND NOT output :
x1  x2  x2' output
0   0   1    0
0   1   0    0
1   0   1    1
1   1   0    0
'''

'''
x1 w1 x2 w2  (x1w1)  (x2w2)  (sum)  (T(1))  
0  1  0  -1    0       0       0      0
0  1  1  -1    0      -1      -1      0
1  1  0  -1    1       0       1      1
1  1  1  -1    1      -1       0      0

x1 x2        
0  0        1  w1
0  1       -1  w2
1  0
1  1
'''

import numpy as np

# function of checking thresold value 
def linear_threshold_gate(dot, T):
    if dot >= T:
        return 1 
    else:
        return 0

# matrix of inputs 
input_table = np.array([
    [0,0], # both no
    [0,1], # one no, one yes 
    [1,0], # one yes, one no 
    [1,1] # bot yes
])
weights = np.array([1,1])
T = 1

dot_products_sum = input_table @ weights

print(f'input table:\n{input_table}') 
print(f'dot products:\n{dot_products_sum}')

for i in range(0,4):
    activation = linear_threshold_gate(dot_products_sum[i], T) 
    print(f'Activation: {activation}')
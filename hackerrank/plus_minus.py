#!/bin/python3

import math
def plusMinus(arr):
    countPos = 0
    countNeg = 0
    countZero = 0
    lenght = len(arr)
    for item in arr:
        if item>= 0:
            if item == 0:
                countZero+=1
            else: 
                countPos+=1
        else:
            countNeg+=1
            
    print(f'{countPos/lenght:.6f}')
    print(f'{countNeg/lenght:.6f}')
    print(f'{countZero/lenght:.6f}')
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

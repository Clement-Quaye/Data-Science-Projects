
import math
import os
import random
import re
import sys
from array import *


def reverseArray(a):
    # Write your code here
    Integer_array = array('i',a)
    i = 0
    new_array = array('i')
    for x in range(-1, -len(Integer_array)):
        new_array[i] = Integer_array[x]
        i = i+1

    return new_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

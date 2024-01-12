#!/usr/bin/env python3
import ipdb

def plus_two(num):
    num = num + 2  # Reassign the result back to num
    ipdb.set_trace()
    return num

result = plus_two(3)
print(result)

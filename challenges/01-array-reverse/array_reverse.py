#!/usr/bin/env python

# Implementation discussion: https://dbader.org/blog/python-reverse-list
# http://pythontutor.com/visualize.html#code=def%20reverse_list%28arr%29%3A%0A%20%20%20%20return%20arr%5B%3A%3A-1%5D%0A%20%20%20%20%0Amy_arr%20%3D%20%5B1,2,3,4,-9%5D%0A%0Areverse_list%28my_arr%29&cumulative=false&curInstr=5&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

def reverseArray(arr):
    return arr[::-1]
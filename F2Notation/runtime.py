#!/usr/bin/python

import sys
import time

def ctime(n):
    n = n+1
    n = n+1
    return


def ntime(n):
    for i in range(1, n):
        num = i
        return

def n2time(n):
    for i in range(1, n):
      for j in range (1, n):
        num = i * j
    return



if __name__ == '__main__':
    args = sys.argv
    start_time = time.time()
    if int(args[2]) == 0:
        ctime(int(args[1]))
    elif int(args[2]) == 1:
        ntime(int(args[1]))
    elif int(args[2]) == 2:
        n2time(int(args[1]))
    else:
        print "Input Invalid"
    print("--- %s seconds ---" % (time.time() - start_time))

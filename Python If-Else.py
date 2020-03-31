#!/bin/python

import math
import os
import random
import re
import sys

def func(n):
  if(n%2!=0 or ( n%2==0 and  n in  range(6,20))):
    print("Weird")
  if(n%2==0 and ( n>20 or  n in  range (2,5))):
    print("Not Weird")
  if (n== 20):
    print("Weird")
if __name__ == '__main__':
    n = int(raw_input().strip())
    func(n)

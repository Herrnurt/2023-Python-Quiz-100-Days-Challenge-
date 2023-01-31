#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:01:15 2023

@author: boladipo
"""

def calc(arr = [3]):
    arr.append(2)
    return arr


print(sum(calc()) + sum(calc()))
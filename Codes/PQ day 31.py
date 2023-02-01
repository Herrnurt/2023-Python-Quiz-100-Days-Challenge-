#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 21:11:40 2023

@author: boladipo
"""



def foo():
    try:
        print(1, end=" ")
    finally:
        print(2)
k = foo()
print(k)
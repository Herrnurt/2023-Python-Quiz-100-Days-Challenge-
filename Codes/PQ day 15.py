#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 23:01:25 2023

@author: boladipo
"""

s1 = {5, 10, 20, 30}
s2 = {20, 25, 35}


s1.intersection_update(s2)
print(s1)

s3 = s1.intersection(s2)

print(s3)
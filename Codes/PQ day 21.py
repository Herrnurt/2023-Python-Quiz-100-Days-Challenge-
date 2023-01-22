#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:30:36 2023

@author: boladipo
"""

a = {'name' : "abc"}
b = a
c = a.copy()


a["name"] = 'xyz'
print(b['name'], c['name'])
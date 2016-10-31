#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = [int(i) for i in input('Enter numbers with delimiter space: ').split()]

i = 0
for item in a[:]:
    a.remove(item)
    i += a.count(item)
print(i)
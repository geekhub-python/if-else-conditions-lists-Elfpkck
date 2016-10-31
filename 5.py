#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = [int(i) for i in input('Enter numbers with delimiter space: ').split()]

for i in range(len(a) - 1):
    if a[i] * a[i+1] > 0:
        print(a[i], a[i+1])
        break
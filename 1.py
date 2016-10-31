#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input('Enter year: '))

if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("YES")
else:
    print("NO")

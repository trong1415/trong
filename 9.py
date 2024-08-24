# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:01:33 2024

@author: Pé Lỳ 
"""
import math
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
A = (math.sqrt(a) - math.sqrt(b)) / (math.pow(a,1/4) - math.pow(b,1/4))
B = (math.sqrt(a) + math.pow(a*b,1/4)) / (math.pow(a,1/4) + math.pow(b,1/4))
print("kết quả là:" ,A-B)
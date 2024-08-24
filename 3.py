# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:36:36 2024

@author: Pé lỳ 
"""
X = int(input("Nhập vào số N = "))
a = X // 10
b = X % 10
if 0 < X < 99:
    print(" Kết quả bài toán là:= ", a + b)
else:
    print("Lỗi hiển thị số")
    

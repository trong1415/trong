# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:16:33 2024

@author: Pé Lỳ
"""

# phương trình bậc 2
a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))
if a == 0:
    print("Phương trình không tồn tại")
else:
    if b >= 0:
        daub = " + "
    else:
        daub = " - "
    if c >= 0:
        dauc = " + "
    else:
        dauc = " - "
    print(f" {a}X^2 {daub} {abs(b)}X {dauc} {abs(c)} = 0")
        
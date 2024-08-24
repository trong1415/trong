# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:41:34 2024

@author: ADMIN
"""

print("Đai học Quốc Gia, Khu phố 6, P.Linh Trung, Q. Thủ Đức, Tp.HCM")
X = ("Đai học Quốc Gia, Khu phố 6, P.Linh Trung, Q. Thủ Đức, Tp.HCM")
x= float(input( "Nhập điều kiện 1 hoặc 2:"))
if x == 1:
    print(X.replace(",", "\n"))
elif x == 2:
    print(X.replace(", ","\n").replace(", p.","\n").replace(", Q.","\n").replace(", Tp.","\n"))
else:
    print("Không thỏa điều kiện yêu cầu")
    
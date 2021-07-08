#!/usr/bin/env python3
#-*- utf-8 -*-
'''
小明身高1.75，体重80.5kg。请根据BMI公式(体重除以身高的平方)帮小明计算他的BMI指数，并根据BMI指数：
-低于18.5：过轻
-18.5-25：正常
-25-28：过重
-28-32：肥胖
-高于32：严重肥胖
用if-elif判断并打印结果：
'''
weight = 0
height = 0
bmi = 0
result = "正常"
weight = float(input("Please input your weight(kg):"))
height = float(input("Please input your height(m):"))
bmi = weight/(height*height)
if bmi < 18.5:
    result = "过轻"
elif (bmi >= 18.5) & (bmi <25):
    result = "正常"
elif (bmi >=25) & (bmi <28):
    result = "过重"
elif (bmi >=28) & (bmi <32):
    result ="肥胖"
else: 
    result = "严重肥胖"
print("Your BMI is:%.1f" %bmi )
print("The result is:%s" %result)

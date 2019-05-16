# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:32:49 2019

@author: TWW47
"""
import pandas as pd
import numpy as np

data1=pd.read_csv("D:\cdr_fq\output_test.csv")
data2=pd.read_csv("D:\cdr_fq\output02.csv")
data3=pd.read_csv("D:\cdr_fq\output03.csv")
data4=pd.read_csv("D:\cdr_fq\output04.csv")
data5=pd.read_csv("D:\cdr_fq\output05.csv")
data6=pd.read_csv("D:\cdr_fq\output_train.csv")

row1=data1.shape[0]
row2=data2.shape[0]
row3=data3.shape[0]
row4=data4.shape[0]
row5=data5.shape[0]
row6=data6.shape[0] #获取行数

col=data1.shape[1] #获取列数
'''
first=data6.loc[[0]]    #取行

second=data1.iloc[[0]]
first.index={0}
second.index={0}
arow=(first-second)**2
a_1=arow.apply(lambda x: x.sum(), axis=1)
a1=a_1[0]

second=data1.iloc[[1]]
first.index={0}
second.index={0}
arow=(first-second)**2
a_2=arow.apply(lambda x: x.sum(), axis=1)
a2=a_2[0]
if a1>a2:
   print(a2)
if a1<=a2:
   print(a1)
'''
#进行比对
#for compare_count in range(1,5):
q=0
for expset_row in range(0,row6-1):
    row_exp=data6.iloc[[expset_row]]
    row_train=data1.iloc[0]
    row_exp.index={0}
  #  row_train.index={0}
    result_0=abs(row_exp-row_train)
    last_result_1=result_0.apply(lambda x: x.sum(), axis=1)
    last_result=last_result_1[0]
    last_index=0
    for trainset_row in range(1,row1-1):
        row_train=data1.iloc[[trainset_row]]
        row_exp.index={0}
        row_train.index={0}
        result_1=abs(row_exp-row_train)
        temp_result_1=(result_1.apply(lambda x: x.sum(), axis=1))
        temp_index=trainset_row
        temp_result=temp_result_1[0]
        if last_result>temp_result:
             last_result=temp_result
             last_index=temp_index
    if expset_row==last_index:
        q=q+1
        
print(q/(row6-1))
   # print(expset_row)
   # print(last_index)
             
             
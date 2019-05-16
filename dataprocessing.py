# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 00:31:32 2018

@author: Bason
"""
import pandas as pd

data=pd.read_csv("D:\cdr_fq\Onethousand_06.csv")
i=data['cus_num'][0]
j=0
data_handled=pd.DataFrame(columns={'cus_num','call_fre1','fre1_num4','call_fre2','fre2_num4','call_fre3','fre3_num4','call_fre4','fre4_num4','call_fre5','fre5_num4',
                                             'lac_fre1','lacfre1_num4','lac_fre2','lacfre2_num4','lac_fre3','lacfre3_num4',
                                             'cellid_fre1','cefre1_num4','cellid_fre2','cefre2_num4','cellid_fre3','cefre3_num4'})

for cusnum in range(0,997):
    new_data=pd.DataFrame([[0,0]],columns={'opp_num','numbers'})
    new_data1=pd.DataFrame([[0,0]],columns={'lac','numbers'})
    new_data2=pd.DataFrame([[0,0]],columns={'cellid','numbers'})
    k=1
    l=1
    m=1
    while data['cus_num'][j]==i:
       count1=0
       count2=0
       count3=0
       for x in range(0,k):
           if new_data['opp_num'][x]==data['opp_num'][j]:
               new_data['numbers'][x]+=1
           else:
               count1+=1
       if count1==k:
           k+=1
           new_data=new_data.append({'opp_num':data['opp_num'][j],'numbers':1},ignore_index=True)
           
       for x in range(0,l):
           if new_data1['lac'][x]==data['lac'][j]:
               new_data1['numbers'][x]+=1
           else:
               count2+=1
       if count2==l:
           l+=1
           new_data1=new_data1.append({'lac':data['lac'][j],'numbers':1},ignore_index=True)
           
       for x in range(0,m):
           if new_data2['cellid'][x]==data['cellid'][j]:
               new_data2['numbers'][x]+=1
           else:
               count3+=1
       if count3==m:
           m+=1
           new_data2=new_data2.append({'cellid':data['cellid'][j],'numbers':1},ignore_index=True)
           
       j=j+1
       print(j)
       if j==len(data.index)-1:
           break
    new_data=new_data.sort_values(['numbers'],ascending=False).head(5)
    new_data=new_data.reset_index(drop=True)
    while new_data.iloc[:,0].size<5:
        new_data=new_data.append({'opp_num':0,'numbers':0},ignore_index=True)
    new_data1=new_data1.sort_values(['numbers'],ascending=False).head(3)
    new_data1=new_data1.reset_index(drop=True)
    while new_data1.iloc[:,0].size<3:
        new_data1=new_data1.append({'lac':0,'numbers':0},ignore_index=True)
    new_data2=new_data2.sort_values(['numbers'],ascending=False).head(3)
    new_data2=new_data2.reset_index(drop=True)
    while new_data2.iloc[:,0].size<3:
        new_data2=new_data2.append({'cellid':0,'numbers':0},ignore_index=True)
    data_handled=data_handled.append({'cus_num':i,
                                     'call_fre1':new_data['numbers'][0],'fre1_num4':new_data['opp_num'][0]%10000,
                                     'call_fre2':new_data['numbers'][1],'fre2_num4':new_data['opp_num'][1]%10000,
                                     'call_fre3':new_data['numbers'][2],'fre3_num4':new_data['opp_num'][2]%10000,
                                     'call_fre4':new_data['numbers'][3],'fre4_num4':new_data['opp_num'][3]%10000,
                                     'call_fre5':new_data['numbers'][4],'fre5_num4':new_data['opp_num'][4]%10000,
                                     'lac_fre1':new_data1['numbers'][0],'lacfre1_num4':new_data1['lac'][0]%10000,
                                     'lac_fre2':new_data1['numbers'][1],'lacfre2_num4':new_data1['lac'][1]%10000,
                                     'lac_fre3':new_data1['numbers'][2],'lacfre3_num4':new_data1['lac'][2]%10000,
                                     'cellid_fre1':new_data2['numbers'][0],'cefre1_num4':new_data2['cellid'][0]%10000,
                                     'cellid_fre2':new_data2['numbers'][1],'cefre2_num4':new_data2['cellid'][1]%10000,
                                     'cellid_fre3':new_data2['numbers'][2],'cefre3_num4':new_data2['cellid'][2]%10000,},ignore_index=True)
    i=data['cus_num'][j]
print(data_handled)
writer=pd.ExcelWriter("D:\cdr_fq\output06.xlsx")
data_handled.to_excel(writer,'Sheet1')
writer.save()
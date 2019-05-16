import pandas as pd


data = pd.read_csv("F:\call_fingerprints\dataset\data\Onethousand_06.csv")
opp_max=len(data)


#建立本端号码字典
cus_num={}
i=0
j=0
for i in range(opp_max):
    if i==0:
        cus_num[j]=data['cus_num'][i]
    else:
        if data['cus_num'][i]!=cus_num[j]:
            j=j+1
            cus_num[j]=data['cus_num'][i]


cus_max=len(cus_num)
# ===============finish========================================================
# print(cus_num)
# =============================================================================

#创建单一用户数据表
single_cus={}
for k in range(cus_max):
    single_cus[k]=data[data.cus_num==cus_num[k]]
    
# ==========finish=============================================================
# print(single_cus)
# =============================================================================

#获取行数——每个用户月通话次数
single_num={}
for k in range(cus_max):
    single_num[k]=single_cus[k].shape[0]
    
# =============finish==========================================================
#print(single_num)
# ==0: 329, 1: 18, 2: 218, 3: 50, 4: 42, 5: 511, 6: 160, 7: 76, 8: 232, 9: 167===========================================================================


#上中下旬通话次数frequency
early_fre={}
mid_term_fre={}
late_fre={}
start_key=0

#分六个时间段 统计通话次数 T1. 00:00-04:00  T2. 04:00-08:00  T3. 08:00-12:00  
#T4. 12:00-16:00  T5. 16:00-20:00  T6. 20:00-24:00  
T1_fre={}
T2_fre={}
T3_fre={}
T4_fre={}
T5_fre={}
T6_fre={}

#unusal rate of roam_code 
roam_code_ur={}
#unusal rate of opp_attr_code
opp_attr_code_ur={}


for k in range(cus_max):
    
    
    early_fre[k]=0
    mid_term_fre[k]=0
    late_fre[k]=0
    
    T1_fre[k]=0
    T2_fre[k]=0
    T3_fre[k]=0
    T4_fre[k]=0
    T5_fre[k]=0
    T6_fre[k]=0
    
    roam_code_ur[k]=0
    opp_attr_code_ur[k]=0
    count1=1
    count2=1
    
    roam_code_set={}
    roam_code_set_count=[0]*100
    roam_code_set[0]=single_cus[k]['roam_code'][start_key]
    
    opp_attr_code_set={}
    opp_attr_code_set_count=[0]*100
    opp_attr_code_set[0]=single_cus[k]['opp_attr_code'][start_key]
# =============================================================================

# =============================================================================
    
    for m in range(single_num[k]):
        
        #上中下旬finish
        day=(single_cus[k]['start_time'][start_key+m]//1000000)%100
        if day<=10:
            early_fre[k]=early_fre[k]+1
        elif day<=20:
            mid_term_fre[k]=mid_term_fre[k]+1
        else:
            late_fre[k]=late_fre[k]+1
       
        #六时段计数finish
        time=(single_cus[k]['start_time'][start_key+m]//10000)%100

        if time<=4:
            T1_fre[k]=T1_fre[k]+1
        if time<=8:
            T2_fre[k]=T2_fre[k]+1
        if time<=12:
            T3_fre[k]=T3_fre[k]+1
        if time<=16:
            T4_fre[k]=T4_fre[k]+1
        if time<=20:
            T5_fre[k]=T5_fre[k]+1
        if time<=24:
            T6_fre[k]=T6_fre[k]+1
            
        #异常处理
        #unusal rate of roam_code 
        change=0
        for t in range(count1):
            if single_cus[k]['roam_code'][start_key+m]==roam_code_set[t]:
                roam_code_set_count[t]=roam_code_set_count[t]+1
                change=1
                break
        if change==0:
            roam_code_set[count1]=single_cus[k]['roam_code'][start_key+m]
            count1=count1+1
        
        #unusal rate of opp_attr_code
        change=0
        for t in range(count2):
            if single_cus[k]['opp_attr_code'][start_key+m]==opp_attr_code_set[t]:
                opp_attr_code_set_count[t]=opp_attr_code_set_count[t]+1
                change=1
                break
        if change==0:
            opp_attr_code_set[count2]=single_cus[k]['opp_attr_code'][start_key+m]
            count2=count2+1

    roam_code_ur[k]=1-max(roam_code_set_count)/sum(roam_code_set_count)
    opp_attr_code_ur[k]=1-max(opp_attr_code_set_count)/sum(opp_attr_code_set_count)

    start_key=start_key+single_num[k]


# =============================================================================
# cus_num
# single_num
# early_fre={}
# mid_term_fre={}
# late_fre={}
# T1_fre={}
# T2_fre={}
# T3_fre={}
# T4_fre={}
# T5_fre={}
# T6_fre={}
# roam_code_ur[k]=0
# opp_attr_code_ur[k]=0
# =============================================================================

fin = pd.DataFrame({'cus_num' : cus_num,
                    'single_num' : single_num,
                    'early_fre' : early_fre,
                    'mid_term_fre' : mid_term_fre,
                    'late_fre' : late_fre,
                    'T1_fre' : T1_fre,
                    'T2_fre' : T2_fre,
                    'T3_fre' : T3_fre,
                    'T4_fre' : T4_fre,
                    'T5_fre' : T5_fre,
                    'T6_fre' : T6_fre,
                    'roam_code_ur' : roam_code_ur,
                    'opp_attr_code_ur' : opp_attr_code_ur
                    })

fin.to_csv('F:\call_fingerprints\dataset\data\\Onethousand_liu_06.csv',index=0)

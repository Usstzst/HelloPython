#-*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import reflection
import pandas as pd
import numpy as np
import glob
import sys
import os
import itertools


spark = SparkSession.builder.appName("PSI").getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
engine = create_engine(
    "postgresql+psycopg2://internship:internship.wx@10.138.61.40:5432/test")
    
dis = """ select t.score,t.num/m.total as dis, substr(t.dt,1,7) as dt
           from (select 
                case when b.ccl_ext_v1_score <260 then '260以下'
                     when 260 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 280 then  '[260,280)'
                     when 280 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 300 then  '[280,300)'
                     when 300 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 320 then  '[300,320)'
                     when 320 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 340 then  '[320,340)'
                     when 340 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 360 then  '[340,360)'
                     when 360 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 380 then  '[360,380)'
                     when 380 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 400 then  '[380,400)'
                     when 400 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 420 then  '[400,420)'
                     when 420 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 440 then  '[420,440)'
                     when 440 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 460 then  '[440,460)'
                     when 460 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 480 then  '[460,480)'
                     when 480 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 500 then  '[480,500)'
                     when 500 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 520 then  '[500,520)'
                     when 520 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 540 then  '[520,540)'
                     when 540 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 560 then  '[540,560)'
                     when 560 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 580 then  '[560,580)'
                     when 580 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 600 then  '[580,600)'
                     when 600 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 620 then  '[600,620)'
                     when 620 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 640 then  '[620,640)'
                     when 640 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 660 then  '[640,660)'
                     when 660 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 680 then  '[660,680)'
                     when 680 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 700 then  '[680,700)'
                     when 700 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 720 then  '[700,720)'
                     when b.ccl_ext_v1_score >= 720 then '720以上'
                     end as score,
                     count(*) as num,
                     substr(a.dt,1,7) as dt
           from rdm.rdm_ext_v2_union a 
           left join rdm.ccl_ext_v1_score b 
           on (a.pi_v1_cert_no = b.cert_no and a.dt = b.dt)
           group by case when b.ccl_ext_v1_score <260 then '260以下'
                 when 260 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 280 then  '[260,280)'
                 when 280 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 300 then  '[280,300)'
                 when 300 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 320 then  '[300,320)'
                 when 320 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 340 then  '[320,340)'
                 when 340 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 360 then  '[340,360)'
                 when 360 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 380 then  '[360,380)'
                 when 380 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 400 then  '[380,400)'
                 when 400 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 420 then  '[400,420)'
                 when 420 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 440 then  '[420,440)'
                 when 440 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 460 then  '[440,460)'
                 when 460 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 480 then  '[460,480)'
                 when 480 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 500 then  '[480,500)'
                 when 500 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 520 then  '[500,520)'
                 when 520 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 540 then  '[520,540)'
                 when 540 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 560 then  '[540,560)'
                 when 560 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 580 then  '[560,580)'
                 when 580 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 600 then  '[580,600)'
                 when 600 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 620 then  '[600,620)'
                 when 620 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 640 then  '[620,640)'
                 when 640 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 660 then  '[640,660)'
                 when 660 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 680 then  '[660,680)'
                 when 680 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 700 then  '[680,700)'
                 when 700 <= b.ccl_ext_v1_score and b.ccl_ext_v1_score < 720 then  '[700,720)'
                 when b.ccl_ext_v1_score >= 720 then '720以上'
                 end, substr(a.dt,1,7)
            )t,
            (select substr(a.dt,1,7) as dt,count(*) as total
            from rdm.rdm_ext_v2_union a 
            left join rdm.ccl_ext_v1_score b 
            on (a.pi_v1_cert_no = b.cert_no and a.dt = b.dt)
            group by substr(a.dt,1,7)
            )m
        where t.dt= m.dt
        order by dt desc, score asc """
        
# spark读取sql代码,获取数据并保存为csv文件        
df = spark.sql(dis).toPandas()
df.columns = [dis.lower() for dis in df.columns]
df.to_csv('dis.csv', encoding ='utf-8')

# 读取csv文件，存入数据库test, 表名为test_zst_psi
df1 = pd.read_csv('dis.csv')
df1.to_sql("test_zst_psi", engine, 
    if_exists="replace", 
    index=False)

# 获取distinct dt    
ty = pd.read_sql("select distinct dt from test_zst_psi", engine)


df2 = pd.DataFrame()
for i in itertools.product(ty.dt, ty.dt):

    dis1 = """select distinct dis as dis1, score, dt as dt1
            from test_zst_psi 
            where dt = '%(i[0])s' 
            order by score
            """ % {
            "i[0]": i[0]
            }
    
    dis2 = """select distinct dis as dis2, score, dt as dt2
            from test_zst_psi
            where dt = '%(i[1])s'
            order by score
            """ % {
            "i[1]": i[1]
            } 
    
    
    data1 = pd.read_sql(dis1, engine)
    data2 = pd.read_sql(dis2, engine)
    
    psi_data = data1.merge(data2,how = 'left', left_index =True, right_index = True)
    psi_data["psi"] = (psi_data["dis1"] - psi_data["dis2"])*np.log(psi_data["dis1"]/psi_data["dis2"])
    df2 = df2.append(psi_data, ignore_index=True)
    
psi = pd.pivot_table(df2, values='psi', index='dt1', columns='dt2', aggfunc=np.sum)
psi.to_csv('psi.csv') 

"""
for i in dt1:
    for j in dt2:
        if psi[i][j] == 0:
            j = j+1
            psi[i][j]=0
"""   
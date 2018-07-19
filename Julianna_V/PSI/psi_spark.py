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
    
dis = """ sql code"""
        
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
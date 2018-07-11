#-*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import reflection
import pandas as pd
import numpy as np
import os
import itertools





os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
engine = create_engine(
    "postgresql+psycopg2://internship:internship.wx@10.138.61.40:5432/test")

df = pd.read_excel('excel表格')
df.to_sql("test_zst_psi", engine, 
    if_exists="replace", 
    index=False)
    
ty = pd.read_sql("select distinct dt from test_zst_psi", engine)


df1 = pd.DataFrame()

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
    df1 = df1.append(psi_data, ignore_index=True)
    
psi = pd.pivot_table(df1, values='psi', index='dt1', columns='dt2', aggfunc=np.sum)
psi.to_csv('psi.csv')    



    
    
    



        
        
        



 




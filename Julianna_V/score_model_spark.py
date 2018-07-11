import os
import sys

import pandas as pd

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Ha").getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

x = """ sql code"""
y = """ sql code"""
z = """sql code """        

name1 = "score_every"
name2 = "score_psi"
name3 = "score_on_off_com"

data1 = spark.sql(x).toPandas()
data1.columns = [x.lower() for x in data1.columns]
data1.to_csv('output/%s.csv'%name1,encoding = 'utf-8')

data2 = spark.sql(y).toPandas()
data2.columns = [y.lower() for y in data2.columns]
data2.to_csv('output/%s.csv'%name2,encoding = 'utf-8')

data3 = spark.sql(z).toPandas()
data3.columns = [z.lower() for z in data3.columns]
data3.to_csv('output/%s.csv'%name3,encoding = 'utf-8')    
    
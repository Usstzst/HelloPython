import os
import sys

import pandas as pd

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Ha").getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

x = """ select t.score as score, t.num/m.total as dis, t.dt as dt
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
                 a.dt
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
                 end, a.dt
            order by dt desc,score asc
            )t,
            (select a.dt,count(*) as total
            from rdm.rdm_ext_v2_union a 
            left join rdm.ccl_ext_v1_score b 
            on (a.pi_v1_cert_no = b.cert_no and a.dt = b.dt)
            group by a.dt
            order by a.dt
            )m
        where t.dt = m.dt
        order by dt desc, score asc """
y = """ select t.score,t.num/m.total as dis, substr(t.dt,1,7) as dt
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
z = """ select a.dt, 
               count(a.ccl_ext_v1_score) as off_cnt, 
               count(b.score) as cnt,
               count(case when a.ccl_ext_v1_score = b.score then 1 end) as same_cnt,
               count(b.score) - count(case when a.ccl_ext_v1_score = b.score then 1 end) as diff_cnt,
               nvl(((count(b.score) - count(case when a.ccl_ext_v1_score = b.score then 1 end))/count(b.score)),0) as diff_per,
               nvl(sum(abs(a.ccl_ext_v1_score - b.score)), 0) as diff_sum
            from rdm.ccl_ext_v1_score a
            left join tmp.zst_api_score_ccl_ext_v1 b 
            on a.report_id = b.report_id
            and a.dt = b.request_dt
            group by a.dt
            order by a.dt desc """        

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
    
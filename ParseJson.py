''' 解析json数据'''

'''json--> excel表格存储起来'''
# import json
# import xlwt
#
# # 创建excel工作表
# workbook = xlwt.Workbook(encoding='utf-8')
# worksheet = workbook.add_sheet('sheet1')
#
# # 设置表头
# worksheet.write(0, 0, label='positionName')
# worksheet.write(0, 1, label='companyShortName')
# worksheet.write(0, 2, label='industryField')
# worksheet.write(0, 3, label='companySize')
# worksheet.write(0, 4, label='district')
#
# # 读取json 文件
#
# with open('producter.json', encoding='utf-8') as f:
#     line = f.readline()
#     data_json = json.loads(line)
#
#     r = 1
#     for obj in data_json['content']['positionResult']['result']:
#         worksheet.write(r, 0, obj['positionName'])
#         worksheet.write(r, 1, obj['companyShortName'])
#         worksheet.write(r, 2, obj['industryField'])
#         worksheet.write(r, 3, obj['companySize'])
#         worksheet.write(r, 4, obj['district'])
#         r += 1
#
# workbook.save('positionName.xls')



'''json --> mongodb 存储'''

import json
from pymongo import MongoClient
import pprint


client = MongoClient('localhost', 27017)

db = client.test_database
posts = db.posts

with open('producter.json', encoding='utf-8') as f:
    line = f.readline()
    data_json = json.loads(line)

    for obj in data_json['content']['positionResult']['result']:
        print (obj['companyId'])
        posts.insert_one({
                          'companyId': obj['companyId'],
                          'positionName': obj['positionName'],
                          'companyShortName': obj['companyShortName'],
                          'industryField': obj['industryField'],
                          'companySize': obj['companySize'],
                          'district':  obj['district']
                          })

print("")
pprint.pprint(posts.find_one({"companyId": 147427}))
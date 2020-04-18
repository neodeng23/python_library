# -*- coding: utf-8 -*-
import xlrd
import requests
from xlutils.copy import copy
'''
1.读取excel测试用例
2.构建接口对应请求
3.测试结果写入excel
'''

execlDir = r'C:\xxx\xxx\111.xlsx'    # r用来取消转义
workbook = xlrd.open_workbook(execlDir)
print(workbook.sheet_names())        # 显示所有子表名，返回的是list

# 两种获取子表的方法
worksheet = workbook.sheet_names()[1]
worksheet = workbook.sheet_by_name('表名')

rows = worksheet.rows_values(1)  # 读取一行
clos = worksheet.cell_values(1)  # 读取一列
cell_data = worksheet.cell(1, 6).values  # 读取单元格

##########################################
# 写入excel
workbookr = copy(workbook)
wrsheet = workbookr.get_sheet(1)
wrsheet.write(1, 9, excel_res)
workbookr.save(r'C:\xxx\xxx\xxx\xxx.xlsx')

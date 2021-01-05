'''
workbook 工作簿
worksheet 工作表
cell 单元格
pip install -i https://mirrors.aliyun.com/pypi/simple/ openpyxl
'''

import openpyxl

# 打开工作簿
book = openpyxl.load_workbook(r'E:\workspace\selenium\ranzhi\data.xlsx')
# 获取指定的工作表
login_success = book['login_success']
# print(login_success)

# [('admin',123456),('user13','123456)]
# 方法一
data = []
for i in login_success:
    row = []
    for cell in i :
        row.append(cell.value)
    print(row)
    data.append((row))
print(data[1:])

# 方法二
# r = [tuple(cell.value for cell in row) for row in login_success]
# print(r[1:])
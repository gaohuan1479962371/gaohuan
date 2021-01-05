# 1.基本的读取文件的方式

import csv
csv_reader=csv.reader(open(r'E:\workspace\selenium\ranzhi\homework.csv',encoding='utf-8'))
for row in csv_reader:
    print(row)

# # 2.读取文件中的某一列以及多列

with open(r'E:\workspace\selenium\ranzhi\homework.csv',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    column=[row for row in reader]
    print(column[1:])

# # 3.读取文件的某一行

with open(r'E:\workspace\selenium\ranzhi\homework.csv',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    for i,rows in reader:
        if i==1:
            row=rows
    print(row)

# # 4.读取文件的行数

a=open(r"E:\workspace\selenium\ranzhi\homework.csv","r")
b=len(a.readline())
print(b)
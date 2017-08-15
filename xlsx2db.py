#!/usr/bin/python
#-*- coding:utf-8 -*-

import xlrd
from sql_test import sqlwrite
from sys import argv

if len(argv) == 3:
    workbook_name = argv[1].decode('utf-8')
    sheet_name = argv[2].decode('utf-8')
else:
    print("""
    Usage: xlsx2db.py excel文件名 sheet表单名""")
    exit(0)


with xlrd.open_workbook(workbook_name) as wb:
#    print wb.sheet_names()
#    for sn in wb.sheet_names():
#        print sn
    sh = wb.sheet_by_name(sheet_name)
    count = 0
    for row in range(sh.nrows):
        if sh.row_values(row)[0]:
            url = sh.row_values(row)[0]
        else:
            url = None
        
        if sh.row_values(row)[1]:
            class_id = int(sh.row_values(row)[1])
        else:
            class_id = None
        
        try:    
            sqlwrite(url, class_id)
            count += 1
            print("Insert url %s success!!  count: %d") % (url, count)
        except:
            pass

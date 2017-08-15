# -*- coding:utf-8 -*-

import xlwt
import mysql.connector
import time

def export_xlsx(classfied_urls, classfying_urls, invalid_urls = None):
    localtime = time.localtime(time.time())
    filename = 'excel/' + str(time.time()) + '.xls'
    wbk = xlwt.Workbook()
    sheet_classfied = wbk.add_sheet('classfied')
    sheet_classfying = wbk.add_sheet('classfying')
#    sheet_invalid = wbk.add_sheet('invalid')

    def sheet_write(sheet_name, urls):
        for row in range(len(urls)):
#            print("%s, %s") % (domains[row]['url'],domains[row]['classid'])
            sheet_name.write(row,0,urls[row]['url'])
            sheet_name.write(row,1,urls[row]['classid'])
            row  += 1

    sheet_write(sheet_classfied, classfied_urls)
    sheet_write(sheet_classfying, classfying_urls)
#    sheet_write(sheet_invalid, invalid_urls)
    wbk.save(filename)


if __name__ == '__main__':
    urls1 = [{'classid': 143, 'url': u'classfied.url.1.net'}, {'classid': 144, 'url': u'classfied.url.2.com'}]
    urls2 = [{'classid': 145, 'url': u'classfying.url.1.net'}, {'classid': 146, 'url': u'classfying.url.2.com'}]
    urls3 = [{'classid': 147, 'url': u'invalid.url.1.net'}, {'classid': 148, 'url': u'invalid.url.2.com'}]
    export_xlsx(urls1, urls2, urls3)

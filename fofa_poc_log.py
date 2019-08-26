#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第一行'''/usr/local/bin/python''' 为python的实际安装目录

import re
import requests
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def timestamp_datetime(value):
    myformat =  'The Newest Poc' +' [%Y-%m-%d]'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(myformat, value)
    return dt

def main():
    outFile=open('/root/py/test/fofa_log_OK.html','a+')
    url = 'https://fofa.so/about_client'
    outFile.write(timestamp_datetime(time.time()) +"<br/>")

    r = requests.get(url,verify=False)
    data =  r.text
##    print str(i) + ":========" + data[2500:3960]
    m_Organization = re.findall(r"class=\"poc_row\">(.+?) </div>",data,re.S)
    for my_organization in m_Organization:
##        print 'my_organization:',my_organization
        outFile.write(my_organization.replace('#28FEFC','#000000').replace('href="/result','target = "_blank" href="https://fofa.so/result') +"<br/>")
##    outFile.write(company_id_list[1]+'\t'+company_name_list[1]+'\t'+company_link_list[1]+"\n")
    print 'Done!'
    outFile.close()

if __name__ == '__main__':
    main()
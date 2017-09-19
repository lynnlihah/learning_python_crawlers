#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import requests
import os
from bs4 import BeautifulSoup

inputfile_name = 'company.txt'
outputfile_name = 'cid.txt'

def get_result(company_name):
    search_prefix = "http://hhb.cbi360.net/"
    search_body = "SearchCompanyList.aspx?key=" + urllib.parse.quote(company_name)
    search_page_url = search_prefix + search_body
    search_page = requests.get(search_page_url)
    search_out_sp = BeautifulSoup(search_page.text, 'lxml')
    cid_url = ""
    cid_href = ""
    for url in search_out_sp.find_all("a",{"class":"soso_blue"}):
        if url['title'] == company_name:
            cid_url = url['href']
    if cid_url:
        company_page = requests.get(cid_url)
        company_out_sp = BeautifulSoup(company_page.text, 'lxml')
        for li in company_out_sp.find_all("li", {"class":"company_nav_nomal"}):
            if li.a['title'] == "经营信息":
                cid_href = li.a['href']
        cid = cid_href.split('=')[1]
    return cid


print("==================================Start====================================")
output_dic = {}
try:
    f = open(inputfile_name, "r")
except FileNotFoundError:
    print("找不到输入文件")
    os.system("pause")
    exit()

lines = f.readlines()
for line in lines:
    line = line.replace("\n", "")
    line = line.strip()
    output_dic[line] = "Failed"
f.close()

for key in output_dic:
    try:
        output_dic[key] = get_result(key)
    except:
        print("Failed")
        print("公司名：\t" + key)

cid_file = open(outputfile_name,'w+')
for key in output_dic:
    cid_file.write(key)
    cid_file.write('\t')
    cid_file.write(output_dic[key])
    cid_file.write('\n')
cid_file.close()

print("==================================Work Done====================================")
os.system("pause")
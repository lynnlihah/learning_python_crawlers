#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import requests
from bs4 import BeautifulSoup

def get_result(company_name):
    search_prefix = "http://hhb.cbi360.net/"
    search_body = "SearchCompanyList.aspx?key=" + urllib.parse.quote(company_name)
    search_page_url = search_prefix + search_body
    print(search_page_url)
    search_page = requests.get(search_page_url)
    search_out_sp = BeautifulSoup(search_page.text, 'lxml')
    # print(search_out_sp)
    cid_url = ""
    cid_href = ""
    for url in search_out_sp.find_all("a",{"class":"soso_blue"}):
        if url['title'] == company_name:
            #print(url['href'])
            cid_url = url['href']
    if cid_url:
        company_page = requests.get(cid_url)
        company_out_sp = BeautifulSoup(company_page.text, 'lxml')
        # print(company_out_sp)
        for li in company_out_sp.find_all("li", {"class":"company_nav_nomal"}):
            if li.a['title'] == "经营信息":
                # print(li.a['href'])
                cid_href = li.a['href']

    cid = cid_href.split('=')[1]
    print(cid)
    return cid


output_dic = {}
f = open("company.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.replace("\n", "")
    # line = line.replace("(", "")
    # line = line.replace(")", "")
    line = line.strip()
    output_dic[line] = "not get"
f.close()

print(output_dic)
for key in output_dic:
    try:
        output_dic[key] =  get_result(key)
    except:
        print(line)

print(output_dic)
cid_file = open('cid.txt','w+')
for key in output_dic:
    cid_file.write(key)
    cid_file.write('\t')
    cid_file.write(output_dic[key])
    cid_file.write('\n')
cid_file.close()
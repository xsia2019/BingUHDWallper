"""
用于获取广西建设网上的入库企业信息

"""

#coding=utf-8
from datetime import time
from random import random

import requests
from bs4 import BeautifulSoup
# import csv
# import pandas as pd
import re
# import lxml

# url = 'http://dn4.gxcic.net:1141/cxkBackManage/HuiYuanInfoMis2_GX_Out/Pages/ShiGongInfo_Center/Unit_List.aspx'
# url2 = 'http://dn4.gxcic.net:1141/cxkBackManage/HuiYuanInfoMis2_GX_Out/Pages/DaiLiInfo_Center/DaiLiInfo_Detail.aspx'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
# }
# csvFile = 'data/companyname/companyname0614.csv'


class Gxcic(object):

    def __init__(self):
        self.url = 'http://dn4.gxcic.net:1141/cxkBackManage/HuiYuanInfoMis2_GX_Out/' \
                   'Pages/ShiGongInfo_Center/Unit_List.aspx'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }


    def get_company_name(self, html):
        page_num = self.get_page_num()
        html = self.get_html(html)

        soup = BeautifulSoup(html, "lxml")
        # 得到页码
        company_name = soup.select('td.td_companyname')
        return company_name


    def get_html(self):
        response = requests.get(self.url, headers=self.headers, timeout=30)
        return response.text

    def get_page_num(self):
        html = self.get_html()
        soup = BeautifulSoup(html, "html.parser")
        # 得到页码
        page_num = soup.select('div.PagerStatus')[0].get_text()
        page_num = re.search(r'(总页数：)(.*)', page_num).group(2)
        return page_num

    def get_data(self):
        html = self.get_html()
        soup = BeautifulSoup(html, "html.parser")

        # 得到页码
        page_num = soup.select('div.PagerStatus')[0].get_text()
        page_num = re.search(r'(总页数：)(.*)', page_num).group(2)

        __EVENTTARGET = soup.find(id="__EVENTTARGET")['value']
        __EVENTARGUMENT = soup.find(id="__EVENTARGUMENT")['value']
        ctl00_cphContent_DataGrid1_ClientState = soup.find(id="ctl00_cphContent_DataGrid1_ClientState")['value']
        __VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
        __VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")['value']
        __EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value']

        for page in range(int(page_num)):
            data_dict = {
                'ctl00$ScriptManager1': 'ctl00$UpdatePanel4|ctl00$cphContent$DataGrid1$ctl12',
                '__EVENTTARGET': __EVENTTARGET,
                '__EVENTARGUMENT': __EVENTARGUMENT,
                'ctl00_cphContent_DataGrid1_ClientState': ctl00_cphContent_DataGrid1_ClientState,
                '__VIEWSTATE': __VIEWSTATE,
                '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
                '__EVENTVALIDATION': __EVENTVALIDATION,
                'ctl00$cphCondition$tbDanWeiName': '',
                'ctl00$cphCondition$tbZuZhiJGDM': '',
                'ctl00$cphCondition$DDLXiaQu$TextDDLXiaQu': '请选择',
                'ctl00$cphCondition$DDLXiaQu$ValueDDLXiaQu': '',
                'ctl00$cphCondition$DDLHangYeType$TextDDLHangYeType': '所有',
                'ctl00$cphCondition$DDLHangYeType$ValueDDLHangYeType': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_0': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_1': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_2': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_3': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_4': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_5': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_6': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_7': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_8': '',
                'ctl00_cphContent_DataGrid1_RowSelecter_9': '',
                'ctl00$cphContent$DataGrid1$PageNumDataGrid1': page + 1,
                'ctl00$cphContent$DataGrid1$ctl14': '',
                '__ASYNCPOST': 'true',
            }
            # yield data_dict
            response = requests.post(self.url, data=data_dict, headers=self.headers, timeout=5)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'lxml')

            # links = soup.find_all('div', {'class': 'small-icon small-icon-view'})
            return soup

    def post_data(self, data):
        response = requests.post(self.url, data=data, headers=self.headers, timeout=30)
        return response.text

    def get_content(self):
        data = self.get_data()
        for dict in data:
            print(type(dict))
            print(dict)

            break



beihai = Gxcic()
links = beihai.get_data()
print(links)






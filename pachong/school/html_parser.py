# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(page_url, soup)
        name = self._get_name(page_url, soup)
        return  new_data,name

    def _get_name(self,page_url,soup):
        return soup.find('title').get_text()
    
    def _get_new_data(self, page_url, soup):
        res_datas =[]
        trs = soup.find('table', class_= "li-admissionLine").find("tbody").findAll("tr")
        for tr in trs:  #一个页面的所有信息
            
            res_data = {}
            tds = tr.findAll("td")  #一条信息
            num = 1
            for td in tds:
                s=td.get_text()
                res_data[num] = s.strip()
                num=num+1
                
            res_datas.append(res_data)
            
        return res_datas
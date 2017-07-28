# -*- coding: UTF-8 -*-
import requests
import json
from DebugHelpTools import typeprint, dictprintC,head
def outputfile(str):
    fout = open(' output', "a")
    fout.write("%s"%str)
    fout.write("\n")
    fout.close()
def printtype(object):
    print object,type(object)

#start

urlroot = '''
http://data.api.gkcx.eol.cn/soudaxue/queryProvinceScore.html\
?fstype=理科&province=重庆&size=50&lunum=1&messtype=jsonp&page='''

if __name__=="__main__":
    
    for page in range(1,2):
        url=urlroot+str(page)
        myresponsedata = requests.get(url).text
        myresponsedata = myresponsedata[5:]
        myresponsedata = myresponsedata[:-2]
        
        
     #   myresponsedata = myresponsedata.encode("UTF-8")
        jsondata = json.loads(myresponsedata)
        
        typeprint(jsondata)
        dictprintC(jsondata)
        schools = jsondata['school']
        for school in schools:
            num = school['num'].encode('UTF-8')
            schoolname = school['schoolname']
            year = school['year']
            batch = school['batch']
            var = school['var']
            outputfile(num+" "+schoolname.encode("UTF-8")+" "+year.encode("UTF-8")+" "+batch.encode("UTF-8")+" "+var.encode("UTF-8"))
    
    

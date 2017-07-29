#coding:utf-8
import json
def typeprint(*objects):                    #将输入的变量打印内容和type，输出str
    var = ""
    for myobject in objects:
        var = var + str(type(myobject)) + str(myobject)
    print var


def dictprintformatC(dictdata):                      #dict转str
    var = json.dumps(dictdata, encoding="UTF-8", sort_keys=True,indent=4,ensure_ascii=False)  
    print var
    
def dictprintC(dictdata,weatherprint = True):                      #dict转str
    var = json.dumps(dictdata, encoding="UTF-8", sort_keys=True,ensure_ascii=False)  
    if weatherprint == True:
        print var
    return var
    
def listprintC(listdata,sourcecharset="UTF-8",weatherprint = True):             #list转str
    var = ""
    for key in listdata:
        var += key
        var += " "
   # typeprint(var)
    #print var.decode("GBK")
  #  typeprint(var.decode("GBK"))
    #typeprint(var.decode("UTF-8").decode("GBK"))
    var = var.decode(sourcecharset)
    if weatherprint == True:
        print var
    return var

def head(instr,linenumber = 5):
    strline = instr.split("\n")
    var = ""
    haveprintlinenumber = 0
    for mystr in strline:
        var += mystr
        var += "\n"
        haveprintlinenumber += 1
        if haveprintlinenumber == linenumber:
            break
    print var
    
    

    
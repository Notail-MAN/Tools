# -*- coding: UTF-8 -*-
class HtmlOutputer(object):
    def output_html(self,data,name):
        fout = open('output\\ '+name, "a")
        
        for i in range(len(data)):
            for k in range(1,7):
                if k not in data[i]:
                    continue
                s = (data[i])[k]
                s=s.encode("utf-8")
                fout.write("%s"%s)
                fout.write("\t")
            fout.write("\n")
        fout.close()

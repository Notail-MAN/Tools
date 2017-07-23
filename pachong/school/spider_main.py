# coding:utf-8
import html_outputer, html_downloader, html_parser
if __name__=="__main__":
    print "您好"
    urlpart1 = "http://gkcx.eol.cn/schoolhtm/specialty/"
    urlpart2 = "/10035/specialtyScoreDetail_"
    urlpart3 = "_10028.htm"
    output = html_outputer.HtmlOutputer()
    downer = html_downloader.HtmlDownloader()
    parse = html_parser.HtmlParser()
    for id in range(30,235):
            for year in range(2008,2017):
                print year
                try:
                    url=urlpart1+str(id)+urlpart2+str(year)+urlpart3
                    print url
                    content = downer.download(url)
                    new_data,name = parse.parse(url, content)
                    output.output_html(new_data,name)
                    print id
                except Exception as e:
                    print e
                    print "fail: "+str(id) 
                
                    
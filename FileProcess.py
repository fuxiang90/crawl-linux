# 处理文件的一些函数  
#
#
# author ： fuxiang ，mail： fuxiang90@gmail.com
from BeautifulSoup import BeautifulSoup          # For processing HTML
import re
g_html_count = 0
g_txt_count = 0
    
def strip_tags(html):
    """
    Python中过滤HTML标签的函数
    >>> str_text=strip_tags("<font color=red>hello</font>")
    >>> print str_text
    hello
    """
    from HTMLParser import HTMLParser
    html = html.strip()
    html = html.strip("\n")
    result = []
    parser = HTMLParser()
    parser.handle_data = result.append
    parser.feed(html)
    parser.close()
    return ''.join(result)

##过滤HTML中的标签
#将HTML中标签等信息去掉
#@param htmlstr HTML字符串.
def filter_tags(htmlstr):
    #先过滤CDATA
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
    re_br=re.compile('<br\s*?/?>')#处理换行
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    re_comment=re.compile('<!--[^>]*-->')#HTML注释
    s=re_cdata.sub('',htmlstr)#去掉CDATA
    s=re_script.sub('',s) #去掉SCRIPT
    s=re_style.sub('',s)#去掉style
    s=re_br.sub('\n',s)#将br转换为换行
    s=re_h.sub('',s) #去掉HTML 标签
    s=re_comment.sub('',s)#去掉HTML注释
    #去掉多余的空行
    blank_line=re.compile('\n+')
    s=blank_line.sub('\n',s)
    s=replaceCharEntity(s)#替换实体
    return s

##替换常用HTML字符实体.
#使用正常的字符替换HTML中特殊的字符实体.
#你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ','160':' ',
                'lt':'<','60':'<',
                'gt':'>','62':'>',
                'amp':'&','38':'&',
                'quot':'"','34':'"',}
    
    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    sz=re_charEntity.search(htmlstr)
    while sz:
        entity=sz.group()#entity全称，如&gt;
        key=sz.group('name')#去除&;后entity,如&gt;为gt
        try:
            htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
            sz=re_charEntity.search(htmlstr)
        except KeyError:
            #以空串代替
            htmlstr=re_charEntity.sub('',htmlstr,1)
            sz=re_charEntity.search(htmlstr)
    return htmlstr

def repalce(s,re_exp,repl_string):
    return re_exp.sub(repl_string,s)


# 将html里面的内容写到文件里面去
def store_page_content(page):
    import os
    global g_txt_count
    os.chdir(r'/home/fuxiang/python/crawl-linux/file')
    soup = BeautifulSoup(page)

    allfonttext=soup.findAll(['a','p','font'])
        
    fwrite = open(str(g_txt_count) ,'w')
    # 
    if len(allfonttext)<=0:
        fwrite.close()
        return 
    for i in allfonttext:
        t = (i.renderContents() )
        context = strip_tags(t)
        fwrite.write ((context))

    g_txt_count = g_txt_count + 1
    fwrite.close()
    

#直接将html 页面写到文件里面去
def store_page(page):
    import os
    global g_html_count
    os.chdir(r'/home/fuxiang/python/crawl-linux/html')
    fwrite = open (str(g_html_count),'w')

    # 存储html 的正文
    store_page_content(page)

    g_html_count = g_html_count + 1
    fwrite.write(page)
    fwrite.close()
# 将索引写到文件里面去
def store_index(index):

    import os
    os.chdir(r'/home/fuxiang/python/crawl-linux/file')
    fwrite = open ('index','w')
    for i in index:
        fwrite.write(str(i))

    fwrite.close()

def store_index(index,filename):

    import os
    os.chdir(r'/home/fuxiang/python/crawl-linux/file')
    fwrite = open (filename,'w')
    for i in index:
        for ii in i:
            fwrite.write(ii)

    fwrite.close()
    
#    fp = open(filename,'r')
#    print fp.read()


## 默认是处理gbk 并转化utf-8
## 参数是 url 地址
def get_page(url):
    try :
        import urllib2
        content = urllib2.urlopen(url).read()
        gbk_content = content.decode('gbk')
        utf_content = gbk_content.encode('utf-8')
        return utf_content
    except:
        return ""

# 
def get_xml(url):
    try :
        import urllib2
        page = urllib2.urlopen(url)
        content = page.read()
        gbk_content = content.decode('gbk')
        utf_content = gbk_content.encode('utf-8')
        return utf_content
    except:
        return ""

# 测试用的
def test(file):
    fp = open(file,'r')
    content = fp.read()
    gbk_content = content.decode('gbk')
    utf_content = gbk_content.encode('utf-8')
#    print utf_content
    return utf_content

def test_utf(file):
    fp = open(file,'r')
    return  fp.read()
    


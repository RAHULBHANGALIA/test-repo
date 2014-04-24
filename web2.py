from urllib import *
from re import *
from csv import *
def scrapemail(link):
     link1=urlopen(link).read()
     link2=findall(r'<a href="(http.*?)"',link1)
     for title in link2:
          print "\nProcessing :"+title
          email=findall(r'([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+)',urlopen(title).read())
          print "\nemail id:"+"".join(email)
          writefile(title,email)
     return

def writefile(title,email):
               fileobject=open("w.csv","w")
               data="".join(title)+","+"".join(email)
               fileobject.write(data)
               return

def urllink(link,depth):
     #link=raw_input("input the url")
     link1=urlopen(link).read()
     link2=findall(r'<a href="(http.*?)"',link1)
     print link2
     depth=depth-1
     if(depth==0):
          return
     else:
          for link3 in link2:
               hyperlinks=urlopen(link3).read()
               title="".join(findall(r"<title.*>(.*?)<",hyperlinks))
               description="".join(findall(r'meta name="description".*?content="(.*?)"',hyperlinks))
               html='<a href="'+link3+'"><h1>'+title+'</h1></a><p>'
               html=html+'<i>'+(description)+'</i>'+'<br>'
               html=html+'<h3 style="color:red">'+link3+'</h3>'
               fileobject=open("wb5.html","a")
               fileobject.write(html)
               urllink(link3,depth)
               
               
    
    
scrapemail("http://www.indschools.co.uk/direct_links_a.shtm")

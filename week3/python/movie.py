import urllib.request as req
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#要求二

positive =[]
negative =[]
general =[]

def getData(url):
#建立request物件，附加 Request Headers的資訊，讓行為像一個正常使用者
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
    })

#解析原始碼，取得每篇文章的標題
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4 
    root=bs4.BeautifulSoup(data,"html.parser") #讓BeautifulSoup 協助我們解析 HTML格式
    titles=root.find_all("div",class_="title") #尋找class="title"的div 標籤

    for title in titles: #篩選被刪除掉的標題
         if title.a != None: #如果標題包含a標籤（沒有被刪除）
            if title.a.string[1:3]=="好雷":
                positive.append(title.a.string)
            elif title.a.string[1:3]=="負雷":
                negative.append(title.a.string)
            elif title.a.string[1:3]=="普雷":
                general.append(title.a.string)
    url="https://www.ptt.cc/bbs/movie/index.html"
    # return 下頁網址
    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]
    
url = "https://www.ptt.cc/bbs/movie/index.html"
# 爬取十頁
count = 0
while count<10:
    url = "https://www.ptt.cc"+getData(url)
    count+=1
# 輸出到 movie.txt
with open("movie.txt", mode="w", encoding="utf-8") as file:
    for i in positive:
        file.write(i)
        file.write("\n")
    for i in negative:
        file.write(i)
        file.write("\n")
    for i in general:
        file.write(i)
        file.write("\n")
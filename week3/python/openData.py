import urllib.request as request
import json
from datetime import datetime
# 要求一：Python 取得網路上的資料並儲存到檔案中

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)

list=data["result"]["results"]

#write data into csv
with open("data.csv","w",encoding="utf-8") as file: 
    for view in list: 
        scenic=view["stitle"]
        address=view["address"].split()
        district=address[1][:3]
        longitude= view["longitude"][:8]
        latitude=view["latitude"][:7]
        photo=view["file"].split("htt")
        firstphoto="htt"+photo[1]
        postYear=datetime.strptime(view["xpostDate"], '%Y/%m/%d').date().strftime("%Y")
        if int(postYear)>=2015:
            file.write(f'{scenic},{district},{longitude},{latitude},{firstphoto}\n')


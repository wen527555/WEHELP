# week5

要求三：SQL CRUD
------------

使用INSERT指令新增一筆資料到member資料表中，這筆資料的username和password欄位必須是test，接著繼續新增至少4筆隨意的資料

![picture](https://github.com/wen527555/WEHELP/blob/5f4c5637dc7877dc370362ef16d845fc09fc5642/week5/screenshot/%E5%9C%96%E7%89%87%201.png)

使用SELECT指令取得所有在member資料表中的會員資料

![picture](./screenshot/圖片 2.png)

使用SELECT指令取得所有在member 資料表中的會員資料，並按照time欄位，由近到遠排序．

![picture](./screenshot/圖片 3.png)

使用SELECT指令取得在member 資料表中第2～4共三筆資料，並按照time欄位，由近到遠排序．

![picture](./screenshot/圖片 4.png)

使用SELECT指令取得欄位 username 是test的會員資料。

![picture](./screenshot/圖片 5.png)

使用SELECT指令取得欄位 username 是test且欄位password也是test的資料。

![picture](./screenshot/圖片 6.png)

使用UPDATE指令取得欄位 username 是test的會員資料，將資料中的name欄位改成test2

![picture](./screenshot/圖片 7.png)

要求四：SQL Aggregate Functions
---------------------------

取得member資料表中，總共有幾筆資料（幾位會員）

![picture](./screenshot/圖片 8.png)

取得member資料表中，所有會員follower\_count欄位的總和

![picture](./screenshot/圖片 9.png)

取得member資料表中，所有會員follower\_count欄位的平均數

要求五：SQL JOIN
------------

![picture](./screenshot/圖片 10.png)

在資料庫中建立新資料表紀錄留言資訊，取名字為message

![picture](./screenshot/圖片 11.png)

使用SELECT搭配JOIN語法，取得所有留言，結果須包含留言者的姓名

![picture](./screenshot/圖片 12.png)

使用SELECT搭配JOIN語法，取得member資料表中欄位username是test的所有留言，資料中需包含留言者的姓名

![picture](./screenshot/圖片 13.png)

使用SELECT, SQL Aggregate Functions搭配JOIN語法，取得member資料表中欄位username是test的所有留言平均按讚數

![picture](./screenshot/圖片 14.png)

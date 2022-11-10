
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import mysql.connector
from mysql.connector import pooling

poolname='mysqlpool'
poolsize=3

dbconfig={'host':'localhost',
        'user':'root',
        'password':'wh1999ne123',
        'database':'website'}

# 創建資料庫，參數設定
connectionpool=mysql.connector.pooling.MySQLConnectionPool(
                                            pool_name=poolname,
                                            pool_reset_session='True',
                                            pool_size=poolsize,
                                            **dbconfig)

app=Flask( __name__ )
app.secret_key="any string but secret" #設定Session 的密鑰

connection=connectionpool.get_connection()
print(connectionpool.pool_name)
print(connectionpool.pool_size)
mydb = mysql.connector.connect(port='3306',
                                **dbconfig)

mycursor = mydb.cursor()

# mydb = mysql.connector.connect(user='root', password='wh1999ne123',
#                               host='127.0.0.1',
#                               database='website') #資料庫連線
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM member")

# for x in mycursor:
#   print(x)


@app.route("/") 
def index():  
    return render_template("index.html")

@app.route("/signup",methods=["POST"]) 
def signup():
    #從前端接收資料
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    #根據收到的資料，和資料庫互動
    while True:
        if (name=="" or username=="" or password==""):
            return redirect('/error?message=請輸入姓名、帳號、密碼') 
        sql = "SELECT username FROM member WHERE username = '"+ username + "'"
        mycursor.execute(sql)
        myresult=mycursor.fetchall() #獲取所有數據
        if(len(myresult))==0:
            sql="INSERT INTO member (name,username,password) VALUES (%s, %s ,%s )"
            val=(name ,username ,password)
            mycursor.execute(sql,val)
            mydb.commit()
            print("新帳號註冊成功")
            return redirect("/")       
        else:
            return redirect("/error?massage=帳號已經被註冊")


@app.route("/signin",methods=["POST"]) 
def signin():
    username=request.form["username"]
    password=request.form["password"]
    sql="SElECT name, username, password FROM member WHERE username ='"+ username + "' AND password ='"+ password + "'"
    mycursor.execute(sql)
    myresult=mycursor.fetchall() #獲取所有數據
    if len(myresult)==1:
        name=myresult[0][0]
        session["name"]=name
        session["username"]=username
        return redirect("/member")

    elif username==password=="":
        return redirect("/error?massage=請輸入帳號密碼")
    
    else:
        return redirect("/error?massage=帳號，或密碼輸入錯誤")


#處理member的網站路徑
@app.route("/member") 
def member():
    if "username" in  session:
        name=session["name"]
        return render_template("member.html",name=name )
    else: 
        return redirect("/")


#處理error的網站路徑
@app.route("/error", methods=["GET"]) 
def error():
    massage=request.args.get("massage","")
    return render_template("error.html",massage=massage)


#處理signout的網站路徑
@app.route("/signout")
def signout():
    if "username" in session:
        session.pop("username",None)    
        return redirect("/")


# @app.route("/message",methods=["POST"])
# def message():

#     id=session["id"] 
#     message=request.form["message"]
#     mycursor.execute("insert into message(member_id,content) values(%(id)s, %(message)s)", {"id":id, "message":message})
#     mydb.commit()
#     return redirect("/member")

if __name__ == "__main__":
    app.run(port=3000,debug=True) #啟動司服器，可透過port參數指定埠數

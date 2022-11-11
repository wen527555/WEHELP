
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import mysql.connector
from mysql.connector import pooling
from flask import jsonify

poolname='mysqlpool'
poolsize=3

dbconfig={'host':'localhost',
        'user':'root',
        'password':'wh1999ne123',
        'database':'website'}

# 創建資料庫，參數設定
connection_pool=mysql.connector.pooling.MySQLConnectionPool(
                                            pool_name=poolname,
                                            pool_reset_session='True',
                                            pool_size=poolsize,
                                            **dbconfig)

app=Flask( __name__ )
app.secret_key="any string but secret" #設定Session 的密鑰
app.config['JSON_AS_ASCII'] = False

connection=connection_pool.get_connection()
print(connection_pool.pool_name)
print(connection_pool.pool_size)
mydb = mysql.connector.connect(port='3306',
                                **dbconfig)

mycursor = mydb.cursor()

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

#查詢
@app.route("/api/member",methods=["GET"])
def search_member():
    username=request.args.get("username"," ")
    connection_object = connection_pool.get_connection()
    mycursor = connection_object.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM member WHERE `username`=%s" ,[username])
    myresult=mycursor.fetchone()
    if connection_object.is_connected():
        mycursor.close()
        connection_object.close()
    if myresult==None:
        return jsonify({
            "data":None
        })
    else:
        return jsonify({
            "data":{
                "id":myresult["id"],
                "name":myresult["name"],
                "username":myresult["username"]
            }
        })

#更新 
@app.route("/api/member",methods=["PATCH"])
def update_member():    
    if "username"  not in session:
        return  jsonify ({"error":True})
    if  request.method == "PATCH": 
        username=session["username"]
        new_name=request.json["name"]
        connection_object = connection_pool.get_connection() 
        cursor = connection_object.cursor(dictionary=True)
        cursor.execute("UPDATE member SET `name`= %s  WHERE `username`=%s;",[new_name,username])
        connection_object.commit()
        session["name"]=new_name
        if connection_object.is_connected():
            cursor.close()
            connection_object.close()
        return  jsonify ({"OK":True})

if __name__ == "__main__":
    app.run(port=3000,debug=True) #啟動司服器，可透過port參數指定埠數

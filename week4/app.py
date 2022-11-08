
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app=Flask(__name__)
#__name__代表目前執行的模組，建立appliction物件
app.secret_key="any string but secret" #設定Session 的密鑰


#使用POST方法,建立路徑/對應的處理函式
@app.route("/") #函式的裝飾（Decorator):以函式為基礎，提供附加的功能
def index():  #用回應路徑/對應的處理函式
    return render_template("index.html")


@app.route("/signin",methods=["POST"]) 
def signin():
    name=request.form["name"]
    password=request.form["password"]
    if (name=="" or password==""):
        return redirect('/error?message=請輸入帳號、密碼')
    elif name == "test" or password == "test":
        session["username"]=name
        return redirect("/member") 
    else:
        return redirect('/error?message=帳號、或密碼輸入錯誤')

#處理member的網站路徑
@app.route("/member") 
def member():
    if "username" in  session:
        name=session["username"]
        return render_template("member.html",name=name)
    else: 
        return redirect("/")



#處理error的網站路徑
@app.route("/error", methods=["GET"]) 
def error():
    message=request.args.get("message","")
    return render_template("error.html",message=message)


#處理signout的網站路徑
@app.route("/signout")
def signout():
    if "username" in session:
        session.pop("username",None)    
        return redirect("/")

@app.route("/square/<number>", methods=["GET"])
def square(number):
    number=int(number)
    result=number**2
    return render_template("square.html",number=number, result=result)

if __name__ == "__main__":
    app.run(port=3000) #啟動司服器，可透過port參數指定埠數

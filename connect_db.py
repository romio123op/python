from crypt import methods
from flask import Flask, render_template, request
# from flask_mysqldb import MySQL

# cài thêm thư viện
# pip3 install mysql-connector
import mysql.connector
app = Flask(__name__)


# app.config['MYSQL_HOST'] = '192.168.100.120'
# app.config['MYSQL_PORT'] = '3306'
# app.config['MYSQL_USER'] = 'ipos'
# app.config['MYSQL_PASSWORD'] = 'iT@2o19$'
# app.config['MYSQL_DB'] = 'customer'

# mysql = MySQL(app)



mydb = mysql.connector.connect(
    host="192.168.100.120",
    user="ipos",
    password="iT@2o19$",
    database="customer"
)


@app.route('/ahuhu', methods=["POST","GET"])
def index():
    if request.method == "GET":
        headers = request.headers
        token = headers.get('token', None)
        if token and token == '123456':
            return 'login noauthen'
    if request.method == "POST":
        details = request.json
        username = details.get('username', None)
        password = details.get('password', None)
        if not username or not password:
            return {
                'error': 'Thông tin param bị thiếu'
            }
        # cur = mysql.connection.cursor()
        mycursor = mydb.cursor()

        sql = "SELECT * FROM account WHERE username = %s and password = %s"
        adr = (username, password, )

        mycursor.execute(sql, adr)

        # print('connect',cur)
        # res = cur.execute("SELECT * FROM account where username = "+username+"and password="+password )
        # res = cur.execute("SELECT * FROM account")

        myresult = mycursor.fetchall()

        # mysql.connection.commit()
        # cur.close()
        if (myresult):
            return {
                "thông tin":"Đăng nhập thành công"
            }
        else:
            return {
                'error': 'Taì khoản không đúng hoặc chưa được đăng ký'
            }
    # return {
    #     'error': "login success !!!"
    # }

@app.route('/register', methods=["POST","GET"])
def reg():
    if request.method == "POST":
        details = request.json
        username = details.get('username', None)
        password = details.get('password', None)
        repassword= details.get('repassword', None)
        if password == repassword:
            mycursor = mydb.cursor()
            sql = "INSERT INTO account (username, password) VALUES (%s, %s)"
            val = (username, password)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            return{
                'thông tin':"tài khoản đã được tạo"
            }
        else:
            return{
                'thông tin':"Mật khẩu không trùng khớp"
            }
            
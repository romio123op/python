from crypt import methods
from distutils.command.config import config
import MySQLdb
from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
import config
import constant
from page import insertDB,closeDB,accountInfo,collect_login
# cài thêm thư viện
# pip3 install mysql-connector
import mysql.connector
app = Flask(__name__)


@app.route('/login', methods=["POST","GET"])
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
                "error": constant.msg.get("INFO_NOT_ENOUGH")
            }
        myresult = collect_login(username,password)
        if (myresult):
            return {
                "data": constant.msg.get("LOGGED")
            }
        else:
            return {
                'error': constant.msg.get("ERROR")
            }

@app.route('/register', methods=["POST","GET"])
def reg():
    if request.method == "POST":
        details = request.json
        username = details.get('username', None)
        password = details.get('password', None)
        repassword= details.get('repassword', None)
        if password == repassword:
            mycursor = accountInfo()
            sql = "INSERT INTO account (username, password) VALUES (%s, %s)"
            val = (username, password)
            mycursor.execute(sql, val)
            # mydb.commit()
            ins = insertDB()
            clo = closeDB()
            # mydb.close()
            return{
                    'thông tin': constant.msg.get("ACCOUNT_CREATE")
                }
        else:
            return{
                    'thông tin': constant.msg.get("CHECK_REPASS")
                }


        
            
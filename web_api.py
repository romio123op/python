from crypt import methods
from distutils.command.config import config
import MySQLdb
from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
import config
import constant
from template import rt_success,rt_error
from connect_db import insertDB,closeDB,accountInfo,collect_login,collect_register
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
            return rt_success("Đăng Nhập Thành Công")
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
            result = collect_register(username,password,repassword)
            clo = closeDB()
            return{
                    'thông tin': constant.msg.get("ACCOUNT_CREATE")
                }
        else:
            return{
                    'thông tin': constant.msg.get("CHECK_REPASS")
                }


        
            
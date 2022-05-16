from crypt import methods
from distutils.command.config import config
import MySQLdb
from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
import config
from page import insertDB
from page import closeDB
from page import accountInfo
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
                "error": config.msg.get("INFO_NOT_ENOUGH")
            }
        # mycursor = mydb.cursor()
        mycursor = accountInfo()
        sql = "SELECT * FROM account WHERE username = %s and password = %s"
        adr = (username, password, )

        mycursor.execute(sql, adr)
        myresult = mycursor.fetchall()

        if (myresult):
            return {
                "thông tin": config.msg.get("LOGGED")
            }
        else:
            return {
                'error': config.msg.get("ERROR")
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
                    'thông tin': config.msg.get("ACCOUNT_CREATE")
                }
        else:
            return{
                    'thông tin': config.msg.get("CHECK_REPASS")
                }


        
            
from crypt import methods
from distutils.command.config import config
from sqlite3 import connect
import MySQLdb
from flask import Flask, render_template, request
import config
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
    host= config.db_info['host'],
    user=config.db_info['user'],
    password=config.db_info['password'],
    database=config.db_info['database']
)

def accountInfo():
    mycursor = mydb.cursor()
    return mycursor

def insertDB():
    insert=mydb.commit()
    return insert

def closeDB():
    close = mydb.close()
    return close

def collect_login(username,password):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM account WHERE username = %s and password = %s"
    adr = (username, password)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    return myresult
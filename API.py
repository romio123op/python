from flask import Flask,request

app = Flask(__name__)
@app.route("/hello",methods = ['POST', 'GET'])
def check():
    if request.method == 'POST':
        data  = request.json
        n = data.get("x",None)
        if n:
            n = int(n)
            sb = []
            for i in range (2, n+1):
                if (check_num(i)):
                    sb.append(i)
            return {
                "data":sb
            }
        else:
            return {
                "error":"Not param"
            }
    if request.method == 'GET':
        n  = request.args.get('x')
        if n:
            n = int(n)
            sb = []
            for i in range (2, n+1):
                if (check_num(i)):
                    sb.append(i)
            return {
                "data":sb
            }
        else:
            return {
                "error":"Not param"
            }

def check_num(n):
    c = (n//2)
    for i in range(2, c + 1):
        if (n % i == 0):
            return False
    return True



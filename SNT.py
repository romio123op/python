def check_num(n):
    c = (n//2)
    for i in range(2, c + 1):
        if (n % i == 0):
            return False
    return True
 
n = int(input("input number n = "))
sb = ""
for i in range (2, n+1):
    if (check_num(i)):
        sb = sb +'\n' +str(i) + " "

f = open("snt.txt", "a")
f.write(str(sb))
f.close()

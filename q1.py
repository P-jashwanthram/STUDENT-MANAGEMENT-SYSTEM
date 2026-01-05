def checkpass(password):
    if(passlength(password) and letter(password)):
        return True
def passlength(password):
    if(password.length>=6 and password.length<=12):
        return True
    return False
def letter(password):
    count=0
    for i in range(63,)
p=input("Enter passwords")
p=p.split(",")
for i in range(0,p.length):
    x=checkpass(p[i])
    if(x):
        print(p[i])

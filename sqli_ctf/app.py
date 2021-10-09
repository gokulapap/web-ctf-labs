from flask import Flask, render_template, request
import os
import psycopg2
import base64

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

#random hidden path to create db table
@app.route("/iusdyfuhu")
def initial():
  DATABASE_URL = os.environ['DATABASE_URL']
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()

  cur.execute('''

create table users (
id SERIAL PRIMARY KEY,
username varchar(100),
password varchar(100)
);

''')

  conn.commit()
  cur.close()
  conn.close()
  return "Table created successfully!!"

@app.route("/register", methods=["POST"])
def register():
  user = request.form.get('user')
  pwd = request.form.get('pass')

  if user == 'admin':
    return render_template("index.html", data="You can't register with admin username")

  if '/static/flag.png' in user:
    user = user.replace("flag.png", "flag2.png")

  user.replace("=", "")
  user.replace("/", "")
  user.replace(";", "")

  DATABASE_URL = os.environ['DATABASE_URL']
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()

  cur.execute(f"insert into users (username, password) values ('{user}', '{pwd}'); ")
  conn.commit()
  cur.close()
  conn.close()
  return render_template("index.html", data="Registered successfully !")

@app.route("/login", methods=["POST"])
def login():
  DATABASE_URL = os.environ['DATABASE_URL']
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()

  user = request.form.get("user")
  pwd = request.form.get("pass")

  if '/static/flag.png' in user:
    user = user.replace("flag.png", "flag2.png")

  try:
    cur.execute(f"select * from users where username='{user}' and password='{pwd}';")
    t = cur.fetchall()
    t = t[0]

    conn.commit()
    cur.close()
    conn.close()

    if t:
      if str(t[1]) == 'admin':
        return '''
<center>
<h1> WELCOME ADMIN </h1>
<br><br>
<h3>
You know Admin has higher privileges ! so in this application, admin is given access to the remote sql editor !
<br><br>
!! CLICK THE BELOW BUTTON !!
</h3>
<br><br>
<a href="/sqleditor"><button>SQL EDITOR</button></a>
</center>
'''
      else:
        return "Hello " + str(t[1])
    else:
        return render_template("index.html", data="Invalid Login/Password !!")

  except Exception as e:
    print(str(e))
    return render_template("index.html", data="Invalid Login/Password !!")

@app.route("/static/flag.png")
def forbide():
    return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
'''

@app.route("/sqleditor")
def editor():
  return '''
<center>
<h1>SQL Editor</h1>
<br><br>
<form action="output" method="post">
<textarea name="sql" rows="15" cols="60">
Enter query here
</textarea>
<br><br><br>
<input type=submit value="Execute">
</form>
</center>
'''

@app.route("/output", methods=["POST"])
def creator():
  code = request.form.get('sql')
  DATABASE_URL = os.environ['DATABASE_URL']
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  res = ''

  if 'insert' in code or 'delete' in code or 'update' in code:
    try:
      cur.execute(code)
      conn.commit()
      cur.close()
      conn.close()
      return "Insertion/Deletion/updation of data sucessful !!"
    except Exception as e:
      return "Some Error occured in your SQL code : " + str(e)

  try:
    cur.execute(code)
    t = cur.fetchall()
  except Exception as e:
    return "Some Error occured in your SQL code : " + str(e)

  for i in t:
    res = res + str(i) + "<br>"

  conn.commit()
  cur.close()
  conn.close()
  return res

if __name__ == "__main__":
  app.run(port=5000)

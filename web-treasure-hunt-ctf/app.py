from flask import Flask,request,redirect
from os import system

app = Flask(__name__)

@app.route("/")
def wel():
  return '''
<center><u><h1>Welcome to Web Treasure hunt</h1></u></center><br><br>
<p>

<center>
<h3>Hint for first Path</h3>
<br>
<b><u>Hint 1:</u><br><br>
Kaalai eluntha udan solluvom = first_word<br>
namakaaga usura kudupavan = second_word<br><br><br>

<b><u>Hint 2:</u></b><br><br>
Ellorukum Hint 1 daan guru
</b>
</center>

<br><p><marquee><h4>Neengal sellum paathai siriyathagave irukatum</h4></marquee>

<!-- 🤔Innuma kandu pidikala ? Note: Intha pakkam inume vara koodathu -->
'''

#111
@app.route("/vn")
def sss():
  return '''
<center>
<h2><u>Good job! You advanced to second path</u></h2>
<p><br><br>

<h3>Hint for the next path</h3>
<br><br>
<b><u>Hint 1:</u><br><br>
Oruthan Romba nerama Enaku sms bomb panni kitte irukan, Avanuku enna number anupuna naan safe aaga muduiyum ? 🤔
</b>
</center>

'''

#222
@app.route("/429")
def bomb():
  return '''
<html>
<head><title>404 Not Found</title></head>
<body>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
</body>
<!-- ayo ithu fake page illa bro, Real 404 page daan! , ok ivlo dooram vantinga verum kaiyoda anupa manasu varala, /yagf la poi login pannuga-->
</html>
'''

#333
@app.route("/yagf")
def login():
  return '''

<center><h1>Welcome to Admin Login</h1></center>
<br><br>

<center>
<form action="/validate" method="post">
Username<br><br>
<input type=text name=usr>
<br><br>
Password<br><br>
<input type=password name=pwd>
<br><br><br>
<input type=submit>
</form>
</center>
<!--login details aa inga teduna epdi kidaikum,My Friend ku therium avan ta vena kettu parunga aHR0cDovL3RyYW5zZmVyLnNoLzFsZ0dibGMvbG9naW4udHh0 -->
'''

#444
@app.route("/validate", methods=["GET","POST"])
def check():
  if request.method == "GET":
   return "<h1>You are not authorized to view this page</h1>"
  if request.method == "POST":
   form_data = request.form
   usr = form_data['usr']
   pwd = form_data['pwd']

   if usr == 'vn_daan_vararu' and pwd == 'flag_find_panna_poraru':
    return redirect("/finalpath", code=302)
   else:
    return "<h1>Invalid Login Credentials, go to /yagf and Try Again</h1>"

#555
@app.route("/finalpath")
def last():
  return '''
<center><h1>Congratulations! you came to last page of the CTF</h1></center>
<br><br><br>
<center>
<form action="/redirect" method="post">
<input type=text name=cmd>
</form>
</center>
<!--comment section is total waste, athunala daan varatinga nu sonnen-->
'''

@app.route("/redirect", methods=["GET", "POST"])
def cmcheck():
  if request.method == 'GET':
    return "<h1>403 Forbidden</h1>"
  if request.method == 'POST':
    form_data = request.form
    if form_data['cmd'] == 'ls' or form_data['cmd'] == 'cat flagpath' or form_data['cmd'] == 'cat flag' or form_data['cmd'] == 'cat flag.txt':
      system('{} > res.txt'.format(form_data['cmd']))
      a = open('res.txt', 'r').read()
      return "<h3>{}</h3>".format(str(a))
    else:
      return redirect("/finalpath", code=302)

@app.route("/dshgfayiurhaejkhbdsajvn")
def winner():
  return "<h2>Go to /dshgfayiurhaejkhbdsajvn/{YOUR_NAME}</h2>"

@app.route("/dshgfayiurhaejkhbdsajvn/<name>")
def winnerfirst(name):
  name = name.upper()
  return '''
<center><h2>🎉CONGRATULATIONS  {}  🎉YOU DID IT !</h2></center>
<br><br><br>
<center>
<b><h3>FINAL_FLAG = NeXt_Vn_NeEnGa_DaAn</h3></b>
<br><br><br>
<p><b>COPY THE FLAG AND TAKE SCREENSHOT OF THIS PAGE AND SEND TO WHATSAPP IN DM</b></p>
</center>
<br><br><br>
<marquee>🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳</marquee>
'''.format(name)

@app.route("/hall-of-fame")
def hall():
  return '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial;
}

/* The grid: Four equal columns that floats next to each other */
.column {
  float: left;
  width: 25%;
  padding: 10px;
}

/* Style the images inside the grid */
.column img {
  opacity: 0.8; 
  cursor: pointer; 
}

.column img:hover {
  opacity: 1;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* The expanding image container */
.container {
  position: relative;
  display: none;
}

/* Expanding image text */
#imgtext {
  position: absolute;
  bottom: 15px;
  left: 15px;
  color: white;
  font-size: 20px;
}

/* Closable button inside the expanded image */
.closebtn {
  position: absolute;
  top: 10px;
  right: 15px;
  color: white;
  font-size: 35px;
  cursor: pointer;
}
</style>
</head>
<body>

<div style="text-align:center">
  <h1>🥳 CTF WINNERS 🥳</h1>
  <p>Click on the images below</p>
</div>

<!-- The four columns -->
<div class="row">
  <div class="column">
    <img src="http://transfer.sh/1iAWBUS/jopraveen.jpeg" alt="Jopraveen" style="width:100%" onclick="myFunction(this);">
  </div>
  <div class="column">
    <img src="http://transfer.sh/1LUaRAd/paul.jpeg" alt="Paul" style="width:100%" onclick="myFunction(this);">
  </div>
  <div class="column">
    <img src="http://transfer.sh/DR52/sakthi.jpeg" alt="sakthi" style="width:100%" onclick="myFunction(this);">
  </div>
</div>

<div class="container">
  <span onclick="this.parentElement.style.display='none'" class="closebtn">&times;</span>
  <img id="expandedImg" style="width:100%">
  <div id="imgtext"></div>
</div>

<script>
function myFunction(imgs) {
  var expandImg = document.getElementById("expandedImg");
  var imgText = document.getElementById("imgtext");
  expandImg.src = imgs.src;
  imgText.innerHTML = imgs.alt;
  expandImg.parentElement.style.display = "block";
}
</script>

</body>
</html>

'''

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)

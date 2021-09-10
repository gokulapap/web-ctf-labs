from flask import Flask,request,redirect,render_template,flash
from os import system

app = Flask(__name__)

@app.route("/")
def index():
  return '''
<center>
<h1> முன் கதை சுருக்கம் </h1>
<br><p>
<b>
<h3>
"VN" Ena Elloralum sellamaga alaikapadum Vanakam Nanba, Tannudaiya mudhal youtube channel aana "Jtechcode" Terminate
aana Naal andru ovaru varudamum, oru kulanthai yai kidnap seithu narabali kodupathu valakamaga veithu kondar. Athe pola intha varudamum (Flag) endra siruvanai kadathi sendrullar, kadathi sendru oru periya balam vaintha Kottaikul adaithu veithullar, Avar eppoludhum kadathiya 2 naatkal pirage kolvadhu valakagama veithullar, Athanaal antha irandu Naatkal avagasam ulla nilayil, Neengal sendru Antha flag siruvanai kaapatrungal !!!
<br><br>
<h2> 2 days only !!</h2>
<br><br>
Mudhalil /first ku sellungal, /first il daan mudhal kottai suvar irukum athil irunthu pala security suvargalai kadanthal mattume neengal vn irukum idhathiruku sendru kaapatha mudiyum !! Neenga kaapatirivinga la ?? Nambikkaya ponga flag oda tirumbi vaanga
</h3>
</b>
</center>
'''

@app.route("/first" , methods=["GET","PUT","POST"])
def welcome():
  if request.method == "GET":
    return "<center><u><h1>VN KOTTAI NULAI VAYIL</h1></u><br><br><br><h1>🚫 NO ENTRY, YOU ARE BLOCKED ! 🚫<br><br><br>🚫  TRY COMING FROM DIFFERENT ROUTE 🚫</h1></center>"
  if request.method == "PUT":
    return redirect("/rendamsuvar", code=302)
  if request.method == "POST":
    return "<center><br><br><br><h1>🚫 GOOD TRY 🚫<br><br><br>🚫 BUT AGAIN YOU ARE BLOCKED SECURITY IS HIGH HERE 🚫<br><br><br>🚫 ITHU VANAKKAM NANBA KOTTAI YARUM AVLO EASY AA NOLAYA MUDIYATHU 🚫 </h1></center>"

@app.route("/second")
def second():
 return "<h1>VN Fort aa assault aa Edai pottingala, No kuruku vali, No Loopholes !</h1>"

@app.route("/rendamsuvar")
def home():
 return render_template("kidnap.html")

@app.route("/msgfromflag")
def msg():
 return '<center><h1>Hello ! Naan daan flag</h1><br><br><h3><p>📜 Enaku romba bayama iruku, <br>Inga Romba irutta iruku, seekram vanthu help pannunga <br>inga oru anna hacker mask pottu <br>NASA va hack pantu irukaru, <br>avaru daan enna kidnap pannavaru <br>epdiyavathu vegama vanthu enna rescue pannunga 🙏🙏</h3><br><br><a href="/oneclicksuvar">Next -></a><br><br><br><br><img src="https://media.istockphoto.com/photos/old-fairytale-castle-on-the-hill-isolated-on-white-picture-id908353858?k=6&m=908353858&s=612x612&w=0&h=c7HxqHOnU6gkb-P8XXVHTik91rJb0xt97V540nArYRs=" height=310 width=500/></center>'

@app.route("/oneclicksuvar")
def oneclick():
 return render_template("login.html")

@app.route('/login.js')
def script():
 return render_template('login.js')

@app.route("/ppthacker")
def ppt():
 return '''<center><h1>🎉 Second Security Wall aa Taandi vandathuku Vaalthukkal 🎉</h1>
<br><br>
<h1>PPT HACKER WALL IS BACK !!</h1>
<br><br><br>
<h1>Find the correct Jumbled word</h1>
<br><br>
<h3>W, N, E, O, T, G, N, K, I, R</h3>
<br><br>
<!-- ungaluku familiar aana word daan -->

<form action="validate" method="post">
<b><label> Enter correct word </label></b><br><br>
<input type=text name=word><br><br>
<input type=submit value=submit>
</form>

</center>


'''

@app.route("/validate", methods=["GET","POST"])
def validate():
  if request.method == "GET":
    return "<h1>403 Forbidden</h1>"
  if request.method == "POST":
    form_data = request.form
    if form_data['word'] == 'NETWORKING':
      return redirect("alerthim")
    else:
      return redirect("ppthacker")

@app.route("/alerthim")
def alerter():
 return '''<center><h1>🎉 Third Security Wall aa Taandi vandathuku Vaalthukkal 🎉</h1>
<br><br>
<h1>One of the easiest security wall to Bypass</h1>
<br><br>
<h3>only one security bot is here, <br>The bot doesnt know who is coming out <br>and who is going in, and the bot is sleeping now <br> just alert him with "Allow Me Inside" to make the bot open the door</h3>
<br><br>

<h1>Alerter !!</h1>
<br>
<form action="check" method="post">
<input type="text" name="value">
<br><br><br>
<input type="submit" value="alert">
</form>
</center>
'''

@app.route("/check", methods=["GET", "POST"])
def check():
 if request.method == "GET":
  return "<h1>403 Forbidden</h1>"
 if request.method == "POST":
  form_data = request.form
  val = form_data['value']
  if '<' in val:
   return "<center><br><h1>WARNING : XSS PAYLOAD ('<') DETECTED !!!!</h1></center>"
  elif val == '%3Cscript%3Ealert%28%27Allow+Me+Inside%27%29%3C%2Fscript%3E':
   return redirect("finalsecuritywall")
  else:
   return "<center><br><h1>Bot Endrikala pa, Alert him well</h1></center>"

@app.route("/finalsecuritywall")
def final():
 return '''
<script>alert('Bot allowed you inside !!')</script>
<center><h1>🎉 Fourth Security Wall aa Taandi vandathuku Vaalthukkal 🎉</h1>
<br><br>
<h1>Final Security Gate Vandutinga 🥳</h1>
<br><br>
<h2>Ivlo kastamana Kottai suvargalai taandi vantha neengal super hero</h2>
<br><br>
<h2>No one can kill vanakam nanba <br> avaru avarave kill panni kitta daan undu <br> kill panna daan kaapatha mudiyum !</h2><br><br>
<h2>Name the one who can kill 🤔🤔🤔??</h2>

<form action="checker"  method="post">
<input type="text" name="name"><br><br>
<input type="submit" value="kill vn">
</form>

</center>
'''

@app.route("/checker" , methods=["GET","POST"])
def checker():
  if request.method == 'GET':
   return "<h1>403 Forbidden</h1>"
  if request.method == 'POST':
   form_data = request.form
   val = form_data['name']
   if val == '127.0.0.1':
     return redirect("udjhfewgrwgedg")
   else:
     return redirect("finalsecuritywall")

@app.route("/udjhfewgrwgedg")
def grand():
 return render_template("final.html")

if __name__ == "__main__":
  port = 5000
  app.run(port=5000)

from flask import session, Flask, request, render_template, redirect, url_for, make_response
import pyrebase

# add your auth and api keys
# firebase config
config = {
    'apiKey': "xxxxxxx",
    'authDomain': "xxxxxxx",
    'projectId': "xxxxxxx",
    'storageBucket': "xxxxxxxxx",
    'databaseURL' : "xxxxxxxx",
    'messagingSenderId': "xxxxxxxx",
    'appId': "xxxxxxxxx",
    'measurementId': "xxxxxxxxxxxx"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

#Flask app config
app = Flask(__name__)
app.secret_key = 'not_easy'

@app.route("/")
def home():
	if 'user' in session:
		return redirect(url_for('sess'))
	return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
	if request.method == "POST":
		user = request.form['susername']
		pwd = request.form['spassword']
		confirm = request.form['spassword2']
		if pwd == confirm:
			try:
				auth.create_user_with_email_and_password(user, pwd)
				return render_template("login.html", info="Registered successfully!")
			except:
				return render_template("login.html", info="Password must be atleast 6 characters in Length")
		else:
			return render_template("login.html", info="The passwords you entered do not match!")


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		user = request.form['username']
		pwd = request.form['password']
		try:
			auth.sign_in_with_email_and_password(user, pwd)
			session["user"] = user
			session.permanent = True
			return redirect("dashboard")
		except:
			return render_template("login.html", info="Invalid Email/password")

@app.route("/dashboard")
def sess():
	try:
		mail = session['user']
		name = mail.split('@')[0].capitalize()
		cook = request.cookies.get('_ga')
		if cook == 'YWRtaW5fY29va2llc19pc192ZXJ5X3Rhc3R5':
			return render_template("dashboard.html", name=name ,flag='wctf[GrEaT_yOu_ReCoVeReD_tHiS_sItE]')
		
		res = make_response(render_template('dashboard.html', name=name))
		if mail == "admin@wctf.com":
			res.set_cookie('_ga', 'YWRtaW5fY29va2llc19pc192ZXJ5X3Rhc3R5', max_age=60*60*24*365*2)		
		else:
			res.set_cookie('_ga', '25d55ad283aa400af464c76d713c07ad', max_age=60*60*24*365*2)
		return res
	except:
		return redirect(url_for('home'))

@app.route("/deshboard", methods=["GET", "POST"])
def fake_dashboard():
	if request.method == "GET":
		name = request.args.get('name')
		if name is None:
			return '''
			<pre>
@app.route("/deshboard", methods=["GET", "POST"])
def fake_dashboard():
        if request.method == "GET":
                name = request.args.get('name')
                if name is None:
                        return "" 
                        if request.method == "GET":
                                return redirect('dashboard')
                        if request.method == "POST":
                                name = request.args.get['name']
                        "" 
                else:   
                        return f"" Hello {name} ""
            </pre>
			'''
		else:	
			return '''
			<h1> Hello {} </h1>
			<!-- Nothing Here --> 
			'''.format(name)


@app.route("/test")
def tester():
  return render_template('dashboard.html')

@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for('home'))

if __name__ == "__main__":
  app.run(port=5000)


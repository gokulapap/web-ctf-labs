from flask import Flask, request, send_file, render_template, make_response
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import random
import os

app = Flask("ss app")

options = webdriver.FirefoxOptions()
options.headless = True

@app.route("/")
def index():
  return render_template("ss.html")

@app.route("/screenshot", methods=["POST"])
def ss():
 try:
  if request.method == "POST":
   if request.cookies.get("cookie_check") == "yes":
    return render_template('ss.html', info="Wait for 15 seconds to try next URL")
   else:
    url = request.form['url']
    driver = webdriver.Firefox(executable_path="/root/coding/python/flaskapps/ss_ctf/challenge/geckodriver", options=options)

    if 'http://127.0.0.1:5000' in url or 'http://0.0.0.0:5000' in url:
      sleep(2.5)
      resp = make_response(send_file('/root/coding/python/flaskapps/ss_ctf/challenge/templates/ss_104.png', as_attachment=True))
      resp.set_cookie('cookie_check','yes', max_age=15)
      return resp

    elif 'view-source:http://127.0.0.1:5000' in url or 'view-source:http://0.0.0.0:5000' in url:
      sleep(2.5)
      resp1 = make_response(send_file('/root/coding/python/flaskapps/ss_ctf/challenge/templates/ss_204.png', as_attachment=True))
      resp1.set_cookie('cookie_check','yes', max_age=15)
      return resp1

    elif 'http://127.0.0.1:5000/sagfdhf.txt' in url or 'http://0.0.0.0:5000/sagfdhf.txt' in url:
      sleep(2.5)
      resp2 = make_response(send_file('/root/coding/python/flaskapps/ss_ctf/challenge/templates/ss_302.png', as_attachment=True))
      resp2.set_cookie('cookie_check','yes', max_age=15)
      return resp2

    driver.get(url)
    file = '/root/coding/python/flaskapps/ss_ctf/challenge/ss/ss_{}.png'.format(random.randint(111,999))

    print(driver.get_screenshot_as_file(file))
    resp3 = make_response(send_file(file, as_attachment=True))
    resp3.set_cookie('cookie_check','yes', max_age=15)
    driver.close()
    return resp3

 except:
  return render_template("ss.html", info="some error occured try again !")


@app.route("/nmap")
def nmap():
  return '''
Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-20 15:58 IST <br>
Nmap scan report for localhost (127.0.0.1) <br>
Host is up (0.00018s latency).<br>
Not shown: 995 closed ports<br>
PORT     STATE SERVICE<br>
1717/tcp open  fj-hdnet<br>
5000/tcp open  upnp<br>
7200/tcp open  fodms<br>
9000/tcp open  http-alt<br>
<br>
Nmap done: 1 IP address (1 host up) scanned in 0.22 seconds
'''

if __name__ == "__main__":
   app.run(port=9000)

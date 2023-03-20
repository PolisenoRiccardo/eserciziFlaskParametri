from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("formPOST.html") 

@app.route('/login', methods = ['POST'])
def login():
  user = request.form['user']
  password = request.form['pasw']
  if  user == 'admin' and password == 'xxx123#':
    return render_template("login.html", user = user) 
  else:
    return render_template("errore.html") 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

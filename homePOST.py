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
    genere = request.form['s']
    if genere == 'Male':
      return render_template("login.html", user = user, ao = 'o') 
    elif genere == 'Female':
      return render_template("login.html", user = user, ao = 'a') 
    elif genere == 'FilippoNeri':
      return render_template("login.html", user = user, ao = 'ǝ')
  else:
    return render_template("errore.html") 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

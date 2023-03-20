from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("hobbies.html", methods = ['GET']) 

@app.route('/hobbies', methods = ['GET'])
def hobbies():
    obbies = request.form.getlist('hobby')
    return render_template("hobbies1.html", hobbies = obbies) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
